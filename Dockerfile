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

# run app
CMD ["python", "test_python.py"]