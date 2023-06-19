UIMAP = {
    "header": lambda: """Coded by Hotamago - SonDepZai""",
    "tutorial": lambda: """Press 't' to start recording\nPress 'q' to quit""",
    "start_recording": lambda: "Start recording...",
    "end_recording": lambda: "End recording",
    "recognized_text": lambda: "Recognized text: ",
    "start_translating": lambda: "Start translating...",
    "translated_text": lambda x: "Translated text: {0}".format(x),
    "start_speaking": lambda: "Start speaking...",
    "end_speaking": lambda: "End speaking",
    "line": lambda: "--------------------",
    "error": lambda: "Error, please try again",
    "quit": lambda: "Quiting...",
}

def print_ui(ui_name, *args, **kwargs):
    if(ui_name not in UIMAP):
        print("UI name not found")
        return
    if(ui_name != "line"):
        print(UIMAP["line"]())
    print(UIMAP[ui_name](*args, **kwargs))