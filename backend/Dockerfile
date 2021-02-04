FROM tiangolo/uvicorn-gunicorn:python3.8
LABEL maintainer="Sebastian Ramirez <tiangolo@gmail.com>"

WORKDIR /backend
COPY ./requirements.txt /backend/requirements.txt

RUN pip install --upgrade pip setuptools wheel && pip install -r /backend/requirements.txt && rm -rf /root/.cache/pip

COPY . /backend
WORKDIR /backend/api

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]