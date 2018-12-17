FROM ubuntu:latest

# Setup Environment
ENV PYTHONUNBUFFERED 1

# Tmp Env Vars for Django to run
ENV DEBUG False

# Install Dependencies
RUN apt-get update && apt-get install -y wakeonlan \
                                        inetutils-ping \
                                        python3 \
                                        python3-pip \
                                        apache2 \
                                        libapache2-mod-wsgi-py3

# Remove Temporary Files
RUN apt-get clean autoclean && \
    apt-get autoremove --yes && \
    rm -rf /var/lib/{apt,dpkg,cache,log}/

# Create link from pip to pip3 and python to python3
RUN ln -s /usr/bin/pip3 /usr/bin/pip
RUN ln -s /usr/bin/python3 /usr/bin/python

# Setup working directory
RUN mkdir /var/www/html/django-wol
WORKDIR /var/www/html/django-wol

# Install dependencies via pip
RUN pip install --upgrade pip
ADD requirements.txt /var/www/html/django-wol
RUN pip install -r requirements.txt

# Add django-wol-web
ADD django-wol /var/www/html/django-wol

# Add apache config
RUN echo hi
ADD apache.conf /etc/apache2/sites-available/000-default.conf

# Add start.sh
ADD start.sh /

EXPOSE 80
ENTRYPOINT [ "/start.sh"]
