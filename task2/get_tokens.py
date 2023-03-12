import re
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer, word_tokenize
import string

def x_doesnt_content_number(x):
    for i in range(10):
        if f'{i}' in x:
            return False
    return True
if __name__ == '__main__':
    resultset = set()
    for i in range(100):
        with open(f'doc/{i}_doc.txt', 'r', encoding='utf-8') as f:
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
            russian = [w for w in filter(r.match,tokenization)]
            resultset.update(russian)
            print(i)
    with open(f'tokens.txt', 'w', encoding='utf-8') as f:
        line = '\n'.join(resultset)
        f.write(line)
