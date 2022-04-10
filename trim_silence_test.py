import librosa
def trim_silence(wav, top_db, frame_length, hop_length):
    return librosa.effects.trim(wav, top_db=top_db, frame_length=frame_length, hop_length=hop_length)


if __name__ == '__main__':
    pass
