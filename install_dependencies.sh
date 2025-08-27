#!/bin/bash

echo "Installation des dépendances pour l'application Contrôle Paie..."

# Vérifier si Python3 est installé
if ! command -v python3 &> /dev/null; then
    echo "Python3 n'est pas installé. Installation..."
    sudo apt update
    sudo apt install python3 python3-pip python3-venv -y
fi

# Vérifier si pip3 est installé
if ! command -v pip3 &> /dev/null; then
    echo "pip3 n'est pas installé. Installation..."
    sudo apt update
    sudo apt install python3-pip python3-venv -y
fi

# Créer un environnement virtuel
echo "Création d'un environnement virtuel Python..."
cd "/home/florent/dev/ver 1.07-1"
python3 -m venv venv_controle_paie

# Activer l'environnement virtuel et installer les dépendances
echo "Installation des dépendances Python dans l'environnement virtuel..."
source venv_controle_paie/bin/activate
pip install pandas PyQt5 openpyxl numpy

echo "Installation terminée!"
echo ""
echo "Pour exécuter l'application, utilisez le script run_app.sh ou la commande :"
echo "source '/home/florent/dev/ver 1.07-1/venv_controle_paie/bin/activate' && cd '/home/florent/dev/ver 1.07-1/code source' && python test.py"
