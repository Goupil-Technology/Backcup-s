# Backcup's
## Projet de script pour backup un serveur YunoHost sur un NAS distant.

L'objectif du script est d'automatiser la création de backup d'un serveur YunoHost vers un serveur NAS distant type Synology.
Le fichier *Commet utiliser pour sauvegarder sur un serveur distant.md* explique en détail comment l'utiliser.

Le script de sauvegarde en lui meme (script_de_sauvegarde_theorique.py) est modifiable pour tout usage.

Stratégie de sauvegarde :
- Les sauvegardes sont conservée sur la semaine (tout les lundi on supprime la sauvegarde du lundi dernier).
- Une sauvegarde est conservé pour chaque semaine (exemple tout les vendredi)
- Une sauvegarde est conservé sur le mois (exemple tout les derniers vendredi du mois)

<img src="https://github.com/favicon.ico](https://raw.githubusercontent.com/MrCarambole/Backcup-s/main/logo%20backcup's.png" width="50">
