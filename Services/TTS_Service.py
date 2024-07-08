import torch
from TTS.api import TTS

device = 'cuda' if torch.cuda.is_available() else 'cpu'

def tts_from_string(string, name = 'test', tts_model = 'tts_models/en/ljspeech/glow-tts'):
    # print(TTS().list_models())
    
    tts = TTS(tts_model).to(device)
    
    print("Generating TTS")
    tts.tts_to_file(text=string, file_path='./Output/Audio/%s.wav'%name)
