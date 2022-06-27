FROM ubuntu:20.04
RUN mkdir /project
WORKDIR /project
COPY requirements.txt .
RUN apt-get update && apt-get install python3-pip -y && pip3 install -r requirements.txt
ADD preprocessing.py /project/preprocessing.py
ADD model.sav /project/model.sav
ADD model_nb.sav /project/model_nb.sav
ADD api.py /project/api.py
CMD uvicorn api:api --host 0.0.0.0 --port 8000


