#!/bin/bash
echo "Installation du script de sauvegarde 🔨"

echo "[1/7] Installation de sshfs"
sudo apt-get install sshfs

echo "[2/7] Creation du nouveau dossier de backup"
mkdir /backup.backup

echo "[3/7] Connexion du nouveau dossier de backup au NAS distant"
sshfs Administrateur@176.170.224.110:/GoupilTechnology/backup_script_v2 /backup.backup -p 7568

echo "[4/7] Creation de dossier nécessaire au fonctionnement du script"
mkdir /backup.backup/archives
mkdir /backup.backup/archives/sauvegarde_semaine
mkdir /backup.backup/archives/sauvegarde_mois

echo "[5/7] Telechargement du script"
mkdir /script_backup
curl "https://raw.githubusercontent.com/MrCarambole/Backcup-s/main/script_v3.py">/script_backup/script.py
echo "0">/script_backup/cycle.log

echo "[6/7] Modification de l'application YunoHost"
sed -i 's/\/home\/yunohost\.backup/\/backup\.backup/g' /usr/lib/python3/dist-packages/yunohost/backup.py
sed -i 's/yunohost\.backup/backup\.backup/' /usr/lib/python3/dist-packages/yunohost/app.py

echo "[7/7] Gestion de la crontab"
(crontab -l ; echo "0 21 * * * /usr/bin/python3 /script_backup/script.py") | crontab -
service cron restart

echo "Le script de sauvegarde est installé 🐸"
