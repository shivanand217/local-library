# Local Library

Local Library website written in Django. Creates an online catalog for a small local library, 
where users can browse available books and manage their accounts.

```
   pip3 install -r requirements.txt
   python3 manage.py makemigrations
   python3 manage.py migrate
   python3 manage.py collectstatic
   python3 manage.py test # Run the standard tests. These should all pass.
   python3 manage.py createsuperuser # Create a superuser 
   python3 manage.py runserver
   ```
