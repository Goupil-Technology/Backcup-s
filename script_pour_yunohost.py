import datetime
import os
import shutil

def gestion_backup_semaine():
    """
    Récupère le dernier jour sauvegardé dans les logs last_day.log,
    Vérifie si c'est le dernier jour de la semaine,
    Si oui il sauvegarde le vendredi à partir de la fonction conserver_sauvegarde_de_la_semaine.
    """
     with open("/Backcup-s/last_day.log", 'r') as last_day:
        contenu = last_day.readlines()
        numero_de_jour = int(contenu[0]) + 1
        if numero_de_jour >= len(liste_jours_semaine):
            jour = liste_jours_semaine[4] # pour conserver le vendredi de chaque semaine
            conserver_sauvegarde_de_la_semaine(jour)
            numero_de_jour = 0
        return numero_de_jour

def conserver_sauvegarde_de_la_semaine(jour):
    """
    Réaliser une copie du fichier envoyé par gestion_backup_semaine dans le fichier de conservation_semaine.
    """
    conservation_dir = "/sftp_mount/archives/conservation_semaine/"
    os.makedirs(conservation_dir, exist_ok=True)

    source_dir = "/sftp_mount/archives/"
    for filename in os.listdir(source_dir):
        if jour in filename:
            source_file = os.path.join(source_dir, filename)
            destination_file = os.path.join(conservation_dir, filename)
            
            try:
                shutil.copy(source_file, destination_file)
                print(f"Successfully copied {filename} to {destination_file}")
            except FileNotFoundError:
                print(f"Error: {source_file} not found.")
            except Exception as e:
                print(f"An error occurred while copying {filename}: {e}")

def supprimer_old_backup(jour):
    """
    Supprime l'ancienne backup du jour courant, par exemple le lundi il supprime lundi dernier.
    """
    liste_fichier = os.listdir('/sftp_mount/archives/')
    for fichier in liste_fichier:
        if jour in liste_fichier:
            os.remove(fichier)

def sauvegarde_du_jour(jour):
        date = datetime.date.today()
        nom = jour+"-"+str(date)+".backup"

        # Crée la backup
        os.system("yunohost backup create") 

        # Renome pour pouvoir la gérer après                                                     
        os.system("rm /home/yunohost.backup/archives/*.json")                                    
        cmd = 'find /home/yunohost.backup/archives/ -type f ! -name "*backup*" -exec mv {{}} /home/yunohost.backup/archives/{} \;'.format(nom)                                                
        os.system(cmd)          

def sauvegarde_log_numero_du_jour(num_de_jour):
    num_de_jour = str(num_de_jour)
    with open("/Backcup-s/last_day.log", 'w') as last_day:
        last_day.write(num_de_jour)

def gestion_backup_mois():
    """
    Récupère le dernier jour sauvegardé dans les logs compte_mois.log
    Vérifie si c'est le dernier jour du mois,
    Si oui il sauvegarde le vendredi à partir de la fonction conserver_sauvegarde_du_mois.
    """
    with open("/Backcup-s/compte_mois.log", 'r') as compte_mois:
        contenu = compte_mois.readlines()
        compteur = int(contenu[0]) + 1
        if compteur >= 30:
            jour = liste_jours_semaine[0] # pour conserver le dernier lundi de chaque mois
            conserver_sauvegarde_du_mois(jour)
            compteur = 0
            with open("/Backcup-s/compte_mois.log", 'w') as compte_mois:
                compteur = str(compteur)
                compte_mois.write(compteur)
        else:
            with open("/Backcup-s/compte_mois.log", 'w') as compte_mois:
                compteur = str(compteur)
                compte_mois.write(compteur)

def conserver_sauvegarde_du_mois(jour):
    """
    Réaliser une copie du fichier envoyé par gestion_backup_mois dans le fichier de conservation_semaine.
    """
    conservation_dir = "/sftp_mount/archives/conservation_30_jour/"
    os.makedirs(conservation_dir, exist_ok=True)

    source_dir = "/sftp_mount/archives/"
    for filename in os.listdir(source_dir):
        if jour in filename:
            source_file = os.path.join(source_dir, filename)
            destination_file = os.path.join(conservation_dir, filename)
            
            try:
                shutil.copy(source_file, destination_file)
                print(f"Successfully copied {filename} to {destination_file}")
            except FileNotFoundError:
                print(f"Error: {source_file} not found.")
            except Exception as e:
                print(f"An error occurred while copying {filename}: {e}")

def main():
    num_de_jour = gestion_backup_semaine()

    liste_jours_semaine = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
    jour = liste_jours_semaine[num_de_jour]

    supprimer_old_backup(jour)
    sauvegarde_du_jour(jour)

    sauvegarde_log_numero_du_jour(num_de_jour)
    gestion_backup_mois()

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
