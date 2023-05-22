from razdel import sentenize

filename = "data/output/output_1.txt"
filename_clean = "data/output/output_clean_1.txt"
with open(filename, "r", encoding="utf-8", errors="ignore") as document_to_read, \
open(filename_clean, "a", encoding="utf-8") as document_to_write:
    lines = document_to_read.readlines()
    for line in lines:
        [kir, ru] = line.split("\t")
        kir = kir.strip()
        ru = ru.strip()
        kir_sentences = list(sentenize(kir))
        ru_sentences = list(sentenize(ru))
        if len(kir_sentences) == len(ru_sentences) and len(kir_sentences) > 1:
            for s1, s2 in zip(kir_sentences, ru_sentences):
                document_to_write.write(s1.text + "\t" + s2.text + "\n")
#                 print(s1.text, s2.text)
        else:
            document_to_write.write(kir + "\t" + ru + "\n")
document_to_read.close()
document_to_write.close()