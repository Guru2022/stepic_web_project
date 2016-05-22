sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/nginx.conf
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo ln -sf /home/box/web/etc/ask.py /etc/gunicorn.d/ask.py
sudo /etc/init.d/gunicorn restart

sudo pip install pip --upgrade
sudo pip install django --upgrade

sudo mysql -u root -e "create database qadb;create user 'root';GRANT ALL ON * TO 'root';FLUSH PRIVILEGES;
"

