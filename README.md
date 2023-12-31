# Project Helps to Transform Your Voice into a Waifu or Anime Girl Voice

The "Project helps to transform your voice into a waifu or anime girl voice" is a GitHub project that aims to provide a tool to transform a person's voice into that of a waifu or anime girl. The project is developed using open-source libraries and tools, and it is designed to be accessible to anyone who is interested in changing their voice.

P/S: Project currently only supports Vietnamese input. May support other languages ​​in the future

## Requirement

### voicevox engine

- You need to install voicevox engine
- Move folder "windows-nvidia" to "Hota-AI-japanese-voice" folder and rename to "\_windows-nvidia"

### ffmpeg

- You need to install ffmpeg
- ffmpeg should have envairoment variable

## How to use

### Step 1: Install requirements.txt

```
pip install -r requirements.txt
```

### Step 2: Fix error of voicevox-client package

use command below to find location of voicevox package

```
pip show voicevox-client
```

it will show something like this:

```
Name: voicevox-client
Version: 0.2.0
Summary: Voicevox engine unoffical wrapper
Home-page: https://github.com/voicevox-client/python
Author: tuna2134
Author-email:
License: MIT
Location: **Location of package**
Requires: httpx, typing-extensions
Required-by:
```

Go to location of voicevox-client then find voicevox folder and open it

Copy file fixlibs\speaker_info.py to voicevox folder

### Step 3: Run application

run main.py

```
python main.py
```

## How it Works

The tool uses deep learning algorithms to analyze the user's voice and apply various filters and effects to create the desired voice transformation. Users can choose from a variety of different voice styles, including cute, playful, and energetic, and can adjust the intensity of the transformation to suit their preferences.

## Who Can Use It

The project is intended to be used by anyone who is interested in anime or Japanese culture and wants to experiment with their voice. It could be useful for content creators who want to add a unique touch to their videos or live streams, or for individuals who want to have fun with their friends and family.

## Ongoing Development

The development of this project is ongoing, with regular updates and improvements being made to enhance the tool's functionality and improve the user experience. The project is open-source, meaning that anyone can contribute to its development or use the source code to create their own voice transformation tools.

## Conclusion

If you're interested in changing your voice to that of a waifu or anime girl, the "Project helps to transform your voice into a waifu or anime girl voice" could be just what you're looking for. With its easy-to-use interface and powerful deep learning algorithms, this tool provides a fun and unique way to experiment with your voice.
