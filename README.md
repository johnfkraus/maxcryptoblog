# cryptoblog

as of Nov 6, 2015, deployed here: http://johnfkraus.pythonanywhere.com


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

add .giritnore
```
*.pyc
__pycache__
myvenv
db.sqlite3
/static
.DS_Store
```

### Django ###
*.log
*.pot
*.pyc
__pycache__/
local_settings.py

Clean out files that should have been ignored:

git rm --cached -r .
git add .

Open a bash console at pythonanywhere.com

https://www.pythonanywhere.com/user/johnfkraus/consoles/bash/1924336/

    $ git clone https://github.com/johnfkraus/cryptoblog.git

$ cd my-first-blog

$ virtualenv --python=python3.4 myvenv

$ source myvenv/bin/activate

(mvenv) $  pip install django whitenoise


    (mvenv) $ python manage.py collectstatic

    (mvenv) $ python manage.py migrate

    (mvenv) $ python manage.py createsuperuser

Click back to the PythonAnywhere dashboard by clicking on its logo, and go click on the **Web** tab. Finally, hit **Add a new web app**.

After confirming your domain name, choose **manual configuration** (NB *not* the "Django" option) in the dialog. Next choose **Python 3.4**, and click Next to finish the wizard.

### Setting the virtualenv

In the "Virtualenv" section, click the red text that says "Enter the path to a virtualenv", and enter:  `/home/<your-username>/my-first-blog/myvenv/`. Click the blue box with the check mark to save the path before moving on.

### Configuring the WSGI file

Django works using the "WSGI protocol", a standard for serving websites using Python, which PythonAnywhere supports. The way we configure PythonAnywhere to recognise our Django blog is by editing a WSGI configuration file.

Click on the "WSGI configuration file" link (in the "Code" section near the top of the page -- it'll be named something like `/var/www/<your-username>_pythonanywhere_com_wsgi.py`), and you'll be taken to an editor.

Delete all the contents and replace them with something like this:

```python
import os
import sys

path = '/home/johnfkraus/cryptoblog'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(get_wsgi_application())
```

> **Note** Don't forget to substitute in your own username where it says `<your-username>`

This file's job is to tell PythonAnywhere where our web app lives and what the Django settings file's name is. It also sets up the "whitenoise" static files tool.

Hit **Save** and then go back to the **Web** tab.

We're all done! Hit the big green **Reload** button and you'll be able to go view your application. You'll find a link to it at the top of the page.

Go to the admin page!!

  http://johnfkraus.pythonanywhere.com/admin/blog/post/

## Debugging tips

If you see an error when you try to visit your site, the first place to look for some debugging info is in your **error log**. You'll find a link to this on the PythonAnywhere [Web tab](https://www.pythonanywhere.com/web_app_setup/). See if there are any error messages in there; the most recent ones are at the bottom. Common problems include:

- Forgetting one of the steps we did in the console: creating the virtualenv, activating it, installing Django into it, running collectstatic, migrating the database.

- Making a mistake in the virtualenv path on the Web tab -- there will usually be a little red error message on there, if there is a problem.

- Making a mistake in the WSGI configuration file -- did you get the path to your my-first-blog folder right?

- Did you pick the same version of Python for your virtualenv as you did for your web app? Both should be 3.4.

- There are some [general debugging tips on the PythonAnywhere wiki](https://www.pythonanywhere.com/wiki/DebuggingImportError).

And remember, your coach is here to help!

# You are live!

The default page for your site should say "Welcome to Django", just like it does on your local computer. Try adding `/admin/` to the end of the URL, and you'll be taken to the admin site.



