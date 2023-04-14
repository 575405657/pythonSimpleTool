from os import system
import time

name = input("输入name：")
system("ffmpeg -i " + name + ".mp4 -vn -codec copy sound.m4a")
time.sleep(10)
system('ffmpeg -i "sound.m4a" -y -acodec libmp3lame -aq 0 "sound.mp3"')
time.sleep(10)
system('spleeter separate -p spleeter:2stems -o output sound.mp3')
time.sleep(10)
system('ffmpeg -i ' + name + '.mp4" -y -f mp4 -an -codec copy -q:v 1 "audio-无声.mp4"')
time.sleep(10)
system(
    'ffmpeg -i ' + name + '.mp4 -i output/sound/accompaniment.wav -c:v copy -c:a aac -strict experimental audio-消音.mp4')

print("完成")
