# import open libraries
import poe
from voicevox import Client
import asyncio
import whisper
import time
# import speech_recognition as sr

import sounddevice as sd
from scipy.io.wavfile import write, read

import translators as ts

import keyboard

# import hota library
from constants.gptCommands import *
from module.safeSystem import gptModel

# import config
from config import *

# UI
from module.UIConsole import *

# Initialize
model = whisper.load_model("base")
# r = sr.Recognizer()
gpt = gptModel(poeModel, tokenPoe[0], poeTimeout)

# Support functions
async def text2speech(text):
    async with Client() as client:
        audio_query = await client.create_audio_query(
            text, speaker=speaker_ai
        )
        with open("_temp/voice.wav", "wb") as f:
            f.write(await audio_query.synthesis(speaker=speaker_ai))

# def speech2text():
#     with sr.AudioFile(LOC_MYVOICE) as source:
#         # listen for the data (load audio to memory)
#         audio_data = r.listen(source)
#         # recognize (convert from speech to text)
#         text = r.recognize_google(audio_data, language="vi-VN")
#         return text

# Global variables
menu_activated = False

# Main
if __name__ == "__main__":
    while(True):
        try:
            print_ui("header")
            print_ui("tutorial_begin")

            ok = True
            typeRec = 0
            while True:
                keyPressed = keyboard.read_key()
                if not keyboard.is_pressed(keyPressed):
                    continue

                if menu_activated:
                    if keyPressed == "y":
                        typeRec = 1
                        break
                    if keyPressed == "t":
                        typeRec = 0
                        break
                    if keyPressed == "c":
                        print_ui("enter_text")
                        speaker_ai = int(input())
                        print_ui("output_text", str(speaker_ai))
                        continue
                    if keyPressed == "`":
                        if menu_activated:
                            print_ui("menu_deactivated")
                        menu_activated = False
                        continue
                    if keyPressed == "q":
                        print_ui("quit")
                        ok = False
                        break
                else:
                    if keyPressed == "`":
                        if not menu_activated:
                            print_ui("tutorial_menu")
                            print_ui("menu_activated")
                        menu_activated = True
                        continue
                    if keyPressed == "q":
                        print_ui("quit")
                        ok = False
                        break
            if not ok:
                break

            input_text = ""

            if typeRec == 0:
                # Record voice
                print_ui("start_recording")
                myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
                sd.wait()  # Wait until recording is finished
                print_ui("end_recording")
                write(LOC_MYVOICE, fs, myrecording)  # Save as WAV file 

                # Speech to text

                result = model.transcribe(LOC_MYVOICE, language="vi", fp16=False, verbose=True)
                input_text = result['text']
                # input_text = speech2text() # Use google speech to text
                print_ui("recognized_text", input_text)
            elif typeRec == 1:
                # Record voice
                print_ui("enter_text")
                input_text = input()

            # Translate english to japanese
            # print_ui("start_translating")
            # input_text = ts.translate_text(input_text, "google", from_language="en", to_language="ja")
            # with open(LOC_LOG, "w", encoding='utf-8') as f:
            #     f.write(input_text)
            # print_ui("translated_text", input_text)

            # Translate vietnamese to japanese and make more anime girl voice
            print_ui("start_translating")
            input_text = gpt.send(gptCommands_animegirlvoice(input_text))
            with open(LOC_LOG, "w", encoding='utf-8') as f:
                f.write(input_text)
            print_ui("translated_text", input_text)

            # Text to speech
            asyncio.run(text2speech(input_text))

            # Play voice
            print_ui("start_speaking", 1)
            time.sleep(1)
            fs, data = read(LOC_VOICE)
            voice = sd.play(data, fs)
            sd.wait()  # Wait until file is done playing
            print_ui("end_speaking")

        except:
            print_ui("error")