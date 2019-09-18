# Umbrella Policy Test
Python 3.5+ script to quickly test if various Cisco Umbrella settings/policies are enabled.

## Background/About
To support a PoC, I needed a way to quickly test all of the test pages that Cisco Umbrella uses to test various policy configurations (see this URL).  Basically, as policy was changed/added/removed, I needed a way to test if a virtual endpoint was getting to Umbrella test pages (policy pass or fail).  

The script is pretty simple and uses [Splinter](https://splinter.readthedocs.io/en/latest/) and chromium as I had similar code from another project.  I may re-write using pyppeteer and/or requests to remove the browser dependency.  Basically it loops through all the URLs in a CSV file and then looks for text on the page - "PassedText" indicates that the text in the column with the same name was found.


## Installation
PortToggler was tested/written on Python 3.7 but should work on 3.5+.  It requires the following external Python modules:
* requests
* click
* click_config_file

Preferred method of installation is in a Python virtual environment.

**1. Clone this repo**
```
git clone https://github.com/zabrewer/UmbrellaPolicyTest
```

**2. Make a new virtual environment in the local folder**
```
python3 -m venv UmbrellaPolicyTest
```
(generic command structure is):
python3 -m venv /path/to/new/virtual/environment


**3. activate the virtual environment:**

example location for virtual environment activation script:
mac/linux:
/path/to/env/bin/activate

windows:
C:\path\to\env\Scripts\activate.bat

actual commands to activate UmbrellaPolicyTest virtual environment:
mac/linux:
```
cd UmbrellaPolicyTest
source bin/activate
```

windows (virtualenv creates an activate.bat file in the Scripts subfolder of the virtual environment dir):
```
cd UmbrellaPolicyTest
Scripts\activate.bat
```
If completed successfully, your command prompt should now have changed (begins with the virtual environment name in parentheses)

To exit the virtual environment at any time, use the deactivate command
```
deactivate
```

## Install Chromium


## Usage
Invoke PortToggler.py --help to get started.  You need an API key, the switch's serial number, and the switch port.

Primary options: --action=disable|enable|status

Examples:

    python PortToggler.py --api-key 123456789 --serialnumber A1B2C3D4 --switchport 5 --action=disable
    
    python PortToggler.py -A 123456789 -SN A1B2C3D4 -SP 5 --action=disable
    
    python PortToggler.py --config /path/to/file/api.cfg --serialnumber A1B2C3D4 --switchport 5 --action=disable

    python PortToggler.py --config api.cfg --serialnumber A1B2C3D4 --switchport 5 --action=disable

    If used, the api config file should contain one line similar to the following (single quotes required) e.g.
    api_key = '123456789'

This project is licensed to you under the terms of the [Cisco Sample
Code License](./LICENSE).

