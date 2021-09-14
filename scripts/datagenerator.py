import csv
import random
from datetime import datetime, timedelta

voltage = random.randint(0, 220)
current = random.randint(0, 10)

now = datetime.now()
current_time = now + timedelta(seconds=60)
with open('CV.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
    for item in range(1440):
        current_time = current_time + timedelta(seconds=60)
        writer.writerow([str(current_time), str(random.randint(1, 220)), str(random.randint(1, 10))])
