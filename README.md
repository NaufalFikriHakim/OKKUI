# OKKUI API testing and development application

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/NaufalFikriHakim/OKKUI.git
$ cd OKKUI
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python -m venv env
```
```sh
Windows:
env\Scripts\activate.bat
```
```sh
Unix (Linux & Mac OS):
source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.

## Walkthrough

There are 2 main features in this application. Those two feateures are API call and API list.
You can access API call page by pressing the API call button in the home page or by typing `http://127.0.0.1:8000/api-call/` on your website.
When calling an API, please refer to the documentation profided in API list page. You can access this page by pressing the API list button in the home page or by typing `http://127.0.0.1:8000/api-list/` on your website