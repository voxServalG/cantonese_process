import pycantonese  # 将繁体中文转为粤语拼音
import zhconv  # 将简体中文转为繁体中文
import os
import sys
from tqdm import tqdm


def simp_to_jyutping_traversely(str_simp):
    str_trad = zhconv.convert(str_simp, 'zh-hant')

    jyutping_result = []
    for single_character in str_trad:
        jp_trad = pycantonese.characters_to_jyutping(single_character)
        jyutping_result.append(jp_trad[0][1])
    return jyutping_result

def simp2Jyutping(str_simp):
    return simp_to_jyutping_traversely(str_simp)


FILE_NAME = 'text_simp.txt'
OUTPUT_NAME = 'output.txt'

if __name__ == '__main__':
    with open(os.path.join(os.path.dirname(sys.argv[0]), FILE_NAME), 'r', encoding='UTF-8') as data:
        sentences = data.read().splitlines()
    with open(os.path.join(os.path.dirname(sys.argv[0]), OUTPUT_NAME), 'w', encoding='UTF-8') as f:
        for i, sentence in tqdm(enumerate(sentences)):
            print(str(i).zfill(6), *simp2Jyutping(sentence))
            print(str(i).zfill(6), *simp2Jyutping(sentence), file=f)
