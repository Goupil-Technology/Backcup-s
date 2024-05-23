# Backcup's
## Projet de script pour backup un serveur YunoHost sur un NAS distant.

L'objectif du script est d'automatiser la création de backup d'un serveur YunoHost vers un serveur NAS distant type Synology. 
Le fichier *Comment utiliser pour sauvegarder sur un serveur distant.md* explique en détail comment l'utiliser.

Stratégie de sauvegarde :
- Les sauvegardes sont conservées sur la semaine (tous les lundi on supprime la sauvegarde du lundi dernier).
- Une sauvegarde est conservé pour chaque semaine (exemple tout les vendredi)
- Une sauvegarde est conservé sur le mois (exemple tout les derniers vendredi du mois)

<img src="https://raw.githubusercontent.com/MrCarambole/Backcup-s/main/logo%20backcup's.png" width="250">

## Comment utiliser pour sauvegarder sur un serveur distant avec une connexion ssh

*sshfs permet de monter un dossier à partir du ssh comme si c'était un disque physique.*

**Etape 1 :** Installation de sshfs sur le serveur :
```
sudo apt-get install sshfs
mkdir /sftp_mount
sshfs user@example.com:/remotedirectory /sftp_mount -p <port> (default 22)
mkdir /sftp_mount/archives
mkdir /sftp_mount/archives/conservation_semaine
mkdir /sftp_mount/archives/conservation_30_jour
```
*Pour permettre le bon fonctionnement du script il est nécessaire de donner des droits hauts (type +777) au fichier mapper sur le NAS (ici /remotedirectory).*

**Etape 2 :** Créer un lien symbolique entre le partage et le fichier de archives de yunohost ceci par exemple :

il faut d'abord supprimer le fichier archives existant !
```
mv /home/yunohost.backup/archives/* /sftp_mount/archives/
rm -rf /home/yunohost.backup/archives
ln -s /sftp_mount/archives /home/yunohost.backup/archives
```

**Etape 3 :** Installation de Backcup's :
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

Sinon pour que ça lance **tous les jours à 21h** on fait :
```
./setup_cron.sh
```

**ATTENTION** il faut que le jour dans last_day.log correspond par exemple si on est mardi le dernier jour théorique c'est lundi donc il faudra qu'il y ait 0 dans le fichier.
