# Introduction

A container is a standardized software package that allows applications to run quickly and reliably in different computing environments​. A container packages up code and all its dependencies so applications can be easily deployed in different computer platforms. A container is created from a container image. A container engine runs containers​. Available for most popular platforms, containerized software will always run the same, regardless of the underlying infrastructure. 

Docker is a container image format and also a complete solution for software containerization. For this activity you will have to download docker desktop from [docs.docker.com/desktop](https://docs.docker.com/desktop). Docker hub [hub.docker.com](https://hub.docker.com) is a public repository of docker images that are available to use, currently with > 7M images. 

# Instructions

The image to be built will run the simple "Hello World!" web app described in [Activity 02: Flask Intro](https://classroom.github.com/a/O0-fFQSq). 

First create and activate a virtual environment, install flask, an generate a **requirements.txt** file using: 

```
pip3 freeze > requirements.txt
```

Deactivate the virtual environment and remove its folder. Next, create a **Dockerfile** with the following instructions to build a Docker image to run the app. 

```
FROM python:3.11
ADD app /app
WORKDIR /app
COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt
ENV FLASK_APP=/app
CMD ["flask", "run", "-h", "0.0.0.0"]
```

You can learn more about **Dockerfile** commands [here](https://phoenixnap.com/kb/wp-content/uploads/2021/04/Docker-commands-cheat-sheet-by-PhoenixNAP-scaled.jpg).

Generate the Docker image using: 

```
docker build -t helloworld .
```

Finally, run the **helloworld** image as a container using: 

```
docker run -i --name helloworld --publish 5000:5000 --rm helloworld
```

Test your web app using a browser and the link: [http://127.0.0.1:5000](http://127.0.0.1:5000).