# 🌍 Language Detector

Applicazione web che rileva automaticamente la lingua di un testo tra **Italiano, Tedesco, 
Inglese, Francese e Spagnolo**, usando un modello di Machine Learning allenato da zero.

Progetto realizzato come lavoro di portfolio nell'ambito di un corso di AI Development.

## Come funziona

L'utente scrive un testo in una casella di input; in modo dinamico (senza bisogno di premere 
un bottone), l'app mostra la lingua rilevata con relativa bandiera.

## Stack tecnologico

- **Python** — linguaggio principale
- **pandas** — pulizia e gestione dei dati
- **scikit-learn** — feature extraction (TF-IDF su n-grammi di caratteri) e modello di 
  classificazione (Naive Bayes)
- **Flask** — backend e API
- **HTML / CSS / JavaScript** — interfaccia utente

## Risultati del modello

Accuracy sul test set: **99.07%**, con precision/recall/F1-score uniformi tra il 98% e il 100% 
su tutte e 5 le lingue.

## Come avviarlo

Istruzioni complete nel documento `Language_Detector_Guida_Configurazione.pdf` incluso nella 
repository. In breve:

\`\`\`bash
pip install -r requirements.txt
python src/download_data.py
python src/clean_data.py
python src/train_model.py
python app/app.py
\`\`\`

Poi apri il browser su `http://127.0.0.1:5000`.

## Documentazione

- 📄 `Language_Detector_Documentazione_Tecnica.pdf` — scelte tecniche, architettura, 
  spiegazione di ogni script, limiti noti e sviluppi futuri
- 📄 `Language_Detector_Guida_Configurazione.pdf` — istruzioni dettagliate di installazione 
  ed esecuzione

## Limiti noti

- Su testi molto brevi (poche lettere) l'affidabilità è ridotta, per la scarsità di 
  informazione statistica disponibile — l'app avvisa l'utente quando questo accade
- Il sistema classifica sempre il testo come una delle 5 lingue supportate, anche se il testo 
  inserito è in una lingua diversa