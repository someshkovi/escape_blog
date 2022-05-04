# escape_blog

## ✨ How to use it

```bash
$ # Get the code
$ git clone https://github.com/someshkovi/escape_blog.git
$ cd escape_blog
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ # Install modules - SQLite Storage
$ pip3 install -r requirements.txt
$
$ # Create tables
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Create superuser
$ python manage.py createsuperuser
$
$ # Start the application (development mode)
$ python manage.py runserver # default port 8000
$
$ # Start the app - custom port
$ # python manage.py runserver 0.0.0.0:<your_port>
$
$ # Access the web app in browser: http://127.0.0.1:8000/
```

## ✨ Code-base structure
```bash
## Project structure
< PROJECT ROOT >
    ├───media_root
    ├───src
    │   ├───blog
    │   ├───marketing
    │   ├───posts
    │   ├───static_files
    │   │   ├───css
    │   │   ├───fonts
    │   │   ├───icons
    │   │   ├───icons-reference
    │   │   │   └───fonts
    │   │   ├───img
    │   │   ├───js
    │   │   ├───styles
    │   │   └───vendor
    │   │       ├───bootstrap
    │   │       ├───font-awesome
    │   │       ├───jquery
    │   └───templates
    │       ├───account
    │       │   ├───email
    │       │   ├───messages
    │       │   └───snippets
    │       ├───openid
    │       ├───socialaccount
    │       │   ├───messages
    │       │   └───snippets
    │       └───tests
    └───static_root
```

## ✨ Deployment

### [Gunicorn](https://gunicorn.org/)
---

Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX.

> Install using pip

```bash
$ pip install gunicorn
```
> Start the app using gunicorn binary

```bash
$ gunicorn --bind=0.0.0.0:8001 core.wsgi:application
Serving on http://localhost:8001
```

Visit `http://localhost:8001` in your browser. The app should be up & running.


<br />

### [Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/)
---

Waitress (Gunicorn equivalent for Windows) is meant to be a production-quality pure-Python WSGI server with very acceptable performance. It has no dependencies except ones that live in the Python standard library.

> Install using pip

```bash
$ pip install waitress
```
> Start the app using [waitress-serve](https://docs.pylonsproject.org/projects/waitress/en/stable/runner.html)

```bash
$ waitress-serve --port=8001 core.wsgi:application
Serving on http://localhost:8001
```

Visit `http://localhost:8001` in your browser. The app should be up & running.

<br />