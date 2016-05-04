from crontab import CronTab
from datetime import datetime
from astral import Location

info=( 'Brno', 'Czech Republic', 49.241921, 16.566693, 'Europe/Prague', 278 )
l=Location(info)

brno_today_sunrise=l.sunrise(datetime.today().date(), True)
brno_today_sunset=l.sunset(datetime.today().date(), True)

file_cron=CronTab(tabfile='crontab.txt')

for job in file_cron:
    if 'open command to window' in job.comment:
        job.hour.on(brno_today_sunrise.hour)
        job.minute.on(brno_today_sunrise.minute)
    elif 'close command to window' in job.comment:
        job.hour.on(brno_today_sunset.hour)
        job.minute.on(brno_today_sunset.minute)

file_cron.write()
