import sounddevice
from scipy.io.wavfile import write

fs = 44100
second = int(input("Enter the Time Duration In Seconds: "))

print("Recording....\n")

record_voice = sounddevice.rec(int(second*fs),samplerate=fs,channels=2)
sounddevice.wait()

write("Out.wav",fs,record_voice)

print("Done.....\n please Check It..")