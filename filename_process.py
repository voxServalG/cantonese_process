import os
import sys

if __name__ == '__main__':
    index = 1
    path = 'H:\TTS_project\wave_demo'
    filelist = os.listdir(path)
    filelist.sort(key=lambda x: int(x[0:14]))  # sort by 0-13th digit of filename

    for file in filelist:
        old_path = os.path.join(path, file)
        new_path = os.path.join(path, '{}.wav'.format(str(index).zfill(6)))
        os.rename(old_path, new_path)
        index += 1
