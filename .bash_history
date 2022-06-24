sudo apt update
sudo apt -y install vim bash-completion wget
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" |sudo tee  /etc/apt/sources.list.d/pgdg.list
sudo apt update
sudo apt -y install postgresql-12 postgresql-client-12
systemctl status postgresql.service 
sudo su - postgres
psql -U thb2117 -h 35.196.192.139 -d proj1part2
psql -U <thb2117> -h 35.196.192.139 -d proj1part2
psql -U thb2117 -h 35.196.192.139 -d proj1part2
psql --version
psql
psql -U thb2117 -h 35.196.192.139 -d proj1part2
psql -U thb2117 -h 35.196.192.139 -d  proj1part2
root
psql -U thb2117 -h 35.196.192.139 -d  proj1part2
ls
nano text.txt
ls
sudo -i
wget http://www.cs.columbia.edu/~biliris/4111/22summer/projects/proj1-3/webserver.tar
tar xf webserver.tar
mv webserver <hellow1>
mv webserver hellow1
cd hellow1
cd ..
mv webserver comswpart3

tar xf webserver.tar
mv webserver comswpart3
cd comswpart3
git config --global user.name "Tanveer"
git config --global user.email "thb2117@columbia.edu"
git init
git remote add origin https://github.com<thb2117>/<comswpart3>.git
git remote add origin https://github.com<thb2117>/<COMSW4111>.git
git remote add origin https://github.com<thb2117>/<comswpart3>.git
git inti
git --help
init
git init
git remote add origin https://github.com<thb2117>/<comswpart3>.git
git remote add origin https://github.com<thb2117>/<COMSW4111>.git
git remote add origin https://github.com<thb2117>/.git
git remote add origin https://github.com<thb2117>.git
git init
cd..
git remote add origin https://github.com<thb2117>/<comswpart3>.git
git add --all
git commit -m "initial commit"
git push -u origin master
git push -u
git push -u origin master
exit
git status
ls
sudo -i
source venv/bin/activate
ls
cd my_flask_app/
source venv/bin/activate
nano
nano app.py
ls
cd my_flask_app
ls
rm app.py.save
ls
. venv/bin/activate
pip install Flask
pip install Gunicorn
nano app.py
nano creatdb.py
pip install psycopg2
sudo apt install python3-dev libpq-dev
pip install psycopg2
pip install wheel
pip install psycopg2
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update
sudo apt-get -y install postgresql
sudo apt install python3-dev libpq-dev
pip install psycopg2
sudo apt install libpq-dev
pip install psycopg2
sudo apt-get install libffi-dev
pip install psycopg2
pip install psycopg2-binary
sudo apt-get install python3-dev
sudo apt-get install build-essential
pip install psycopg2
nano creatdb.py
python creatdb.py
nano creatdb.py
python creatdb.py
psql -U thb2117 -h 35.196.192.139 -d proj1part2
cd my_flask_app
. venv/bin/activate
ls
cd ..
ls
cd my_flask_app
rm app.py
ls
mv ../app.py /
cp ../app.py app.py
ls
cp ../wsgi.py wsgi.py
ls
cd my _flask_app
cd my_flask_app
. venv/bin/activate
mkdir templates
cd templates
ls
cd ..
rm -r templates
ls
cp ../templates.zip templates.zip
ls
unzip templates.zip -d templates
sudo apt install unzip
unzip templates.zip -d templates
ls
rm -r templates
ls
unzip templates.zip
ls
rm templates.zip
ls
nano app.py
rm app.py
nano app.py
gunicorn --bind=0.0.0.0:8080 -w 3 wsgi:app
