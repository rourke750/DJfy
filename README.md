# DJfy

Welcome to DJfy.

This project is based on providing your guests an easy way to control what songs are playing during your event.

## Installation
First things first in order to install this project you will need python.
Consider running a [virtual environment](https://gist.github.com/tyrothalos/c7e08497b01384811fdc8c725f560e99) first.
Then we are going to use pip to install the dependencies, so run
>pip install -r requirements.txt
You are then going to need to enter the DJfy directory (if you setup a virtual environment you need to enter it) and then run
>python manage.py migrate
This creates your database tables.

## Configuration
You will then take Djfy/Djfy/secret_settings.py.template and copy it and rename the copy to secret_settings.py.
You will need to configure that file.  This file protects you from accidently uploading private credetials to github.

## Starting the server
First navigate into DJfy and then run
>python manage.py runserver