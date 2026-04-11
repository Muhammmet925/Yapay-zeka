import spacy

nlp_nesnesi = spacy.load("en_core_web_sm")

# metin = nlp_nesnesi("Dr. Strange loves pav bhaji of mumbai. Hulk loves chaat of delhi")
metin = nlp_nesnesi("Bu gün hava çok güzel. Dışarı çıkıp gezmek istedim.")

print("\n\nCümleler")
for cumleler in metin.sents:
    print(cumleler)

print("\n\nKelimeler")
for cumleler in metin.sents:
    for kelime in cumleler:
        print(kelime)