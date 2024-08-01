# Install
```sh
git clone https://github.com/vaig2010/django_tree_menu
```
## Create virtual env
```sh
python -m venv venv
```
### On Windows, run:
```sh
venv\Scripts\activate
```
### On Unix or MacOS, run:
```sh
venv/bin/activate
```
## Install dependencies (only django)
```sh
pip install django
```
## Migrate and add sample data
```sh
cd django_tree_menu/tree_menu && python manage.py migrate
python manage.py add_sample_data
```
## Run
```sh
python manage.py runserver
```
