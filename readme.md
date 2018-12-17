# Django WOL Web

After looking for a simple Wake-on-Lan web service and coming up with nothing, I decided to just build my own. I am using django for this project, simply because I have written projects with django before, and it works.

## Run the application

In order for the container to reach your PC, it needs host level access to your network. To do so, use ```--net=host``` when running your docker container.

In addition, for security purposes, it asks for a password when you try to use the WOL functionality or add a computer to the DB. This is simply a sha256 hash added as a environment variable. You can either generate this on the commandline, or using a site of your choice. Here is one https://tools.keycdn.com/sha256-online-generator

```
docker run -it -e "HASH=9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b822cd15d6c15b0f00a08" --net=host --hostname wol.example.com soarinferret/django-wol-web
```

## Using the Application

To add a computer, go to http://localhost/new and a page will show up to add a new computer.

If you want your computers to persistent across any updates, please backup the following locations using the ```-v``` docker argument:
```
/var/www/html/django-wol/db.sqlite3
/var/www/html/django-wol/wol/migrations
```

## Building and Testing
```
docker build -t testing .
docker run -it -e DEBUG='True' --name wol_test -p 8080:80 testing
```