# TP_1_Backend_Django Système d'event booking (Django)

Une application web Django pour gérer des événements et permettre aux utilisateurs de réserver des places.

## Prérequis

- Python 3.11 ou plus
- pip (gestionnaire de paquets Python)
- Virtualenv (recommandé)
- Git (pour cloner le projet)

## Pour l'installation

1. **Cloner le dépôt**

git clone https://github.com/Mechac-2004/TP_1_Backend_Django.git
cd mon-projet

2. **créer une marchine virtuel**

créer une marchine virtuel avec 

python -m venv env

3. **Activer la marchine**

Sous Windows activer la marchine

env\Scripts\activate

Sous linux /MacOs

source env/bin/activate

4. **Installer les dépendances**

pip install -r requirement.txt

5. **Les Migrations**

Faite les migrations

python manage.py makemigrations

python manage.py migrate

6 **Démarrage du projet**

Et en fin démarrer le projet avec 

python manage.py runserver  
