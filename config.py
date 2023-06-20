fs = 44100  # Sample rate
seconds = 5  # Duration of recording

speaker_ai = 1

LOC_MYVOICE = '_temp/myvoice.wav'
LOC_VOICE  = '_temp/voice.wav'
LOC_LOG = '_temp/log.txt'

# {'capybara': 'Sage',
#  'nutria': 'Dragonfly',
#  'chinchilla': 'ChatGPT',
#  'a2_2': 'Claude+',
#  'hutia': 'NeevaAI',
#  'a2': 'Claude-instant',
#  'beaver': 'GPT-4'}
poeModel = "chinchilla"
poeTimeout = 5*60
tokenPoe = [
    'y7hrfI4NCxfHaTia9rtNqA%3D%3D',
    ]