import os
from os import *

TitleZero=('title ffmpeg.py')
os.system(TitleZero)
os.system("color 01")
os.system("mode con: cols=79 lines=15")
cls = 'cls'
os.system(cls)
cec0 = '.\\bin\\cecho.exe'
cec1 = (cec0+' {03}')
cec2 = (cec0+' {01}')
cec3 = (cec0+' {04}')
cec4 = (cec0+' {06}')
os.system(cec1+"By Kia7L: ffmpeg.py")
print''
os.system(cec2+"Place Movie In BlockBuster!")
print''
os.system(cec3+"FinishConverted Movie In DoneBuster!")
print''
os.system(cec4)
a1=(raw_input("Video.NAME.Only.Used! : "))
a2=(raw_input("Video.FileType.Used! : "))
b=(raw_input("VideoConverting?FileTypeName! : "))
f=(raw_input("libvorbis or flac : "))
formula=('cd (-c:a -ax-9*11111111/0.00000001/0x01)<NUL')
c=('.\\bin\\ffmpeg.exe -i .\\BlockBuster\\'+a1)
d=(' -c:v vp9 -c:a '+f)
e=(' .\\DoneBuster\\'+a1)
p=('.')
os.system(formula+c+p+a2+d+e+p+b)
print(a1+': ALL DONE!!!')
input()
