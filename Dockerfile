
ARG PYTHON_VERSION=3.11.4
FROM python:${PYTHON_VERSION}-slim as base

RUN mkdir app
WORKDIR /app

ENV PATH="${PATH}:/root/.local/bin"
ENV PYTHONPATH=.


COPY requirements.txt .


RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY src/ .

CMD ["fastapi", "run", "app/main.py", "--port", "8777"]