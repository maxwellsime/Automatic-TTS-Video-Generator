import torch
from TTS.api import TTS

device = "cuda" if torch.cuda.is_available() else "cpu"

def tts_from_string(string, name):
    # print(TTS().list_models())

    tts = TTS("tts_models/en/ljspeech/tacotron2-DDC").to(device)

    tts.tts_to_file(text=string, file_path="./Audio/%s.wav"%name)
