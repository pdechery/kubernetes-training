FROM python:3

WORKDIR app/

COPY app.py .

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["flask", "run", "--host", "0.0.0.0"]
