# import open libraries
from voicevox import Client
import asyncio
import whisper

import sounddevice as sd
from scipy.io.wavfile import write, read

import translators as ts

import keyboard

# import config
from config import *

# UI
from module.UIConsole import *

# Initialize
model = whisper.load_model("base")

# Support functions
async def text2speech(text):
    async with Client() as client:
        audio_query = await client.create_audio_query(
            text, speaker=1
        )
        with open("_temp/voice.wav", "wb") as f:
            f.write(await audio_query.synthesis(speaker=1))

# Main
if __name__ == "__main__":
    while(True):
        try:
            print_ui("header")
            print_ui("tutorial")

            ok = True
            while True:
                if keyboard.is_pressed("t"):
                    break
                if keyboard.is_pressed("q"):
                    print_ui("quit")
                    ok = False
                    break
            if not ok:
                break

            # Record voice
            print_ui("start_recording")
            myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
            sd.wait()  # Wait until recording is finished
            print_ui("end_recording")
            write('_temp/myvoice.wav', fs, myrecording)  # Save as WAV file 

            # Speech to text
            result = model.transcribe("_temp/myvoice.wav", language="en", fp16=False, verbose=True)
            input_text = result['text']
            print_ui("recognized_text")

            # Translate english to japanese
            print_ui("start_translating")
            input_text = ts.translate_text(input_text, "google", from_language="en", to_language="ja")
            with open("_temp/log.txt", "w", encoding='utf-8') as f:
                f.write(input_text)
            print_ui("translated_text", input_text)

            # Text to speech
            asyncio.run(text2speech(input_text))

            # Play voice
            print_ui("start_speaking")
            fs, data = read('_temp/voice.wav')
            voice = sd.play(data, fs)
            sd.wait()  # Wait until file is done playing
            print_ui("end_speaking")

        except:
            print_ui("error")