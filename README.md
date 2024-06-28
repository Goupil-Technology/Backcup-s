# Backcup's 🥤
## Projet de script pour backup un serveur YunoHost sur un NAS distant.

L'objectif du script est d'automatiser la création de backup d'un serveur YunoHost vers un serveur NAS distant type Synology.

## 🗃️ Stratégie de sauvegarde 
- Les sauvegardes sont conservées sur la semaine (tous les lundis on supprime la sauvegarde du lundi dernier).
- Une copie supplémentaire de la sauvegarde courante est réalisée par défaut à certaines intervalles, on peut le personnaliser via la constante INTERVAL_BACKUP. Elles sont sauvegardées dans sauvegarde_semaine.
- Le dernier jour des intervalles (ici 30), une sauvegarde supplémentaire est également réalisée dans sauvegarde_mois.

<img src="https://raw.githubusercontent.com/Goupil-Technology/Backcup-s/main/logobackcups.png" width="250">

## 📥 Installation
```
cd / && curl https://raw.githubusercontent.com/Goupil-Technology/Backcup-s/main/setup.sh>setup.sh && chmod +x setup.sh && ./setup.sh
```

<img src="https://raw.githubusercontent.com/Goupil-Technology/Backcup-s/main/installation.gif" width="700">

### 🚨 Points d'attention
- Le dossier de sauvegarde donné dans l'étape 3 doit déjà exister : le script ne le créera pas.<br>
- Pour que les sauvegardes soient affichées dans le panel admin, il est nécessaire de faire une sauvegarde manuelle (via le panel admin ou en CLI).

## 🗑️ Desinstallation
```
cd / && curl https://raw.githubusercontent.com/Goupil-Technology/Backcup-s/main/uninstall.sh>uninstall.sh && chmod +x uninstall.sh && ./uninstall.sh
```
*A lancer en root*

## 🏗️ Comment ça marche ?
Le dossier /backup.backup/archives est crée à la racine du serveur yunohost, un lien SSHFS est créé entre ce dossier et le dossier de votre choix sur le NAS distant.

Afin que YunoHost sauvegarde à cet emplacement, les constantes du script backup.py sont modifiées ainsi que le script app.py pour que les sauvegardes soient affichées dans le panel admin.

Une nouvelle entrée est créée dans la crontab pour que le script se lance tous les jours à 21 heures.

Chaque semaine, une sauvegarde supplémentaire est réalisée dans '/backup.backup/archives/sauvegarde_semaine' et tous les mois dans '/backup.backup/archives/sauvegarde_mois'. Actuellement ces fichiers de sauvegardes présents dans sauvegardes_semaine et sauvegardes_mois ne sont pas affichés dans la webadmin. Pour que ce soit le cas, il faudrait modifier en profondeur le fichier backup.py. Nous avons choisi de ne pas le faire pour éviter des problèmes de compatibilité avec des futures mises à jour Yunohost.
