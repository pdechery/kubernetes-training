FROM python:3

WORKDIR app/

COPY app/app.py .

COPY app/requirements.txt .

RUN pip install -r requirements.txt

CMD ["flask", "run", "--host", "0.0.0.0"]
