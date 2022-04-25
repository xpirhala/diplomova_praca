FROM ubuntu:latest
RUN apt-get update
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get install -y zlib1g-dev libjpeg-dev libwebp-dev libpng-dev libtiff5-dev
WORKDIR /app
ADD . /app

RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y python3-venv

RUN pip3 install -r requirements.txt

RUN apt-get update
RUN apt install -y libgl1-mesa-glx
RUN apt-get update && \
    apt-get install -y build-essential libzbar-dev && \
    pip install zbar
CMD ["uvicorn","app.main:app", "--host", "0.0.0.0","--port","8000"]