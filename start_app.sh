#!/bin/bash

echo "Lancement direct de l'application Contrôle Paie..."

# Activer l'environnement virtuel
source "/home/florent/dev/ver 1.07-1/venv_controle_paie/bin/activate"

# Aller dans le dossier source et lancer l'application
cd "/home/florent/dev/ver 1.07-1/code source"

# Démarrer l'application en arrière-plan si vous avez un environnement graphique
if [ -n "$DISPLAY" ]; then
    echo "Interface graphique détectée, lancement de l'application..."
    python test.py &
else
    echo "Pas d'interface graphique détectée."
    echo "Pour utiliser l'application, vous avez besoin d'un environnement graphique (X11 ou Wayland)."
    echo "Si vous utilisez SSH, essayez: ssh -X utilisateur@serveur"
fi
