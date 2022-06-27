FROM ubuntu:20.04
RUN apt-get update && apt-get install python3-pip -y && pip3 install requests==2.27.1
RUN mkdir test
WORKDIR /test
ADD test.py /test/test.py
CMD ["python3", "/test/test.py"]
