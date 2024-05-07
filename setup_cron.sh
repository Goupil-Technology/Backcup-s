#!/bin/bash

SCRIPT_PATH="/Backcup-s/script_pour_yunohost.py"

# Vérifier si le script Python est exécutable
if [ ! -x "$SCRIPT_PATH" ]; then
    echo "Erreur : Le script Python n'est pas exécutable."
    echo "Modification des permissions..."
    chmod +x "$SCRIPT_PATH"
fi

# Vérifier les dépendances Python
echo "Vérification des dépendances Python..."
/usr/bin/python3 -c "import datetime" || apt-get install -y python3

# Tâche cron pour exécuter le script toutes les jour à 21 heure
echo "Configuration de la tâche cron..."
(crontab -l ; echo "0 21 * * * /usr/bin/python3 $SCRIPT_PATH") | crontab -

# Redémarrer le service cron
echo "Redémarrage du service cron..."
service cron restart

echo "Configuration terminée."
