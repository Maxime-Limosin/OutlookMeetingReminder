# Meeting Reminder
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Outlook](https://img.shields.io/badge/Microsoft_Outlook-0078D4?style=for-the-badge&logo=microsoft-outlook&logoColor=white)
![](http://ForTheBadge.com/images/badges/built-with-love.svg)

An app to automatically message me on SynologyChat if I have meetings soon.


### Run the app
```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment (zsh)
source venv/bin/activate

# Activate the virtual environment (fish)
# source venv/bin/activate.fish

# Install the required packages
pip3 install -r requirements.txt

# Run the main.py file
python main.py
```

## Usage
You'll have to create the conf.yml file:
* email
* password
* serverAddress
* token: the token of the SynologyChat incoming webhook

Exemple:
```yaml
outlook:
  email: maxime@mail.fr
  password: mySuperPassword
  serverAddress: outlook.office365.com
  
synology:
  token: mySuperToken
```

## Run code automatically
On Linux:
```bash
sudo apt install crontab -y
crontab -e # Choose nano (1st option)
```

Inside crontab, add this ligne:
```
0 17 * * 1-5 [path to project]/venv/bin/activate.fish [path to project]/main.py
```

This will call the program /usr/bin/python3, with the main.py as argument. It'll be called at 17h00 the 1st to 5th day of the week (Monday to Friday).
