import os
import shutil

# Constantes
NB_BACKUP_CONSERVE = 7
BACKUP_PATH = "/home/yunohost.backup/archives"
LOG_PATH = "/script_backup/backup.log"

INTERVAL_BACKUP = [7, 14, 21, 28, 30]
BACKUP_PATH_SEMAINE = "/home/yunohost.backup/archives/sauvegarde_semaine"
BACKUP_PATH_MOIS = "/home/yunohost.backup/archives/sauvegarde_mois"
LOG_CYCLE = "/script_backup/cycle.log"

def get_backup(path):
    return os.listdir(path)

def create_backup():
    try:
        os.system('yunohost backup create')
        return 0
    except:
        return "backup did not work..."

def get_diff_backup_liste(old_backup_liste, new_backup_liste):
    new = []
    for backup in new_backup_liste:
        if backup not in old_backup_liste:
            print("Nouveau fichier: "+backup)
            new.append(backup)

    cycle(new)

    with open(LOG_PATH, "a") as log:
        for file in new:
            log.write(file)
            log.write(" ")
        log.write("\n")

    with open(LOG_PATH, "r") as log:
        lignes = log.readlines()
        nb_ligne = len(lignes)

def cycle_suppr_backup():
    """ Cette fonction est chargée de supprimer les backups les plus anciennes au fur et à mesure en fonction de NB_BACKUP_CONSERVE définit en constante plus haut.
    Par exemple si 'NB_BACKUP_CONSERVE' vaut 5, les sauvegarde seront conservés sur 5 cycles.
    Il met ensuite le fichier log à jour."""
    with open(LOG_PATH, "r") as log:
        lignes = log.readlines()
        if len(lignes) > NB_BACKUP_CONSERVE:
            suppr_backup(lignes[0])
            with open(LOG_PATH, "w") as log:
                [log.write(i) for i in lignes[1:]]

def suppr_backup(backup):
    file_to_delete = [backup.split(" ")[0], backup.split(" ")[1].strip()]
    print("suppr de ", file_to_delete)
    [os.system(f"rm {BACKUP_PATH}/{file}") for file in file_to_delete]

def main():
    old_backup_liste = get_backup(BACKUP_PATH)

    create_backup()

    new_backup_liste = get_backup(BACKUP_PATH)

    get_diff_backup_liste(old_backup_liste, new_backup_liste)

    cycle_suppr_backup()

# ---------------------------------------------------- parti gestion de cycle

def copie_cycle(BACKUP_PATH, filename):
    for i in filename:
        path = "/home/yunohost.backup/archives/"+str(i)
        shutil.copy(path, BACKUP_PATH)
    return 0

def cycle(new):
    with open(LOG_CYCLE, 'r') as cycle:
        numero_de_jour = cycle.readlines()[0]
        if int(numero_de_jour) >= INTERVAL_BACKUP[-1]:
            print("Copie pour le jour dans l'emplacement mois "+numero_de_jour)
            copie_cycle(BACKUP_PATH_MOIS, new)
            with open(LOG_CYCLE, 'w') as cycle:
                cycle.write('0')
        elif int(numero_de_jour) in INTERVAL_BACKUP:
            print("Copie pour le jour dans l'emplacement semaine "+numero_de_jour)
            copie_cycle(BACKUP_PATH_SEMAINE, new)
            with open(LOG_CYCLE, 'w') as cycle:
                cycle.write(str(int(numero_de_jour) + 1))
        else:
            print("Pas de copie supplémentaire")
            with open(LOG_CYCLE, 'w') as cycle:
                cycle.write(str(int(numero_de_jour) + 1))

if __name__ == "__main__":
    main()
