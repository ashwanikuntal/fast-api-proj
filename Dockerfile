FROM python:3

COPY app ./app
COPY requirements.txt requirements.txt
COPY main.py main.py

RUN pip3 install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]

EXPOSE 8080