"""Mini-API d'inventaire fictif pour le TP CI/CD."""
import os
from flask import Flask, jsonify

app = Flask(__name__)
MATERIELS = [
    {"id": 1, "nom": "PC-ADMIN", "type": "ordinateur"},
    {"id": 2, "nom": "SRV-UBUNTU", "type": "serveur"},
    {"id": 3, "nom": "FW-PFSENSE", "type": "pare-feu"},
]

@app.get("/")
def accueil():
    return """<!doctype html><html lang="fr"><meta charset="utf-8">
    <title>Inventaire informatique</title><h1>Inventaire informatique</h1>
    <p>Application de démonstration du TP CI/CD.</p>
    <ul><li><a href="/materiels">Voir les matériels</a></li>
    <li><a href="/health">État du service</a></li>
    <li><a href="/version">Version</a></li></ul></html>"""

@app.get("/health")
def health():
    return jsonify(status="ok"), 200

@app.get("/version")
def version():
    return jsonify(version=os.environ.get("APP_VERSION", "1.0.0"))

@app.get("/materiels")
def materiels():
    return jsonify(MATERIELS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)
