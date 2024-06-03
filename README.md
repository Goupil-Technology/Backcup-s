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
