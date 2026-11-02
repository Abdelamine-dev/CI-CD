# Inventaire informatique — TP CI/CD

Mini-application Python/Flask avec données fictives, sans base de données.
Elle affiche un inventaire fixe : les modifications se font dans la liste MATERIELS de app.py.
Les noms affichés ne correspondent pas à une découverte réelle du réseau.

## Démarrer sur Ubuntu

Prérequis : Python 3.10 ou supérieur avec le module venv.

```bash
cd inventaire-ci-cd
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```

Ouvrir http://localhost:8000 depuis la machine qui exécute l'application.
Depuis votre PC, utiliser http://IP_DE_LA_VM:8000 si le réseau et le pare-feu autorisent cet accès.
Arrêter avec Ctrl+C. Le serveur Python direct sert au test local ; Docker utilise Gunicorn.

## Routes

| Route | Résultat |
| --- | --- |
| / | Page d'accueil avec liens |
| /materiels | Liste JSON des trois matériels |
| /health | HTTP 200 et état ok |
| /version | APP_VERSION ou 1.0.0 par défaut |

## Exécuter les tests

Dans un terminal avec l'environnement virtuel activé :

```bash
python -m pytest -q
```

Quatre tests : disponibilité, contenu métier, erreur 404 et version configurable.

## Docker (étape ultérieure)

```bash
docker build --build-arg APP_VERSION=1.0.0 -t inventaire:1.0.0 .
docker run -d --name inventaire -p 8080:8000 inventaire:1.0.0
curl -f http://localhost:8080/health
curl -f http://localhost:8080/version
docker logs inventaire
```

## Ajouter les fichiers sur GitHub

1. Extraire l'archive ZIP sur votre ordinateur.
2. Créer un dépôt GitHub nommé inventaire-ci-cd.
3. Choisir « uploading an existing file » ou « Add file > Upload files ».
4. Envoyer le contenu du dossier, y compris tests et les fichiers .gitignore et .dockerignore.
5. Vérifier que app.py et README.md sont à la racine du dépôt, puis valider le commit.

Ne pas envoyer l'archive ZIP seule : GitHub doit contenir les fichiers extraits.
Ne jamais envoyer .venv, .env ou des clés SSH.

## Fiche de choix du TP

- Application : mini-API d'inventaire informatique.
- Besoin : consulter une liste fictive de matériels.
- Modification proposée : ajouter un quatrième matériel (adapter le test d'inventaire).
- Source : renseigner l'URL de votre dépôt GitHub après sa création.
- Lancement local : python app.py ; port interne 8000.
- Validation : /health, contenu de /materiels, route inconnue en 404.
- Identification : /version ; variable APP_VERSION pour le futur commit déployé.

## Suite du TP

Ce dossier fournit l'application, les tests et le Dockerfile. Il ne contient pas encore
le workflow GitHub Actions ni deploy.sh : ils seront construits pendant les étapes
CI/CD du TP, avec les paramètres de votre dépôt et de votre VM.
