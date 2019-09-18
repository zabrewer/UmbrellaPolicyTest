#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""UmbrellaPolicyTest Console Script.

Copyright (c) 2019 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

"""
__author__ = "Zach Brewer"
__email__ = "zbrewer@cisco.com"
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2019 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"


from splinter import Browser
import time
import csv

# time in seconds to sleep between page visits
sleeptime = 5   
# ToDo csv file as CLI argument with default of umbrella_urls.csv
csv_filename = 'umbrella_urls.csv'
# debug mode? True/False
debug = False
# headless browser?  True/False
headless = False

browser = Browser('chrome', headless=headless)

def csv_dict_list(filename):    
    # Open variable-based csv, iterate over the rows and map values to a list of dictionaries containing key/value pairs
    reader = csv.DictReader(open(filename, 'rt', encoding='utf-8-sig'))
    dict_list = []
    for line in reader:
        dict_list.append(line)
    return dict_list

csv_data = csv_dict_list(csv_filename)

for item in csv_data:
    testname = item['Testname']
    url = item['URL']
    description = item['Description']
    passedtext = item['PassedText']
    failedtext = item['FailedText']
    print('Processing OpenDNS Test for testname "' + testname + '" and URL "' + url + '"')
    browser.visit(url)
    passed = browser.is_text_present(passedtext)
    failed = browser.is_text_present(failedtext)
    dns_error = browser.is_text_present('This site can’t be reached')
    if debug:
        print('testing for passedtext ', passedtext)
        print('checking for failedtest', failedtext)
        print('passed is', passed)
        print('failed is', failed)

    if passed:
        print('OpenDNS Test "' + testname + '" passed for URL "' + url + '"\n')
    elif failed:
        print('OpenDNS Test "' + testname + '" failed for URL "' + url + '"\n')
    elif dns_error:
        print('Chromium Browser was not able to reach the URL for ' + testname + ' URL: ' + url + '\n')
    else:
        print('Could not find either pass or fail text for "' + testname + 
        '" and URL "' + url + '". \n\n.' +
        'You may want to adjust the sleeptime variable to give the page more time to load.\n' +
        'Also check the csv file PassedText and FailedText column entries for the given testname.\n'
        )

    time.sleep(sleeptime)

browser.quit()
#This site can’t be reached
        
