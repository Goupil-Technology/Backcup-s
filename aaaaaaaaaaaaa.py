import os

def supprimer_old_backup(jour):
    """
    Supprime l'ancienne backup du jour courant, par exemple le lundi il supprime lundi dernier.
    """
    liste_fichier = os.listdir('/sftp_mount/archives/')
    for fichier in liste_fichier:
        if jour in fichier:
          path = "/sftp_mount/archives/"+jour
          os.remove(path)

supprimer_old_backup("mardi")
