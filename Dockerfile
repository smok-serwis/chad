FROM python:3.9

ADD requirements.txt /tmp/requirements.txt
RUN pip install -f /tmp/requirements.txt


WORKDIR /app
RUN mkdir /app/static
ADD chad /app/chad
ADD manage.py /app/manage.py


CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "chad.wsgi:application"]
