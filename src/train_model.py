import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Carichiamo il dataset pulito
df = pd.read_csv("data/dataset_clean.csv")

X = df["text"]      # input: il testo
y = df["lang"]       # output: l'etichetta della lingua

# Dividiamo in training set (80%) e test set (20%)
# stratify=y assicura che la proporzione tra le 5 lingue resti uguale
# sia nel train che nel test set
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print("Frasi di training:", len(X_train))
print("Frasi di test:", len(X_test))

# Trasformiamo il testo in numeri usando n-grammi di caratteri (da 1 a 3 caratteri)
vectorizer = TfidfVectorizer(analyzer="char", ngram_range=(1, 3))
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Alleniamo un modello Naive Bayes (semplice, veloce, funziona bene per il testo)
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Valutiamo il modello sul test set (dati mai visti durante il training)
y_pred = model.predict(X_test_vec)
accuracy = accuracy_score(y_test, y_pred)

print()
print(f"Accuracy sul test set: {accuracy:.2%}")
print()
print("Report dettagliato per lingua:")
print(classification_report(y_test, y_pred))

import joblib

# Salviamo il modello allenato e il vectorizer, ci serviranno nel backend Flask
joblib.dump(model, "models/language_model.joblib")
joblib.dump(vectorizer, "models/vectorizer.joblib")

print()
print("Modello e vectorizer salvati nella cartella models/")