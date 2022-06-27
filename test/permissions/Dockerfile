FROM ubuntu:20.04
RUN apt-get update && apt-get install python3-pip -y && pip3 install requests==2.27.1
RUN mkdir authentication
WORKDIR /authentication
ADD authentication.py /authentication/authentication.py
CMD ["python3" , "authentication.py"]
