# /etc/nginx/sites-available/pbp

server {
    server_name paintballparkscz.test www.paintballparkscz.test;

    location = /favicon.ico { 
        access_log off; 
        log_not_found off; 
        }

    location /static/ {
        autoindex on;
        root /home/gonzalo/pbp/staticfiles/;
        }
    
    location /media/ {
        autoindex on;
        root /home/gonzalo/pbp/media/;
        }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/pbp.sock;
    }
}
