from collections import Counter

from pymorphy2 import MorphAnalyzer


def get_index():
    index = {}
    with open(f'index.txt', 'r', encoding='utf-8') as f1:
        for line in f1:
            word, counter = eval(line)
            index[word] = counter
        return index


def get_lem_docs(lem: str, index, all_doc, flg_inv):
    if lem in index.keys():
        if flg_inv:
            return all_doc.difference(index[lem].keys())
        else:
            return index[lem].keys()
    else:
        return {}


def search(request: str, index, all_doc):
    morph = MorphAnalyzer()

    result = all_doc
    parts = request.split()
    last_operation = 'and'
    flg_inv = False

    for part in parts:
        if part.lower() in ('and', 'or'):
            last_operation = part.lower()
        elif part.lower() == 'not':
            flg_inv = True
        else:
            lem = morph.normal_forms(part)[0]
            lem_result = get_lem_docs(lem, index, all_doc, flg_inv)
            if last_operation == 'and':
                result = result.intersection(lem_result)
            elif last_operation == 'or':
                result.update(lem_result)
            last_operation = 'and'
    return result


if __name__ == '__main__':
    index = get_index()
    all_doc = set(range(0, 100))
    print("Введите запрос поиска.Для выхода введите:e")
    line = input()
    while line != 'e':
        result = search(line, index, all_doc)
        print(sorted(result))
        line = input()
    print("Хорошего дня!")
