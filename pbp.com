# /etc/nginx/sites-available/pbp

server {
    server_name paintballparkscz.com www.paintballparkscz.com;

    location = /favicon.ico { 
        access_log off; 
        log_not_found off; 
        }

    location /static/ {
        autoindex on;
        root /root/pbp/staticfiles/;
        }
    
    location /media/ {
        autoindex on;
        root /root/pbp/media/;
        }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/pbp.sock;
    }
}
