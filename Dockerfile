FROM python:3.4
ENV PYTHONUNBUFFERED 1
RUN mkdir /trackangle
WORKDIR /trackangle
ADD requirements.txt /trackangle/
RUN pip install -r requirements.txt
