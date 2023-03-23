# Задание:
# Для каждого cкаченного документа из Задания 1:
# Подсчитать tf каждого термина (см. список терминов из Задания 2)
# Подсчитать idf для термина
# Подсчитать tf  для каждой лемматизированной формы (см. список форм  из Задания 2)  как  отношение сумм вхождения числа терминов  к общему количеству терминов в документе
# Подсчитать idf
# Для оценки выполнения задания прислать:
#
# ссылку на рабочую версию кода в репозитории
# Txt файлы  по списком терминов и  подсчитанными  tf-idf. Каждый файл соотвествует одному файлу выкачки и содержит данные в  формате <термин><пробел><idf><пробел><tf-idf><\n>
# Txt файлы  по списком лемматизированных форм  и  подсчитанными tf-idf. Каждый файл соотвествует одному файлу выкачки и содержит данные в  формате <лемма><пробел><idf><пробел><tf-idf><\n>
import math
import re
from collections import Counter

from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer, word_tokenize
import string




def x_doesnt_content_number(x):
    for i in range(10):
        if f'{i}' in x:
            return False
    return True


if __name__ == '__main__':
    main_tokens = {}
    all_doc = 100
    with open(f'tokens.txt', 'r', encoding='utf-8') as f1:
        for line in f1:
            main_tokens[line.split()[0]] = {'idf': 0, 'tf': {i: 0 for i in range(0, all_doc)}}
    for i in range(all_doc):
        with open(f'doc/{i}_doc.txt', 'r', encoding='utf-8') as f:
            simple_tokens = Counter()
            summ = 0
            text = f.read().lower()
            text = re.sub(r'<script[^<]*>*<\/script>', ' ', text)
            text = re.sub(r'<[^>]*>', ' ', text)
            text = text.translate({ord(char): " " for char in string.punctuation})
            tokenizer = RegexpTokenizer(r'\w+')
            tokens = tokenizer.tokenize(text)
            tokenization = [word for word in tokens
                            if not word in stopwords.words('english')
                            and not word in stopwords.words('russian')
                            and len(word) > 2
                            and x_doesnt_content_number(word)]
            r = re.compile("[а-яА-Я]+")
            russian = [w for w in filter(r.match, tokenization)]
            for word in russian:
                simple_tokens[word] += 1
                summ += 1
            for key in simple_tokens.keys():
                if key in main_tokens.keys():
                    main_tokens[key]['idf'] += 1
                    main_tokens[key]['tf'][i] = simple_tokens[key] / summ

    for i in range(100):
        with open(f'tokens/doc{i}_tokens_tdf_idf.txt', 'w', encoding='utf-8') as f:
            for token in main_tokens.keys():
                idf = math.log(all_doc / main_tokens[token]['idf'])
                f.write(f"{token} {idf} {idf * main_tokens[token]['tf'][i]} \n")
