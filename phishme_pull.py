#!/usr/bin/python
# A Program to interface with the PhishMe API and pull down the full CSV Results from the previous month
#written by M1ckeysofine @BlankSpace2Day please holler with questions or comments

import urllib2
import json
import csv
import time
import datetime

#We need to have the date and the last month's numeric month
now = datetime.datetime.now()
last_month = now.month - 1 if now.month > 1 else 12

#API URL setup stuff here. Make sure to include the Unique API Token from PhishMe

url = "https://login.phishme.com/api/v1/scenarios.json"
request = urllib2.Request(url)
request.add_header('Authorization', 'Token token="PUT API TOKEN HERE"')
response = urllib2.urlopen(request)
jsoncontent = response.read()

#Lists of results from the previous month.
#Note the range use in the for loop: if you run more that 4 scenarios in a month increase the range maximum to a number greater than you expect to have monthly, We de-duplicate the list later

csv_url_list = []
csv_id_list = []
for i in range(0,5):
    if json.loads(jsoncontent)[i]['date_started'].startswith(str(last_month)):
        csv_url_list.append(json.loads(jsoncontent)[i]['full_csv_url'])
        csv_id_list.append(json.loads(jsoncontent)[i]['id'])


#As promised de-duplication of the list to create a list of files we will download

download_list = list(set(csv_url_list))
print str(now) + " Processing " + str(len(download_list)) + " Scenario Results"

#I tried this a couple ways. The approach of for x in len(download_list) was failing me so I went with the old faithful index count for traversal
#Again you need to make sure the Unique API Token is assigned as token
#PhishMe has a cooldown time for large downloads so I added a 5 second wait between downloads to prevent hitting that timeout

filename_list = []
count = 0
while count < len(download_list):
    for i in download_list:
        csvrequest = urllib2.Request(i)
        csvrequest.add_header('Authorization', 'Token token="PUT API TOKEN HERE"')
        csvresponse = urllib2.urlopen(csvrequest)
        file = csv.reader(csvresponse)
        print str(now) + " Processing URL " + i
        filename = "/home/user/phishmefailures_" + str(csv_id_list[count]) + ".csv"
        filename_list.append(filename)
        with open (filename, "w") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(file)
        print str(now) + " Sleeping to prevent API cooldown timer"
        time.sleep(5)
        count = count + 1
        print str(now) + " " + i + " Downloaded and saved as " + filename

                                                                                     

