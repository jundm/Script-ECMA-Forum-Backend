FROM ubuntu:20.04

# Install python3
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && pip3 install --upgrade pip

COPY . /app
WORKDIR /app

RUN  pip3 install -r requirements.txt

EXPOSE 8000
CMD ["python3", "manage.py", "runserver","0.0.0.0:8000"]