#Specifying a base image
FROM python:alpine

#Install deps
WORKDIR /home/mcontainers
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . . 

# Default command
CMD ["python","server.py"]