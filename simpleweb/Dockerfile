#Specifying a base image
FROM python:alpine

#Install deps
WORKDIR /home/
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY server.py server.py 

# Default command
CMD ["python","server.py"]