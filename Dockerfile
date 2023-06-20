# python image
FROM python:3.9-slim

# load requirements
COPY ./requirements.txt /requirements.txt

# install dependencies
RUN pip install -r /requirements.txt

# create directory for app
RUN mkdir /app

# set working directory
WORKDIR /app

# copy app to working directory

COPY ./src/script /app

ENV email="bene6@hotmail.de"
ENV iter_stop_parameter=60
ENV search_term='("GC content of" OR "G + C content of") AND bacterial[Title/Abstract]'


# run app
CMD ["python", "test_python.py"]