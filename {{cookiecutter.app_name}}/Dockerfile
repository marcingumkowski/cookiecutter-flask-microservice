FROM ubuntu:16.04
RUN apt-get update -y
RUN apt-get install -y software-properties-common python-software-properties
RUN add-apt-repository ppa:jonathonf/python-3.6
RUN apt-get update \
  && apt-get install -y python3-pip docker.io python3.6 python3.6-dev  \
  && cd /usr/local/bin \
  && echo 'alias python="/usr/bin/python3.6"' >> ~/.bashrc
RUN python -m pip install --upgrade pip
COPY . /app
WORKDIR /app
RUN python -m pip install -r requirements.txt
CMD ["python","service/{{cookiecutter.service_name}}.py"]
