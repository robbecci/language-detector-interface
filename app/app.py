from flask import Flask, request, jsonify, render_template
import joblib
import os

app = Flask(__name__)

# Carichiamo il modello e il vectorizer UNA SOLA VOLTA all'avvio del server,
# non ad ogni richiesta (sarebbe lentissimo)
MODEL_PATH = os.path.join("models", "language_model.joblib")
VECTORIZER_PATH = os.path.join("models", "vectorizer.joblib")

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

# Mappa dei codici lingua verso nomi leggibili, per una risposta più chiara
LANGUAGE_NAMES = {
    "ita": "Italiano",
    "deu": "Tedesco",
    "eng": "Inglese",
    "fra": "Francese",
    "spa": "Spagnolo"
}

@app.route("/")
def home():
    return render_template("index.html")

MIN_RELIABLE_LENGTH = 10  # sotto questa soglia, avvisiamo l'utente

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text", "")

    if not text.strip():
        return jsonify({"error": "Testo vuoto"}), 400

    text_vec = vectorizer.transform([text])
    predicted_code = model.predict(text_vec)[0]
    predicted_name = LANGUAGE_NAMES.get(predicted_code, predicted_code)

    is_short = len(text.strip()) < MIN_RELIABLE_LENGTH

    return jsonify({
        "language_code": predicted_code,
        "language_name": predicted_name,
        "is_short": is_short
    })

if __name__ == "__main__":
    app.run(debug=True)