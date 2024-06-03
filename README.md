# Backcup's
## Projet de script pour backup un serveur YunoHost sur un NAS distant.

L'objectif du script est d'automatiser la création de backup d'un serveur YunoHost vers un serveur NAS distant type Synology. 

Stratégie de sauvegarde :
- Les sauvegardes sont conservées sur la semaine (tous les lundi on supprime la sauvegarde du lundi dernier).
- Une sauvegarde est conservé pour chaque semaine (exemple tout les vendredi)
- Une sauvegarde est conservé sur le mois (exemple tout les derniers vendredi du mois)

<img src="https://raw.githubusercontent.com/MrCarambole/Backcup-s/main/logo%20backcup's.png" width="250">

## Installation
```
cd / && curl https://raw.githubusercontent.com/MrCarambole/Backcup-s/main/setup.sh>setup.sh && chmod +x setup.sh && ./setup.sh
```

## Desinstallation
```
cd / && curl https://raw.githubusercontent.com/MrCarambole/Backcup-s/main/uninstall.sh>uninstall.sh && chmod +x uninstall.sh && ./uninstall.sh
```
*A lancer en root*

## Comment ça marche ?
Un lien SSHFS est créé entre votre serveur YunoHost et le NAS sur le dossier '/backup.backup'. Afin que YunoHost sauvegarde à cet emplacement, les constantes du script backup.py sont modifiées ainsi que le script app.py pour que les sauvegardes soient affichées dans le panel admin. Une nouvelle entrée est créée dans la crontab pour que le script se lance tous les jours à 21 heures. Chaque semaine, une sauvegarde supplémentaire est réalisée dans '/backup.backup/archives/sauvegarde_semaine' et tous les mois dans '/backup.backup/archives/sauvegarde_mois' (ces sauvegardes ne sont pas affichées dans le panel admin).
