import os
import subprocess
import streamlit as st
from datetime import timedelta
import whisper
import srt 
from moviepy.video.io.VideoFileClip import VideoFileClip
from textblob import TextBlob
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# Initialize GPT-2 model and tokenizer globally
@st.cache_resource
def load_gpt2_model():
    """Load GPT-2 model and tokenizer for summarization"""
    try:
        model_name = "gpt2"
        tokenizer = GPT2Tokenizer.from_pretrained(model_name)
        model = GPT2LMHeadModel.from_pretrained(model_name)
        
        # Set pad token to eos token for GPT-2
        tokenizer.pad_token = tokenizer.eos_token
        model.config.pad_token_id = model.config.eos_token_id
        
        return model, tokenizer
    except Exception as e:
        st.error(f"Error loading GPT-2 model: {e}")
        return None, None

# --- Step 1: Audio Extraction ---
def extract_audio(video_path,output_audio_path):
    try:
        video = VideoFileClip(video_path)
        audio = video.audio
        if audio:
            audio.write_audiofile(output_audio_path)
            return True
        else:
            st.error("[!] No audio track found in the video")
            return False
    except Exception as e:
        st.error(f"Error extracting the audio: {e}")
        return False

#--- Step 2 : trascription using whisper---
def transcribe_audio(audio_path):
    try:
        model = whisper.load_model("tiny")
        result = model.transcribe(audio_path)
        return result
    except Exception as e:
        st.error(f"Error transcribing audio: {e}")
        return None 

# merging summarization projects
def summarize_text(text):
    try:
        # Load GPT-2 model and tokenizer
        model, tokenizer = load_gpt2_model()
        if model is None or tokenizer is None:
            return "Error: Could not load GPT-2 model"
        
        # Truncate text if too long (GPT-2 has token limits)
        max_input_length = 500
        if len(text) > max_input_length:
            text = text[:max_input_length] + "..."
        
        # Create a prompt for summarization
        prompt = f"Summarize the following text in a concise paragraph:\n\n{text}\n\nSummary:"
        
        # Tokenize the input
        inputs = tokenizer.encode(prompt, return_tensors="pt", truncation=True, max_length=1024)
        
        # Generate summary
        with torch.no_grad():
            outputs = model.generate(
                inputs,
                max_length=inputs.shape[1] + 100,  # Generate up to 100 more tokens
                num_return_sequences=1,
                temperature=0.7,
                do_sample=True,
                pad_token_id=tokenizer.eos_token_id
            )
        
        # Decode the generated text
        generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Extract the summary part (after "Summary:")
        if "Summary:" in generated_text:
            summary = generated_text.split("Summary:")[-1].strip()
        else:
            summary = generated_text[len(prompt):].strip()
        
        return summary if summary else "Unable to generate summary"
        
    except Exception as e:
        st.error(f"Error summarizing text: {e}")
        return ""
#merging projects

# merging NLP projects
def analyze_sentiment(text):
    try:
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity
        if polarity > 0:
            sentiment = "Positive"
        elif polarity < 0:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"
        return sentiment, polarity, subjectivity
    except Exception as e:
        st.error(f"Error analyzing sentiment: {e}")
        return "Error", 0, 0

#--- Step 3: Generate SRT File---
def generate_srt(transcription_result):
    try:
        subtitles=[]
        for i,seg in enumerate(transcription_result.get('segments', [])):
            subtitle = srt.Subtitle(
                index=i+1,
                start=timedelta(seconds=seg['start']),
                end=timedelta(seconds=seg['end']),
                content=seg['text'].strip()
            )
            subtitles.append(subtitle)
        return srt.compose(subtitles)
    except Exception as e:
        st.error(f"Error generating SRT: {e}")
        return ""
    
#--- Step 4: Burn Subtitles using FFmpeg---
def burn_subtitles(video_path, srt_relative_path, output_path, ffmpeg_path):
    #This uses the working command with relative path for SRT
    video_full = os.path.abspath(video_path)
    output_full = os.path.abspath(output_path)
    command = f'"{ffmpeg_path}" -i "{video_full}" -vf "subtitles={srt_relative_path}" "{output_full}"'
    try:
        subprocess.run(command, shell=True, check = True)
        return True
    except subprocess.CalledProcessError as e:
        st.error(f"Error burning subtitles: {e}")
        return False

#--- Main Streamlit App---
def main():
    st.title("AI-Powered Video Caption Generator")
    st.write("Upload a video to generate and burn captions onto it.")

    #File uploader for video
    uploaded_video=st.file_uploader("Upload Video", type=["mp4", "mov"])
    if uploaded_video:
        #Save the uploaded video
        video_path="videos/uploaded_video.mp4"
        os.makedirs("videos",exist_ok=True)
        with open(video_path, "wb") as f:
            f.write(uploaded_video.getbuffer())
        st.video(video_path)

        if st.button("Generate Captions"):
            #Step 1: Extract Audio
            os.makedirs("audio", exist_ok=True)
            audio_path = "audio/uploaded_audio.wav"
            st.write("Extracting audio...")
            if not extract_audio(video_path, audio_path):

                return

            # Step 2: Transcribe Audio
            st.write("Transcribing audio...")
            transcription_result = transcribe_audio(audio_path)
            if not transcription_result:
                return
            st.write("Transcript Result:")
            transcribed_text = transcription_result.get("text", "")
            st.session_state.transcribed_text = transcribed_text
            st.session_state.transcription_result = transcription_result  # <-- Add this line
            st.write(transcribed_text)

        if "transcribed_text" in st.session_state and st.session_state.transcribed_text:
            if st.button("Summarize Transcript"):
                summary = summarize_text(st.session_state.transcribed_text)
                st.subheader("Summary:")
                st.write(summary)

            if st.button("Analyze Sentiment"):
                sentiment, polarity, subjectivity = analyze_sentiment(st.session_state.transcribed_text)
                st.subheader("Sentiment Analysis:")
                st.write(f"Sentiment: {sentiment}")
                st.write(f"Polarity: {polarity:.2f}")
                st.write(f"Subjectivity: {subjectivity:.2f}")

            #step 3: Generate SRT File
        if "transcription_result" in st.session_state and st.session_state.transcription_result:
            srt_content = generate_srt(st.session_state.transcription_result)
            # ...rest of your code...
            os.makedirs("captions", exist_ok=True)
            srt_path ="captions/uploaded_output.srt"
            with open(srt_path, "w", encoding="utf-8") as f:
                f.write(srt_content)
            st.success("SRT file generated.")

            # Step 4: Burn Subtitles onto Video
            ffmpeg_path= r"C:\ffmpeg-2025-07-21-git-8cdb47e47a-essentials_build\bin\ffmpeg.exe"
            st.write("Burning subtitles onto video...")
       
            if burn_subtitles(video_path, srt_path, "videos/uploaded_output_video.mp4", ffmpeg_path):
                st.success("Video with burned-in captions generated!")
                st.video("videos/uploaded_output_video.mp4")
if __name__=="__main__":
    main()





