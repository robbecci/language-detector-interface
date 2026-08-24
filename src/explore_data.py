import pandas as pd

# Il file sentences.csv di Tatoeba non ha intestazioni (nomi colonna),
# quindi le definiamo noi manualmente, guardando la documentazione Tatoeba
COLUMN_NAMES = ["id", "lang", "text"]

df = pd.read_csv(
    "data/sentences.csv",
    sep="\t",              # Tatoeba usa il tab come separatore, non la virgola
    header=None,           # non c'è una riga di intestazione nel file
    names=COLUMN_NAMES,
    on_bad_lines="skip"    # salta righe malformate invece di far crashare tutto
)

print("Numero totale di frasi nel file:", len(df))
print()

# Le 5 lingue che ci interessano, con i codici usati da Tatoeba
LANGUAGES = ["ita", "deu", "eng", "fra", "spa"]

for lang in LANGUAGES:
    count = len(df[df["lang"] == lang])
    print(f"{lang}: {count} frasi disponibili")

print()
print("Esempio di righe:")
print(df.head())