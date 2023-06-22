fs = 44100  # Sample rate
seconds = 5  # Duration of recording
volume_outspeaker = 1.0  # Volume of speaker

speaker_ai = 1

LOC_TEMP = '_temp/'
LOC_MYVOICE = LOC_TEMP + 'myvoice.wav'
LOC_VOICE  = LOC_TEMP + 'voice.wav'
LOC_LOG = LOC_TEMP + 'log.txt'

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