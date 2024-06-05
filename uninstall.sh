fusermount -u /backup.backup/archives
rm -R /backup.backup/
rm -R /script_backup/
rm /setup.sh
sed -i 's/\/backup\.backup/\/home\/yunohost\.backup/g' /usr/lib/python3/dist-packages/yunohost/backup.py
sed -i 's/backup\.backup/yunohost\.backup/' /usr/lib/python3/dist-packages/yunohost/app.py
crontab -l | sed '/\/script_backup\/script.py/d' | crontab -
