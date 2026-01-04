# app/model_loader.py

import joblib

# Chemin du modèle
MODEL_PATH = "/var/www/html/PERSO/Projet_NLP/model/svm_tfidf_phishing.pkl"

#sdsdsd

def load_model():
    model, tfidf = joblib.load(MODEL_PATH)
    return model, tfidf
