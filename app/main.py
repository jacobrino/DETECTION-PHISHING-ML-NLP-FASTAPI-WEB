# app/main.py

from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI
from scipy.sparse import hstack
import numpy as np

from app.schema import EmailRequest, PredictionResponse
from app.preprocessing import preprocess_text, detect_url
from app.model_loader import load_model

print('Lancement uvicorn')

app = FastAPI(title="Phishing Email Detector")


# Autoriser les requêtes depuis localhost: fichiers HTML locaux ou autres ports
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou remplace par ["http://localhost:5500"] ou similaire si tu veux restreindre
    allow_credentials=True,
    allow_methods=["*"],  # ou ["POST"]
    allow_headers=["*"],  # ou ["Content-Type"]
)


# Charger modèle + tfidf
model, tfidf = load_model()

@app.post("/predict", response_model=PredictionResponse)
def predict_email(data: EmailRequest):
    # Fusionner et prétraiter
    text_raw = f"{data.subject} {data.body}"
    print(' text_raw : ',text_raw,'\n' )
    text_clean = preprocess_text(text_raw)
    print(' text_clean : ',text_clean,'\n' )
    has_url = detect_url(text_raw)
    print(' has_url : ',has_url,'\n' )

    # Vectorisation
    X_text = tfidf.transform([text_clean])
    X_url = np.array([[has_url]])
    X_final = hstack([X_text, X_url])

    # Prédiction
    prediction = model.predict(X_final)[0]

    print('Valeur prediction retour ', prediction,'\n')

    return PredictionResponse(
        prediction="phishing" if prediction == 1 else "non_phishing",
        proba=None
        # LinearSVC ne dispose pas un retour sous forme de probabilité soit c'est 1, soit 0
        # Pas comme la régression logistique.
    )

# curl -X POST http://localhost:8000/predict \
#   -H "Content-Type: application/json" \
#   -d '{
#     "subject": "Verify your account",
#     "body": "Your PayPal account has been limited. Please verify your account at http://fake-paypal.com/login."
#   }'
# Commande to test api 

# uvicorn main:app --reload
# To lauch uvicorn local server 