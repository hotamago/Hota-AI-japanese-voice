def gptCommands_animegirlvoice(text):
    promt = """translate text "{text}" from vietnamese to japanese the result much follow the rule below:
- no explanation
- only return japanese
- translate it into Japanese with a cute voice like the cat girls in the anime (Always end with "nya")
- no transcription added
- when you finish add @finish to the end of result""".format(text=text)

    return promt