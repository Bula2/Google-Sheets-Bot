import time

import schedule
from Drive_API import updateDate

schedule.every().day.at("02:01").do(updateDate)

while True:
    schedule.run_pending()
    time.sleep(1)