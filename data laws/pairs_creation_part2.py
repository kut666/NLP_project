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

for filename in tqdm(os.listdir("data/txt_2"), 'File', position=0):
    with open(os.path.join("data/txt_2", filename), 'r', encoding='utf-8', errors='ignore') as document:
        lines = document.readlines()
    line_idxs_section2 = {}
    line_idxs_section3 = {'end':[len(lines)-1]}
    for idx, line in enumerate(lines):
        if line.startswith(('ЭКИНДЖИ БОЛЮК', 'Э КИНДЖИ БОЛЮК', ' Э КИНДЖИ БОЛЮК')): 
            if 'crh' not in line_idxs_section2:
                line_idxs_section2['crh'] = [idx]
            else: 
                line_idxs_section2['crh'].append(idx)
        elif line.startswith(('РАЗДЕЛ ВТОРОЙ', 'Р АЗДЕЛ ВТОРОЙ', ' Р АЗДЕЛ ВТОРОЙ')):
            if 'ru' not in line_idxs_section2:
                line_idxs_section2['ru'] = [idx]
            else: 
                line_idxs_section2['ru'].append(idx)
        elif line.startswith(('РОЗДІЛ ДРУГИЙ', 'Р ОЗДІЛ ДРУГИЙ', ' Р ОЗДІЛ ДРУГИЙ')):
            if 'ua' not in line_idxs_section2:
                line_idxs_section2['ua'] = [idx]
            else: 
                line_idxs_section2['ua'].append(idx)
        elif line.startswith(('РАЗДЕЛ ТРЕТИЙ', 'Р АЗДЕЛ ТРЕТИЙ', ' Р АЗДЕЛ ТРЕТИЙ')):
            if 'ru_3' not in line_idxs_section2:
                line_idxs_section2['ru_3'] = [idx]
            else: 
                line_idxs_section2['ru_3'].append(idx)
            if 'ru' not in line_idxs_section3: 
                line_idxs_section3['ru'] = [idx]
            else: 
                line_idxs_section3['ru'].append(idx)
        elif line.startswith(('РОЗДІЛ ТРЕТІЙ', 'Р ОЗДІЛ ТРЕТІЙ', ' Р ОЗДІЛ ТРЕТІЙ')):
            if 'ua' not in line_idxs_section3:
                line_idxs_section3['ua'] = [idx]
            else: 
                line_idxs_section3['ua'].append(idx)
        elif line.startswith(('УЧЮНДЖИ БОЛЮК', 'У ЧЮНДЖИ БОЛЮК', ' У ЧЮНДЖИ БОЛЮК')): 
            if 'crh' not in line_idxs_section3:
                line_idxs_section3['crh'] = [idx]
            else: 
                line_idxs_section3['crh'].append(idx)
                
    idx_section2_sorted = sorted([max(line_idxs_section2[keys]) for keys in line_idxs_section2])
    idx_section3_sorted = sorted([max(line_idxs_section3[keys]) for keys in line_idxs_section3])
    
    if len(idx_section2_sorted) < 4 or len(idx_section3_sorted) < 4:
        print(f'{filename}: {line_idxs_section2}, {line_idxs_section3}')
        continue 
        
    crh_lines_section2 = lines[max(line_idxs_section2['crh']):idx_section2_sorted[idx_section2_sorted.index(max(line_idxs_section2['crh']))+1]]
    ru_lines_section2 = lines[max(line_idxs_section2['ru']):idx_section2_sorted[idx_section2_sorted.index(max(line_idxs_section2['ru']))+1]]
    
    crh_lines_section3 = lines[max(line_idxs_section3['crh']):idx_section3_sorted[idx_section3_sorted.index(max(line_idxs_section3['crh']))+1]]
    ru_lines_section3 = lines[max(line_idxs_section3['ru']):idx_section3_sorted[idx_section3_sorted.index(max(line_idxs_section3['ru']))+1]]

    crh_idx_list_section2=[]
    for idx, line in enumerate(crh_lines_section2):
        line = line.strip()
        if 'КЪЫРЫМ ДЖУМХУРИЕТИ' == line:
            crh_idx_list_section2.append([idx])
        if line.startswith('Къырым Джумхуриети Девлет Шурасынынъ Реиси'): 
            if len(crh_idx_list_section2) < 1: 
                continue
            elif len(crh_idx_list_section2[-1]) != 1:
                continue
            else: 
                crh_idx_list_section2[-1].append(idx)
    ru_idx_list_section2=[]
    for idx, line in enumerate(ru_lines_section2): 
        line = line.strip()
        if 'ПОСТАНОВЛЕНИЕ' == line:
            ru_idx_list_section2.append([idx])
        if line.startswith('Председатель Государственного Совета Республики Крым'): 
            if len(ru_idx_list_section2) < 1: 
                continue
            elif len(ru_idx_list_section2[-1]) != 1:
                continue
            else: 
                ru_idx_list_section2[-1].append(idx)
                
    crh_idx_list_section3=[]
    for idx, line in enumerate(crh_lines_section3):
        line = line.strip()
        if 'КЪЫРЫМ ДЖУМХУРИЕТИ' == line:
            crh_idx_list_section3.append([idx])
        if line.startswith('Къырым Джумхуриети Девлет Шурасынынъ Реиси'): 
            if len(crh_idx_list_section3) < 1: 
                continue
            elif len(crh_idx_list_section3[-1]) != 1:
                continue
            else: 
                crh_idx_list_section3[-1].append(idx)
                
    ru_idx_list_section3=[]
    for idx, line in enumerate(ru_lines_section3): 
        line = line.strip()
        if 'ПОСТАНОВЛЕНИЕ ПРЕЗИДИУМА' == line:
            ru_idx_list_section3.append([idx])
        if line.startswith('Председатель Государственного Совета Республики Крым'): 
            if len(ru_idx_list_section3) < 1: 
                continue
            elif len(ru_idx_list_section3[-1]) != 1:
                continue
            else: 
                ru_idx_list_section3[-1].append(idx)
    
    ru_idx_list_section2 = [idx for idx in ru_idx_list_section2 if len(idx) == 2]
    crh_idx_list_section2 = [idx for idx in crh_idx_list_section2 if len(idx) == 2]
    ru_idx_list_section3 = [idx for idx in ru_idx_list_section3 if len(idx) == 2]
    crh_idx_list_section3 = [idx for idx in crh_idx_list_section3 if len(idx) == 2]
    
#     assert len(kir_idx_list) == len(ru_idx_list), f'Unequal numbers of articles in {filename}: {len(kir_idx_list)} != {len(ru_idx_list)}'
    if len(crh_idx_list_section2) != len(ru_idx_list_section2):
        print(f'Unequal numbers of articles in {filename}: {len(ru_idx_list_section2)} != {len(crh_idx_list_section2)}')
        continue
    for [c1, c2], [r1, r2] in zip(crh_idx_list_section2, ru_idx_list_section2):
        crh = clean_article(crh_lines_section2[c1:c2])
        ru = clean_article(ru_lines_section2[r1:r2])
        crh_sent = [sent.strip() for sent in re.split('(?:\d{1,}\.)+', crh)]
        ru_sent = [sent.strip() for sent in re.split('(?:\d{1,}\.)+', ru)]
    #     assert len(kir_sent) == len(ru_sent), f'Unequal numbers of senteces: {len(kir_sent)}!={len(ru_sent)}'
        if len(crh_sent) != len(ru_sent):
            print(f'Unequal numbers of senteces: {len(crh_sent)}!={len(ru_sent)}')
            continue
        with open('data/output/output_corp_2.txt', 'a', encoding="utf-8") as f:
            for s1, s2 in zip(crh_sent, ru_sent):
                f.write(s1 + "\t" + s2 + "\n")
    f.close()
    
    #     assert len(kir_idx_list) == len(ru_idx_list), f'Unequal numbers of articles in {filename}: {len(kir_idx_list)} != {len(ru_idx_list)}'
    if len(crh_idx_list_section3) != len(ru_idx_list_section3):
        print(f'Unequal numbers of articles in {filename}: {len(ru_idx_list_section3)} != {len(crh_idx_list_section3)}')
        continue
    for [c1, c2], [r1, r2] in zip(crh_idx_list_section3, ru_idx_list_section3):
        crh = clean_article(crh_lines_section3[c1:c2])
        ru = clean_article(ru_lines_section3[r1:r2])
        crh_sent = [sent.strip() for sent in re.split('(?:\d{1,}\.)+', crh)]
        ru_sent = [sent.strip() for sent in re.split('(?:\d{1,}\.)+', ru)]
    #     assert len(kir_sent) == len(ru_sent), f'Unequal numbers of senteces: {len(kir_sent)}!={len(ru_sent)}'
        if len(crh_sent) != len(ru_sent):
            print(f'Unequal numbers of senteces: {len(crh_sent)}!={len(ru_sent)}')
            continue
        with open('data/output/output_2.txt', 'a', encoding="utf-8") as f:
            for s1, s3 in zip(crh_sent, ru_sent):
                f.write(s1 + "\t" + s2 + "\n")
    f.close()
    