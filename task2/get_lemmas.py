from pymorphy2 import MorphAnalyzer

morph = MorphAnalyzer()
lemmas = {}
with open(f'tokens.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line[:-1]
        lem = morph.normal_forms(line)[0]
        if lemmas.get(lem) is None:
            lemmas[lem] = [line]
        else:
            lemmas.get(lem).append(line)
with open(f'lemmas.txt', 'w', encoding='utf-8') as f:
    for key in lemmas.keys():
        tokens = lemmas[key]
        f.write(f'{key} : {" ".join(tokens)}\n')



