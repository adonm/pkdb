# pkdb
Parkour DB

Description to come, a basic platform for parkour related apps.

On ubuntu 14.04 setup:

```
cd pkdb
apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk python3-dev build-essential python3-pip libpq-dev
pyvenv-3.4 venv
. venv/bin/activate
pip install -r requirements.txt
uwsgi -i pkdb.ini
```

Database setup (insecure, but quick for the lazy)

```
apt-get install postgresql-9.4-postgis-2.1
sudo -u postgres createuser -s www-data
sudo -u postgres createuser -s root
createdb pkdb-dev
createdb pkdb
./manage.py migrate
```
