## Commet utiliser pour sauvegarder sur un serveur distant avec une connexion ssh

**sshfs** permet de monter un dossier à partir du ssh comme si c'était un disque physique
```
sudo apt-get install sshfs
mdkir /sftp_mount
sshfs user@example.com:/remote/directory /sftp_mount
```

**Comme la cli de yunohost ne permet pas de choisir le dossier ou backup il faudra créer un lien symbolique entre le pratage et le fichier de archives de yunohosy**

Comme ceci par exemple :
```
cp -R /home/yunohost.backup/archives/. /sftp/archives
rm -Rf /home/yunohost.backup/archives
ln -s /sftp/archives /home/yunohost.backup/archives
```

```
cd /
git clone https://github.com/MrCarambole/Backcup-s.git
chmod +x setup_cron_test.sh
chmod +x setup_cron.sh
```

Pour test si il marche bien on peu lancer le setup_cron_test.sh qui va faire un backup tout les heures
```
./setup_cron.sh
```

Sinon pour pour que ça lance tout les jours à 21 on fait :
```
./setup_cron.sh
```

ATTENTION il faut que le jour dans last_day.log corressponde par exemple si on est mardi le dernier jour thérorique c'est lundi donc il faudra qu'il y ait 0 dans le fichier.
