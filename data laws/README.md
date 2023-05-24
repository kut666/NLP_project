## Steps to collect data

In my part of working with data, I used written sources - the laws of the Republic of Crimea.
Some laws are issued in the Republic of Crimea in three language versions: Russian, Ukrainian and Crimean Tatar
Until 2014, the journal "Collection of normative legal Acts of the Autonomous Republic of Crimea" was published
After 2014, the journal "Vedomosti of the state counsil of the Republic Of Crimea" is published. 
These journals contain a parallel corpus, which I was engaged in.


### Step 0. Download documents from website

- [Until 2014](http://crimea.gov.ru/information/of_izdaniya/sbornik_npa_rk) 97 pdf-files
- [After 2014](http://www.crimea.gov.ru/information/of_izdaniya/vedomosti_gs_rk) 152 pdf-files

### Step 1. Convert documents from PDF to txt-file 
script: 
```
pdf_to_txt.py
```
### Step 2. Studying the structure of the document

- Until 2014 (it has a similar structure to journals published after 2014)
- After 2014 notebook: ```document_structure_part_2.ipynb ```

### Step 3. Creating text-pairs crh-ru from data 

- Until 2014 script: ```pairs_creation_part1.py```
- After 2014 script: ```pairs_creation_part2.py ```

### Step 4. Selecting sentences from the paragraph
script: 
```
clean_corp.py
```
### Step 5. Preprocessing and combining datasets
notebook: 
```
Datasets concatenation.ipynb
```
