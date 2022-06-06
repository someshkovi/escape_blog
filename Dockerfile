FROM python:3
ENV HOME=/usr/src/app

COPY . /usr/src/app
WORKDIR /usr/src/app

# install dependencies  
RUN pip install --upgrade pip
RUN pip install -r requriements.txt
CMD [ "pyton3", "src/manage.py", "0.0.0.0:8000"]