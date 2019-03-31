# fossee2

Project for IITB summer Internship Entrance


- Clone the repo
``` 
git clone https://github.com/mananpoddar/fossee2
cd fossee2/mysite
```
- Create a virtualenv
```
virtualenv -p python3 venv
source venv/bin/activate
```

- Install the requirements
```
pip install -r requirements.txt
```
- Setup your mysql database and sync it with my project
```
go to fossee2/mysite/mysite/settings.py and in DATABASE array, change the password and 
username to yours.
do python manage.py makemigrations
then, python manage.py migrate
```

- close any libreoffice application running on your system for better experience
- Run the dev server 
```
python manage.py runserver
```
- request localhost:8000/fossee2
<br><br>
- Important directories and files to make your look up to the code easier
```
core backend logic - > fossee2/mysite/fossee2/views.py
core frontend logic - > fossee2/mysite/fossee2/static/fossee2/ajax.js
templates(html files) - > fossee2/mysite/fossee2/templates/fossee2/
routing files - > fossee2/mysite/fossee2/urls.py

```

