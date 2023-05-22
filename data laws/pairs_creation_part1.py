import os 
import re
import string

from tqdm.auto import tqdm
from razdel import sentenize

def clean_article(article: list[str]) -> str: 
    text = " ".join(line.strip() for line in article) 
    text = text.lower().replace('- ', '')
    matches = re.findall(r"((?:[а-яА-я]\s){3,}[а-яА-я])", text)
    for match in matches: 
        text = text.replace(match, "".join(match.split()))
    return text 

for filename in tqdm(os.listdir("data/txt/utf-8"), 'File', position=0):
    with open(os.path.join("data/txt/utf-8", filename), 'r', encoding='utf-8', errors='ignore') as document:
        lines = document.readlines()
    line_idxs = {}
    for idx, line in enumerate(lines):
            if 'БИРИНДЖИ БОЛЮК' in line: 
                if 'kir' not in line_idxs:
                    line_idxs['kir'] = [idx]
                else: 
                    line_idxs['kir'].append(idx)
            elif 'РАЗДЕЛ ПЕРВЫЙ' in line or 'Р АЗДЕЛ ПЕРВЫЙ' in line:
                if 'ru' not in line_idxs:
                    line_idxs['ru'] = [idx]
                else: 
                    line_idxs['ru'].append(idx)
            elif 'РОЗДІЛ ПЕРШИЙ' in line:
                if 'ua' not in line_idxs:
                    line_idxs['ua'] = [idx]
                else: 
                    line_idxs['ua'].append(idx)
            elif 'РАЗДЕЛ ВТОРОЙ' in line or 'Р АЗДЕЛ ВТОРОЙ' in line:
                if 'ru_2' not in line_idxs:
                    line_idxs['ru_2'] = [idx]
                else: 
                    line_idxs['ru_2'].append(idx)
    idx_sorted = sorted([max(line_idxs[keys]) for keys in line_idxs])
    if len(idx_sorted) < 4:
        print(f'{filename}: {line_idxs}')
        continue 
    kir_lines = lines[max(line_idxs['kir']):idx_sorted[idx_sorted.index(max(line_idxs['kir']))+1]]
    ru_lines = lines[max(line_idxs['ru']):idx_sorted[idx_sorted.index(max(line_idxs['ru']))+1]]
    kir_idx_list=[]
    for idx, line in enumerate(kir_lines):
        line = line.strip()
        if 'КЪЫРЫМ МУХТАР ДЖУМХУРИЕТИ' == line or 'УКРАИНА КЪАНУНЫ' == line:
            kir_idx_list.append([idx])
        if line.startswith('Къырым Мухтар Джумхуриети Юкъары Радасынынъ Реиси') or line.startswith('Украина Президенти'): 
            if len(kir_idx_list) < 1: 
                continue
            elif len(kir_idx_list[-1]) != 1:
                continue
            else: 
                kir_idx_list[-1].append(idx)
    ru_idx_list=[]
    for idx, line in enumerate(ru_lines): 
        line = line.strip()
        if 'ПОСТАНОВЛЕНИЕ ВЕРХОВНОЙ РАДЫ' == line or 'ЗАКОН УКРАИНЫ' == line:
            ru_idx_list.append([idx])
        if line.startswith('Председатель Верховной Рады Автономной Республики Крым') or line.startswith('Президент Украины'): 
            if len(ru_idx_list) < 1: 
                continue
            elif len(ru_idx_list[-1]) != 1:
                continue
            else: 
                ru_idx_list[-1].append(idx)
    ru_idx_list = [idx for idx in ru_idx_list if len(idx) == 2]
    kir_idx_list = [idx for idx in kir_idx_list if len(idx) == 2]
#     assert len(kir_idx_list) == len(ru_idx_list), f'Unequal numbers of articles in {filename}: {len(kir_idx_list)} != {len(ru_idx_list)}'
    if len(kir_idx_list) != len(ru_idx_list):
        print(f'Unequal numbers of articles in {filename}: {len(kir_idx_list)} != {len(ru_idx_list)}')
        continue
    for [k1, k2], [r1, r2] in zip(kir_idx_list, ru_idx_list):
        kir = clean_article(kir_lines[k1:k2])
        ru = clean_article(ru_lines[r1:r2])
        kir_sent = [sent.strip() for sent in re.split('(?:\d{1,}\.)+', kir)]
        ru_sent = [sent.strip() for sent in re.split('(?:\d{1,}\.)+', ru)]
    #     assert len(kir_sent) == len(ru_sent), f'Unequal numbers of senteces: {len(kir_sent)}!={len(ru_sent)}'
        if len(kir_sent) != len(ru_sent):
            print(f'Unequal numbers of senteces: {len(kir_sent)}!={len(ru_sent)}')
            continue
        with open('output_corp.txt', 'a', encoding="utf-8") as f:
            for s1, s2 in zip(kir_sent, ru_sent):
                f.write(s1 + "\t" + s2 + "\n")
    f.close()