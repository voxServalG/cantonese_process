import pycantonese  # 将繁体中文转为粤语拼音
import zhconv  # 将简体中文转为繁体中文
import os
import sys
from tqdm import tqdm

FILE_NAME = 'train_text_sample.txt'
FILE_TRAD_NAME = 'train_text_sample_trad.txt'
OUTPUT_NAME = 'output.txt'


def transform_from_simp_to_trad(input_txt, output_txt):
    with open(os.path.join(os.path.dirname(sys.argv[0]), input_txt), 'r', encoding='UTF-8') as data:
        sentences = data.read().splitlines()
    with open(os.path.join(os.path.dirname(sys.argv[0]), output_txt), 'w', encoding='UTF-8') as f:
        for sentence in sentences:
            sentence_trad = zhconv.convert(sentence, 'zh-hk')
            print(sentence_trad, file=f)


# ensure string in input_txt are all in TRAD_Chinese!!!
def get_jyutping_of_string(input_txt, output_txt):
    with open(os.path.join(os.path.dirname(sys.argv[0]), input_txt), 'r', encoding='UTF-8') as data:
        sentences = data.read().splitlines()
    with open(os.path.join(os.path.dirname(sys.argv[0]), output_txt), 'w', encoding='UTF-8') as f:
        for i, sentence in tqdm(enumerate(sentences)):
            print(str(i + 1).zfill(6), end=' ', file=f)
            result_jp = pycantonese.characters_to_jyutping(sentence)
            # result_jp: a list of tuples like <word, jyutping>
            # jp_tuple: each item in result_jp, is a tuple
            # jp[1] and single_jp: a single jyutping in jp_tuple
            for jp_tuple in result_jp:
                single_jp = jp_tuple[1]
                char_printed = 0
                for split_char in single_jp:
                    print(split_char, end='', file=f)
                    char_printed += 1
                    if split_char.isdigit():
                        if jp_tuple is result_jp[-1] and char_printed is len(single_jp):
                            pass
                        # pass does nothing in Python
                        else:
                            print(' ', end='', file=f)
                if jp_tuple is result_jp[-1]:
                    print('\n', end='', file=f)


if __name__ == '__main__':
    transform_from_simp_to_trad(FILE_NAME, FILE_TRAD_NAME)
    get_jyutping_of_string(FILE_TRAD_NAME, OUTPUT_NAME)
