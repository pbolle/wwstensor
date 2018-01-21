#!/usr/bin/env python

import os
import csv
import datetime
from collections import deque

TARGET_DIR = "/home/pbolle/Dokumente/weather/converted/model1.csv"
SOURCE_DIR = "/home/pbolle/Dokumente/weather/raw/"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
puffer = deque([])
pufferSize = 12
datafiles = []
for year in os.listdir(SOURCE_DIR):
    for month in os.listdir(SOURCE_DIR + year):
        for day in os.listdir(SOURCE_DIR + year + "/" + month):
            datafile = SOURCE_DIR + year + "/" + month + "/" + day
            if os.path.isfile(datafile):
                datafiles.append(datafile)
datafiles = sorted(datafiles)

f = open(TARGET_DIR, 'wt')
try:
    writer = csv.writer(f)
    writer.writerow(
        ["date", "delay", "hum_in", "temp_in", "hum_out", "temp_out", "abs_pressure", "rel_pressure", "wind_ave",
         "wind_gust", "wind_dir", "rain", "status", "illuminance", "uv", "temp_out_1h"])
    for datafile in datafiles:
        with open(datafile, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                eventDate = datetime.datetime.strptime(row[0], DATE_FORMAT)
                targetRow = [eventDate.month, eventDate.day, eventDate.hour, eventDate.minute] + row[1:]
                puffer.append(row[5])
                if len(puffer) > pufferSize:
                    row = row + [puffer.popleft()]
                    print(row)
                    writer.writerow(row)
finally:
    f.close()
