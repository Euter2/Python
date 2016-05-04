from crontab import CronTab
from datetime import datetime
from astral import Location

# Location info for sunrise and sun calculation
info=( 'Brno', 'Czech Republic', 49.241921, 16.566693, 'Europe/Prague', 278 )
l=Location(info)

# Calculate sunrise and sunset for current day
brno_today_sunrise=l.sunrise(datetime.today().date(), True)
brno_today_sunset=l.sunset(datetime.today().date(), True)

# Open crontab file
file_cron=CronTab(tabfile='crontab.txt')

# Find open and close job in crontab and update 
# sunrise and sunset with calculated time 
for job in file_cron:
    if 'open command to window' in job.comment:
        job.hour.on(brno_today_sunrise.hour)
        job.minute.on(brno_today_sunrise.minute)
    elif 'close command to window' in job.comment:
        job.hour.on(brno_today_sunset.hour)
        job.minute.on(brno_today_sunset.minute)

# Write changes to crontab file
file_cron.write()
