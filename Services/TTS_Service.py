import torch
from TTS.api import TTS

device = 'cuda' if torch.cuda.is_available() else 'cpu'

def tts_from_string(string, name = 'test', tts_model = 'tts_models/en/ljspeech/glow-tts'):
    # print(TTS().list_models())
    
    tts = TTS(tts_model).to(device)
    
    print("Generating TTS")
    tts.tts_to_file(text=string, file_path='./Output/Audio/Temp/%s.wav'%name)

#tts_from_string('Another')
#tts_from_string('Another', 'test-speedy', 'tts_models/en/ljspeech/speedy-speech')
#tts_from_string('Another', 'test-vits', 'tts_models/en/ljspeech/vits')
#tts_from_string('Another', 'test-vits-neon', 'tts_models/en/ljspeech/vits--neon')
#tts_from_string('Another', 'test-fast-pitch', 'tts_models/en/ljspeech/fast_pitch')
#tts_from_string('Another', 'test-overflow', 'tts_models/en/ljspeech/overflow')
