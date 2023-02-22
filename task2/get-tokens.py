import re
from sklearn.feature_extraction.text import CountVectorizer
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
            # text = re.sub(r'[^\t\v\r\n\f]\w*\d[^\t\v\r\n\f]*', ' ', text)
            tokenizer = RegexpTokenizer(r'\w+')
            tokens = tokenizer.tokenize(text)
            tokenization = [word for word in tokens
                            if not word in stopwords.words('english')
                            and not word in stopwords.words('russian')
                            and len(word) > 1
                            and x_doesnt_content_number(word)]
            resultset.update(tokenization)
    with open(f'tokens.txt', 'w', encoding='utf-8') as f:
        line = '\n'.join(resultset)
        f.write(line)