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
