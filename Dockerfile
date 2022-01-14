FROM python:3.9 AS runtime

ADD requirements.txt /tmp/requirements.txt
RUN cat /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt


WORKDIR /app
RUN mkdir /app/static
ADD chad /app/chad
ADD manage.py /app/manage.py
ADD documentation /app/documentation

RUN python manage.py collectstatic

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "chad.wsgi:application"]
FROM runtime AS unittest

RUN pip install coverage

ADD tests /app/tests
ADD .coveragerc /app/.coveragerc

RUN chmod ugo+x /app/tests/test.sh

CMD ["/app/tests/test.sh"]