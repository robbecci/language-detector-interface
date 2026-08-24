import pandas as pd

COLUMN_NAMES = ["id", "lang", "text"]
LANGUAGES = ["ita", "deu", "eng", "fra", "spa"]
SENTENCES_PER_LANG = 3000
MIN_LENGTH = 2   # caratteri minimi
MAX_LENGTH = 100  # caratteri massimi

df = pd.read_csv(
    "data/sentences.csv",
    sep="\t",
    header=None,
    names=COLUMN_NAMES,
    on_bad_lines="skip"
)

# Teniamo solo le lingue che ci servono
df = df[df["lang"].isin(LANGUAGES)]

# Rimuoviamo righe con testo mancante
df = df.dropna(subset=["text"])

# Rimuoviamo duplicati esatti
df = df.drop_duplicates(subset=["text"])

# Filtriamo per lunghezza del testo (numero di caratteri)
df["length"] = df["text"].str.len()
df = df[(df["length"] >= MIN_LENGTH) & (df["length"] <= MAX_LENGTH)]

# Per ogni lingua, prendiamo un campione casuale di SENTENCES_PER_LANG frasi
samples = []
for lang in LANGUAGES:
    lang_df = df[df["lang"] == lang]
    sample = lang_df.sample(n=SENTENCES_PER_LANG, random_state=42)
    samples.append(sample)
    print(f"{lang}: selezionate {len(sample)} frasi")

# Uniamo tutti i campioni in un unico dataset
final_df = pd.concat(samples)

# Mescoliamo le righe (altrimenti sarebbero ordinate per lingua)
final_df = final_df.sample(frac=1, random_state=42).reset_index(drop=True)

# Teniamo solo le colonne che ci servono davvero
final_df = final_df[["lang", "text"]]

# Salviamo il dataset pulito
final_df.to_csv("data/dataset_clean.csv", index=False)
print()
print("Dataset pulito salvato in data/dataset_clean.csv")
print("Totale frasi:", len(final_df))