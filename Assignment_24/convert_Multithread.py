from threading import *
from time import time
from moviepy.editor import * 


def Vide2Audio(video_file,audio_name):
    video = VideoFileClip(video_file)
    video.audio.write_audiofile(audio_name)

VideoUrl_list=[
    ["https://as6.asset.aparat.com/aparat-video/b046ad35e8e376f095207d5af28ca2ca21156598-144p.mp4?wmsAuthSign=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6IjBmYjI5NGNlM2VjYzFmZDkyMTc0MTlmZTY1YzFhYTNjIiwiZXhwIjoxNjc4NTcxMDY2LCJpc3MiOiJTYWJhIElkZWEgR1NJRyJ9.Z94F4aWRNvp9SIG4q7SjKiDJyGq-_iomKSGRTZ-aDSQ","LastKingdom.mp3"],
    ["https://aspb15.asset.aparat.com/aparat-video/08116733a7d8d4559193b86cf920990116897166-144p.mp4?wmsAuthSign=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6ImUwNWY1MzhmN2M1MDIwMDhiNWUyYTVmOTZiZDUwOWI4IiwiZXhwIjoxNjc4NTcxOTEyLCJpc3MiOiJTYWJhIElkZWEgR1NJRyJ9.Ve3eyUrcHp_7wojxUE_0nwe2sztmxxamCsojHkOkAaE","ThisisUs.mp3"],
    ["https://aspb31.asset.aparat.com/aparat-video/0ab21cba987eaee24c796efa5341de4834999337-144p.mp4?wmsAuthSign=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6IjA2MzM0ZTBjNmExMjdmYjhjM2MxYzg5Yjk2MWMyODFjIiwiZXhwIjoxNjc4NTcyMzIwLCJpc3MiOiJTYWJhIElkZWEgR1NJRyJ9.g63RQdXwDl_iL8XvBBcHK4LjF9dM1kW_Fgbbo5Bz0t4","TRANSYLVANIA.mp3"],
    ["https://hw14.asset.aparat.com/aparat-video/5528cb47aa372daa521af39d10b4b14613381616-144p.mp4?wmsAuthSign=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6ImExNjY5NmViNmVlZDQ3YjI0NDdlMzE5MWRhMzM0Mzg4IiwiZXhwIjoxNjc4NTcyMDI1LCJpc3MiOiJTYWJhIElkZWEgR1NJRyJ9.oIuU3Qs3FOfvFZDkm_F5MI-X2bgujiy7Tl82rb1Y9Go","Interstellar.mp3"],
    ["https://aspb1.asset.aparat.com/aparat-video/226064db51fcdfc7c16fdfdaac624d0c6796260-270p.mp4?wmsAuthSign=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6IjljMmJmOWQwMzkyMTQwNDgwYWUyMGE4MmIzZGY4ZTJiIiwiZXhwIjoxNjc4NTcyMTc3LCJpc3MiOiJTYWJhIElkZWEgR1NJRyJ9.RAQ-9iamAsbVnu3l8CBsEoA2DkjI7i6huPid3ttE4uw","Lion.mp3"],
]
threads=[]
start_time2=time()

for url,audio in VideoUrl_list:
    new_thread=Thread(target=Vide2Audio,args=[url,audio])
    threads.append(new_thread)

for t in threads:
    t.start()

for t in threads:
    t.join()

end_time2=time()

print("Running time with multi threading is ",end_time2-start_time2," seconds")