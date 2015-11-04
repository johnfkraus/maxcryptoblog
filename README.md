# cryptoblog



  860  yum remove rh-python34

  889  cd djtutorial/



  892  mkdir cryptoblog

  915  yum install python-virtualenv

  943  yum remove python-virtualenv
  945  yum install python-virtualenv

  949  virtualenv --python=python3.4 myvenv
  951  source myvenv/bin/activate


  953  django-admin startproject mysite .


  960  pip install django==1.8
  961  python manage.py migrate
  962  python manage.py runserver 

  999  cd cryptoblog/
 1001  echo "# cryptoblog" >> README.md
 1002  git init
 1003  git add README.md
 1004  git commit -m "first commit"
 1005  git remote add origin https://github.com/johnfkraus/cryptoblog.git
 1006  git push -u origin master
 1008  git add .
 1009  git commit -m 'startproject, migrate'
 1010  git push
 1012  cat README.md 
 1013  history >> README.md 

Change time zone.
in mysite/settings.py after
STATIC_URL = '/static/'
add
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

(myvenv) ~/djangogirls$ python manage.py migrate

(myvenv) ~/djangogirls$ python manage.py runserver

browse to http://127.0.0.1:8000/

(myvenv) ~/djangogirls$ python manage.py startapp blog


    (myvenv) ~/djangogirls$ python manage.py startapp blog


to blog/models.py add Post model.

    (myvenv) ~/djangogirls$ python manage.py makemigrations blog


replace contents of blog/admin.py add:

```python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

    (myvenv) ~/djangogirls$ python manage.py createsuperuser


run `python manage.py runserver` 
browse to  http://127.0.0.1:8000/admin/


