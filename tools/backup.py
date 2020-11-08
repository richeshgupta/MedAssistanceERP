from django.db import connection
import os
import time
from datetime import datetime
from subprocess import check_output

def db_backup():
    print(os.name)
    date = time.time()
   
    if os.name=='posix':
        path = '~/'
    else:
        # For Windows
        path='D:/'
    x = str(datetime.fromtimestamp(date))
    x = (x[:10])
    cmnd = 'pg_dump -U postgres -d "MedDb" -f {path}backup-{x}-{date}.sql'.format(path=path,date=date,x=x)
    # os.system("cmd /k 'pg_dump -U postgres -d MedDb -f C:/backup.sql'")
    print(check_output(cmnd,shell=True).decode())
    return path,time


