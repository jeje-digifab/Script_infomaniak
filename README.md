# Script Infomaniak

Script réalisé dans le cadre du test technique pour l’admission en alternance **TSSR** chez Infomaniak.

Ce script interroge les enregistrements DNS de l’URL
[https://candiharvest.infomanihack.ch](https://candiharvest.infomanihack.ch)
afin d’obtenir le header **X-Candidate-Id** nécessaire pour débloquer le Level 1 et accéder au questionnaire de candidature.
Pour cela, il effectue une requête DNS afin d’extraire un enregistrement TXT contenant l’ID, puis injecte cette valeur dans une requête GET HTTP ciblée, permettant ainsi de valider l’étape demandée dans l’évaluation technique.


## Prérequis

- **Python** : 3.11+ (testé avec Python 3.11.2)
- **pip** : 23.0.1 ou plus récent
- Accès Internet pour effectuer les requêtes DNS et HTTP


## Installation & exécution

1. **Cloner le dépôt**
    ```
    git clone https://github.com/jeje-digifab/Script_infomaniak.git
    cd Script_infomaniak
    ```

2. **Installer les dépendances**
    ```
    pip install -r requirements.txt
    ```

3. **Lancer le script**
    ```
    python3 script.py
    ```

## Ressources utilisées

- [Python DNS look-up (GeeksforGeeks)](https://www.geeksforgeeks.org/python/network-programming-in-python-dns-look-up/)
- [User Guide urllib3](https://urllib3.readthedocs.io/en/stable/user-guide.html)
