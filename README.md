# Machine translation (from Russian language to Crimean Tatar language and vice versa)

The project report contains a description of a model's for machine translation from Crimean Tatar to Russian built with neural machine learning techniques. Collected and published first dataset for parallel corpus [crh] - [ru].


## Report 
Ypu can read project report [here](https://github.com/kut666/NLP_project/report.pdf)


## Contributors 
**Orkhan Makhmudov**: collected data from phrasebook A.G. Goryanov, visualized comparison of models and word embedings.
**Denis Tsybrik**: collected data from laws, learned and validated GRU, GRU+Attention, LSTM+Attention -based models.
**Korzh Bogdan**: rewrote the transliterator from latin to cyrillic, build a parser to collect more than 8000 translation pairs from news sites. Some of those websites were not translated to Russian, but had Ukrainian translation instead, so Yandex Cloud API was used to translate targets to Russian, a total of 2 million characters, learned and validated Transormer+Attention -based models.


## Results

|Model | 10 epochs | 20 epochs | 25 epochs |
|-----------|---------|---------|---------|
|GRU | 34.00 | - | - |
|GRU + Attention | 35.16 | 39.98 | - |
|LSTM + Attention | 28.39 | - | - |
| Transformers + Attention | - | - | 51.83 |

## Sample outputs

**Transformers + attention **

**[crh]:** бу иляджны насыл ичмели

**[ru_original]:** как принимать это лекарство

**[ru_original]:** как это лекарство пить

---

**[crh]:** бугунь акъшам мешгъульсинъизми

**[ru_original]:** вы не заняты сегодня вечером

**[ru_original]:** сегодня вечером сегодня вечером
