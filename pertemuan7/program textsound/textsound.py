from gtts import gTTS 
from playsound import playsound

mytext = 'Selamat Datang di Fakultas Teknik! Namaku Muhammad Yusuf Kurnia dari TIF22D'
language = 'id'
myobj = gTTS(text=mytext, lang=language, slow=False) 

myobj.save("selamat_datang.mp3") 
playsound("selamat_datang.mp3", True)