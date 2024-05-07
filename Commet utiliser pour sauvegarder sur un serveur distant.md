## Commet utiliser pour sauvegarder sur un serveur distant avec une connexion ssh

**sshfs** permet de monter un dossier à partir du ssh comme si c'était un disque physique
```
sudo apt-get install sshfs
mdkir /sftp_mount
sshfs user@example.com:/remote/directory /sftp_mount
```

**Comme la cli de yunohost ne permet pas de choisir le dossier ou backup il faudra modifier le script qui permet de faire la backup : yunohost/src/backup.py**

source du script : /usr/lib/python3/dist-packages/yunohost/backup.py

Comme ceci par exemple :
```
81 BACKUP_PATH = "/home/yunohost.backup"
```
```
81 BACKUP_PATH = "~/sftp_mount"
```

Il faudra aussi modifier les chemins dans le script
