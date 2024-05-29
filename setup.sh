#!/bin/bash
sudo apt-get install sshfs
mkdir /sftp_mount
sshfs Administrateur@192.168.1.2:/home/test_backup_augustin/ /sftp_mount

mkdir /sftp_mount/archives
mkdir /sftp_mount/archives/sauvegarde_semaine
mkdir /sftp_mount/archives/sauvegarde_mois

mv /home/yunohost.backup/archives/* /sftp_mount/archives/
rm -rf /home/yunohost.backup/archives
ln -s /sftp_mount/archives /home/yunohost.backup/archives

mkdir /script_backup
curl "https://raw.githubusercontent.com/MrCarambole/Backcup-s/main/script_v2.py">/script_backup/script.py
echo "0">/script_backup/cycle.log
echo "">/script_backup/backup.log

SCRIPT_PATH="/script_backup/script.py"
(crontab -l ; echo "**/10 * * * * /usr/bin/python3 $SCRIPT_PATH") | crontab -
service cron restart

echo "Configuration terminée."
