sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/nginx.conf
sudo /etc/init.d/nginx restart
sudo /etc/init.d/gunicorn stop
sudo gunicorn /home/box/web/hello.py -D
