# Image de l'API basée sur une image python
FROM python:3.10-alpine

# Création et positionnement du répertoire par défaut dans le container
WORKDIR /app

# Copie du fichier requirements local (machine hôte) vers le container 
# (répertoire /app, car il s'agit du WORKDIR)
COPY requirements.txt requirements.txt

# Installation des dépendances dans le container
RUN mkdir ./quiz-api \
    && pip install -r requirements.txt

# # Creation d'une base vide
# RUN touch quiz.db

# Variables d'environement de production
ENV FLASK_DEBUG=0
ENV FLASK_ENV=production
ENV FLASK_APP=app.py

# Copie de l'ensemble du code + dépendances
COPY . ./quiz-api/

# Informations sur l'image
LABEL maintainer="Michalski Léon <michalski.leon@edu.esiee.fr>" \
    version="1.0"

EXPOSE 5000
# Commande de démarrage du serveur gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "quiz-api:create_app()", "--log-level", "info", "--error-logfile", "-", "--access-logfile", "-"]