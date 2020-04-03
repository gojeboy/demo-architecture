FROM python

RUN apt-get install libpq-dev
RUN pip install psycopg2


RUN pip3 install --upgrade pip
# RUN apt-get install 
WORKDIR /app

COPY . /app

RUN pip3 --no-cache install -r requirements.txt

RUN ls


ENTRYPOINT [ "./run.sh"]