FROM python:3.7.3

WORKDIR /tmp

ADD requirements.txt
RUN pip install -r requirements.txt

ADD . .

ENTRYPOINT ["python", "/tmp/run.py"]