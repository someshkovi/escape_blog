FROM python:3
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN pip install -r requriements.txt
CMD [ "pyton3", "src/manage.py", "0.0.0.0:8000"]