FROM python:3.9.7

WORKDIR /app

RUN pip install git+https://github.com/maistodos/python-creditcard.git@main

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD alembic upgrade head && \
  uvicorn main:app --host 0.0.0.0 --port 8000 --reload
