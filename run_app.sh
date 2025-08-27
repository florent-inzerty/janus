#!/bin/bash

echo "Lancement de l'application Contrôle Paie..."

# Vérifier si l'environnement virtuel existe
if [ ! -d "/home/florent/dev/ver 1.07-1/venv_controle_paie" ]; then
    echo "L'environnement virtuel n'existe pas. Exécution du script d'installation..."
    ./install_dependencies.sh
fi

# Activer l'environnement virtuel
source "/home/florent/dev/ver 1.07-1/venv_controle_paie/bin/activate"

# Vérifier si les dépendances sont installées dans l'environnement virtuel
if ! python -c "import pandas, PyQt5, openpyxl, numpy" 2>/dev/null; then
    echo "Certaines dépendances manquent dans l'environnement virtuel. Réinstallation..."
    pip install pandas PyQt5 openpyxl numpy
fi

# Aller dans le dossier source et lancer l'application
cd "/home/florent/dev/ver 1.07-1/code source"
python test.py
