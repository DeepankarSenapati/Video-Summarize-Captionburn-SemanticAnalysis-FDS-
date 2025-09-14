import subprocess
import os


def burn_subtitles(video_path, srt_relative_path, output_path, ffmpeg_path):

    #get absolute paths for video and output
    video_full = os.path.abspath(video_path)
    output_full = os.path.abspath(output_path)

    #use the relative path for subtitles exactly as it worked in your manual command.
    # make sure the working directory is the project directory.
    command = f'"{ffmpeg_path}" -i "{video_full}" -vf "subtitles={srt_relative_path}" "{output_full}"'

    print("Running command:")
    print(command)

    try:
        subprocess.run(command, shell=True, check = True)
        print(f"[✅] Video with burned-in captions generated: {output_full}")
    except subprocess.CalledProcessError as e:
        print(f"[!] Error burning subtitles: {e}")

if __name__== "__main__":
    #update this to the path of your working FFmpeg excutable (withh libass support).
    ffmpeg_path = r"C:\ffmpeg-2025-07-21-git-8cdb47e47a-essentials_build\bin\ffmpeg.exe"

    #use relative path for the subtitles (exactly as yiu used in the working command)
    video_file = "videos/sample_video.mp4" # Input video file (can be relative or absolute)
    srt_relative_path = "captions/output.srt" #use the relative path here!
    output_video = "videos/output_video.mp4" #output video file with subtitles burned in

    burn_subtitles(video_file, srt_relative_path, output_video, ffmpeg_path)



