# Détection de Phishing par NLP (SVM + TF‑IDF) — API FastAPI

Ce projet propose une approche **NLP** pour détecter des emails/messages de **phishing** à partir de leur contenu textuel.
Le pipeline inclut la **fusion de plusieurs datasets**, le **prétraitement**, l’extraction de features via **TF‑IDF**, l’entraînement d’un classifieur **SVM**, puis le déploiement du modèle via une **API FastAPI**.
Ce projet a été dévéloppé en Juin 2025 mais publié en Décembre 2025 dans un cadre de mise à jour d'un Portfolio personnel.
---

## Fonctionnalités


- `index.html` : page web simple permettant d’analyser un texte (phishing / non phishing) en **appelant l’API FastAPI**.
- Fusion de plusieurs jeux de données en un dataset unique : `dataset_merged.csv`
- Prétraitement du texte (nettoyage, normalisation, tokenization, stopwords, etc.)
- Vectorisation **TF‑IDF**
- Modèle **SVM** entraîné et sauvegardé (`.pkl`)
- API **FastAPI** pour faire des prédictions

---

## Structure du dépôt

```bash
Projet_NLP/
├── app/
│   ├── main.py               # API FastAPI
│   ├── preprocessing.py      # fonctions de prétraitement réutilisables
│   ├── model_loader.py       # chargement du modèle et du vectorizer
│   ├── schema.py             # schémas Pydantic
│   └── index.html          # page web (frontend) qui appelle l’API
├── data/
│   ├── dataset_merged.csv    # dataset fusionné
│   └── ntlk_data/            # ressources NLTK
├── model/
│   └── svm_tfidf_phishing.pkl
├── notebooks/
│   └── NLP_phishing_Analyse_des_datasets,_prétraitement,_conception_et_entrainement_modèle,_test_avec_fast_api_.ipynb    # analyse, fusion datasets, prétraitement, entraînement
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Datasets utilisés & fusion

Le dataset final **`dataset_merged.csv`** a été construit en fusionnant les sources suivantes dont le lien est https://www.kaggle.com/datasets/naserabdullahalam/phishing-email-dataset/data:


- `CEAS_08.csv`
- `Enron.csv`
- `Ling.csv`
- `Nazario.csv`
- `Nigerian_Fraud.csv`
- `SpamAssasin.csv`
- `phishing_email.csv`
Le fichier dataset_merged.csv est accessible via le lien "https://drive.google.com/file/d/10Tikyb0kRy4FFp4syaRldYg-u3lHYBNZ/view?usp=sharing"

Dans le notebook, ces fichiers étaient chargés depuis Google Drive (exemple) :

```python
file_path_1 = '/content/drive/MyDrive/ColabNotebooks/Projet_NLP/Phishing Email Dataset/Original/CEAS_08.csv'
file_path_2 = '/content/drive/MyDrive/ColabNotebooks/Projet_NLP/Phishing Email Dataset/Original/Enron.csv'
file_path_3 = '/content/drive/MyDrive/ColabNotebooks/Projet_NLP/Phishing Email Dataset/Original/Ling.csv'
file_path_4 = '/content/drive/MyDrive/ColabNotebooks/Projet_NLP/Phishing Email Dataset/Original/Nazario.csv'
file_path_5 = '/content/drive/MyDrive/ColabNotebooks/Projet_NLP/Phishing Email Dataset/Original/Nigerian_Fraud.csv'
file_path_6 = '/content/drive/MyDrive/ColabNotebooks/Projet_NLP/Phishing Email Dataset/Original/SpamAssasin.csv'
file_path_7 = '/content/drive/MyDrive/ColabNotebooks/Projet_NLP/Phishing Email Dataset/Original/phishing_email.csv'
```

---

## Installation

### 1) Cloner le dépôt

```bash
git clone https://github.com/<TON_USER>/<TON_REPO>.git
cd Projet_NLP
```

### 2) Créer un environnement virtuel

```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
# venv\Scripts\activate       # Windows
```

### 3) Installer les dépendances

```bash
pip install -r requirements.txt
```

> ℹ️ Les ressources NLTK sont déjà présentes dans `data/ntlk_data/` (versionnées), donc aucun téléchargement n’est nécessaire.

---

## Utilisation

### 1) Lancer l’API FastAPI

Depuis la racine du projet :

```bash
uvicorn app.main:app --reload
```

Puis ouvrir :

- Swagger UI : http://127.0.0.1:8000/docs  
- Redoc : http://127.0.0.1:8000/redoc  

### 2) Exemple de requête

> Adaptez l’endpoint si votre `main.py` utilise un chemin différent.

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{ 
    "subject": "Important: Verify your account now", 
    "body": "Your account has been suspended. Click here to verify your information immediately." 
  }'

```

Exemple de réponse (indicatif) :

```json
{
  "label": "phishing",
  "proba": null
}
```

---

## Entraînement / Notebook

Le notebook `notebooks/NLP_phishing.ipynb` contient :

- l’exploration des datasets
- la fusion des datasets
- le prétraitement
- l’entraînement du modèle (SVM + TF‑IDF)
- la sauvegarde du modèle (`.pkl`)

Pour reproduire l’entraînement :

1. ouvrez le notebook
2. adaptez les chemins des datasets
3. exécutez toutes les cellules

---

## Modèle

Le modèle entraîné est stocké dans :

- `model/svm_tfidf_phishing.pkl`

Le chargement est géré par `app/model_loader.py`.

---

## Remarques importantes

- `data/ntlk_data/` peut être **très volumineux** : si GitHub refuse le push, utilisez **Git LFS** ou retirez ce dossier.
- Si le fichier `.pkl` devient trop gros, il est conseillé de le publier via **GitHub Releases** ou **Git LFS**.

---

## Auteur

**ANDRIANJARA Jacob Rino**  
Projet : Détection de phishing par NLP — FastAPI / SVM / TF‑IDF
