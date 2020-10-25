from django.db import connection
import os
import time
from subprocess import check_output

def db_backup():
    print(os.name)
    date = time.time()
    # For Windows
    if os.name=='posix':
        path = '~/'
    else:
        path='D:/'
    
    cmnd = 'pg_dump -U postgres -d "MedDb" -f {path}backup-{date}.sql'.format(path=path,date=date)
    # os.system("cmd /k 'pg_dump -U postgres -d MedDb -f C:/backup.sql'")
    print(check_output(cmnd,shell=True).decode())
db_backup()

