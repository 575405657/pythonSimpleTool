import ffmpeg
import os
from PIL import Image

file_path = 'input_video'
logo = Image.open('left_logo.png')
filenames = os.listdir(file_path)
for f in filenames:
    file_info = f.split(".")
    print(file_info[0])
    dir_path = os.path.realpath(__file__)
    path = os.path.dirname(dir_path) + "\\" + file_path + "\\" + f
    print(path)
    probe = ffmpeg.probe(path)
    video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
    width = int(video_stream['width'])
    height = int(video_stream['height'])
    print("此视频的大小为：%s,%s" % (width, height))
    main = ffmpeg.input(path)
    audio_stream = ffmpeg.input(path).audio
    logo = logo.resize((width, height), Image.ANTIALIAS)
    logo.save("left_logo_temp.png")
    v_logo = ffmpeg.input("left_logo_temp.png")
    ffmpeg.filter([main, v_logo], 'overlay', 0, 0).output(audio_stream, "output_video\\" +
                                                          f + '_有水印.' +
                                                          file_info[-1]).run()
