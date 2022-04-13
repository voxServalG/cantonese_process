import librosa
from librosa.display import specshow
import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
import os
import sys


def trim_silence(wav, top_db, frame_length, hop_length):
    return librosa.effects.trim(wav, top_db=top_db, frame_length=frame_length, hop_length=hop_length)


INPUT = 'E:\\python_PROJECTS\\cantonese_process\\220411_1835.wav'
OUTPUT = 'E:\\python_PROJECTS\\cantonese_process\\result.wav'
rate = 44100


def get_db(wav, sr):
    S = np.abs(librosa.stft(wav))
    plt.figure()
    plt.subplot(2, 1, 1)
    specshow(S ** 2, sr=sr, y_axis='log')
    plt.colorbar()
    plt.title('Power spectogram')
    plt.subplot(2, 1, 2)
    specshow(librosa.power_to_db(S ** 2, ref=np.max), sr=sr, y_axis='log', x_axis='time')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Log-Power spectogram')
    plt.set_cmap('autumn')
    plt.tight_layout()
    plt.show()
if __name__ == '__main__':
    wav = librosa.core.load(INPUT, sr=44100)[0]
    # get_db(wav, rate)
    result = librosa.effects.trim(wav, top_db=60, frame_length=2048, hop_length=512)[0]
    sf.write(OUTPUT, result, rate, format='wav')
