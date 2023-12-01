import os,subprocess
import time,json
import ffmpeg

def convert_video_to_mp4(input_file, output_file):
    ffmpeg_cmd = [
        "ffmpeg",
        "-i", input_file,
        output_file
    ]
    try:
        subprocess.run(ffmpeg_cmd, check=True)
        print("Successfully converted!")
        os.remove(input_file)
    except subprocess.CalledProcessError as e:
        print("Conversion failed!")
       
while True:
    try:
        for file in os.listdir("files/input"):
            input_name = "files/input/"+file
            output_name = "files/output/"+file.split('.')[0]+".mp4"
            #print(output_name)
            convert_video_to_mp4(input_name,output_name)
    except:
        print('error')