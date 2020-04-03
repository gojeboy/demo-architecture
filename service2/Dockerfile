FROM python

RUN apt-get install libpq-dev
RUN pip install psycopg2

WORKDIR /usr/src/app
RUN mkdir app
COPY requirements.txt ./

COPY ./app ./app

COPY manage.py ./

RUN pip install --no-cache-dir -r requirements.txt

RUN ls

EXPOSE 5001

CMD ["python", "manage.py","run"]