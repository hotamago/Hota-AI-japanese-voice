UIMAP = {
    "header": lambda: """Coded by Hotamago - SonDepZai""",
    "tutorial_begin": lambda: """Press '`' to open menu""",
    "tutorial_menu": lambda: """Press 'y' to enter text\nPress 't' to start recording\nPress 'd' to change speaker_device\nPress 'c' to change speaker ai\nPress 'r' to repeat last voice\nPress 'q' to quit""",
    "menu_activated": lambda: """Menu was activated""",
    "menu_deactivated": lambda: """Menu was deactivated""",
    "start_recording": lambda: "Start recording...",
    "end_recording": lambda: "End recording",
    "recognized_text": lambda x: "Recognized text: {0}".format(x),
    "enter_text": lambda: """Enter text: """,
    "output_text": lambda x: "Output text: {0}".format(x),
    "start_translating": lambda: "Start translating...",
    "translated_text": lambda x: "Translated text: {0}".format(x),
    "start_speaking": lambda x: "Start speaking after ({0})...".format(x),
    "end_speaking": lambda: "End speaking",
    "list_devices": lambda x: "List devices: {0}".format(x),
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