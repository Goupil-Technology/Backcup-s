## Comment utiliser pour sauvegarder sur un serveur distant avec une connexion ssh

**sshfs** permet de monter un dossier à partir du ssh comme si c'était un disque physique
Sur le serveur :
```
sudo apt-get install sshfs
mkdir /sftp_mount
sshfs user@example.com:/remotedirectory /sftp_mount -p <port> (default 22)
mkdir /sftp_mount/archives
mkdir /sftp_mount/archives/conservation_semaine
mkdir /sftp_mount/archives/conservation_30_jour
```
**Pour permettre le bon fonctionnement du script il est nécessaire de donner des droits hauts (type +777) au fichier mapper sur le NAS (ici /remotedirectory)**

**Comme la cli de yunohost ne permet pas de choisir le dossier ou backup il faudra créer un lien symbolique entre le partage et le fichier de archives de yunohosy**

Comme ceci par exemple :
```
cp -R /home/yunohost.backup/archives/. /sftp_mount/archives
rm -Rf /home/yunohost.backup/archives
ln -s /sftp_mount/archives /home/yunohost.backup/archives
```

```
cd /
git clone https://github.com/MrCarambole/Backcup-s.git
cd /Backcup-s
chmod +x setup_cron_test.sh
chmod +x setup_cron.sh
```

Pour test s'il marche bien on peut lancer le setup_cron_test.sh qui va faire un backup **tout les heures** :
```
./setup_cron.sh
```

Sinon pour que ça lance **tout les jours à 21h** on fait :
```
./setup_cron.sh
```

**ATTENTION** il faut que le jour dans last_day.log correspond par exemple si on est mardi le dernier jour théorique c'est lundi donc il faudra qu'il y ait 0 dans le fichier.
