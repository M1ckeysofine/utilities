python
#!/usr/bin/env python3
# A Program to interface with the PhishMe API and pull down the full CSV Results from the previous month
# Originally written by ************ @BlankSpace2Day
# Improved by Cedric

import json
import csv
import time
import datetime
from urllib.request import Request, urlopen
from urllib.error import URLError
import os

# Configuration
API_TOKEN = "PUT API TOKEN HERE"
BASE_URL = "https://login.phishme.com/api/v1/"
OUTPUT_DIR = "/home/user/"

def get_last_month():
    now = datetime.datetime.now()
    return (now.month - 2) % 12 + 1  # Correctly handles December (12 -> 11)

def make_api_request(url):
    request = Request(url)
    request.add_header('Authorization', f'Token token="{API_TOKEN}"')
    try:
        with urlopen(request) as response:
            return json.loads(response.read())
    except URLError as e:
        print(f"Error making API request: {e}")
        return None

def get_scenarios():
    url = f"{BASE_URL}scenarios.json"
    return make_api_request(url)

def download_csv(url, filename):
    request = Request(url)
    request.add_header('Authorization', f'Token token="{API_TOKEN}"')
    try:
        with urlopen(request) as response, open(filename, 'w', newline='') as csvfile:
            csvreader = csv.reader(response.read().decode('utf-8').splitlines())
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(csvreader)
        print(f"{datetime.datetime.now()} Downloaded and saved as {filename}")
        return True
    except URLError as e:
        print(f"Error downloading CSV: {e}")
        return False

def main():
    last_month = get_last_month()
    scenarios = get_scenarios()

    if not scenarios:
        print("Failed to retrieve scenarios. Exiting.")
        return

    csv_data = [(s['full_csv_url'], s['id']) for s in scenarios 
                if s['date_started'].startswith(str(last_month))]

    print(f"{datetime.datetime.now()} Processing {len(csv_data)} Scenario Results")

    for url, scenario_id in csv_data:
        filename = os.path.join(OUTPUT_DIR, f"phishmefailures_{scenario_id}.csv")
        if download_csv(url, filename):
            print(f"{datetime.datetime.now()} Sleeping to prevent API cooldown timer")
            time.sleep(5)

if __name__ == "__main__":
    main()
