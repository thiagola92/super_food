FROM python:3.7.3

WORKDIR /tmp

ADD requirements.txt .
RUN pip install -r requirements.txt

RUN apt update
RUN apt install vim -y

ADD . .

ENTRYPOINT ["bash"]