# YaraManager
Web based Manager for Yara Rules

Python 3 version

Before installation, make sure Python3 + pip are installed

## Automatic installation for windows:
* git clone the repo
* cd to\YaraManager\Path
* .\install.bat

Note - during the installation you'll be prompted to enter a username & a password

Please enter a username in an email convention (user@email.com) - the email does not have to be real

* .\run.bat


## Manual installation
* git clone the repo
* cd to\YaraManager\Path
* (optional) install virtualenv - python3 -m virtualenv venv && ./venv/Scripts/activate
* pip install -r requirements.txt 
* python manage.py createsuperuser
* python manage.py collectstatic
* python manage.py makemigrations
* python manage.py makemigrations rule_manager
* python manage.py migrate
* (run with -) python manage.py runserver

## Screenshots
Main view  - rules table + filtering
![](README_files/rules_table.PNG?raw=true "")

Rule edit page
![](README_files/rule_edit.PNG?raw=true "")
