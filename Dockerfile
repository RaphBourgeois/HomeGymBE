
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
EXPOSE 5000
#RUN uvicorn src.main:app --reload --host 0.0.0.0 --port 5000
CMD ["uvicorn", "src.main:app", "--reload", "--host", "0.0.0.0", "--port", "5000"]
#CMD ["uvicorn", "run", "src.main.py", "--host", "0.0.0.0", "--port", "5000"]