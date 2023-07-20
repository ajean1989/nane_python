FROM python:3.9

ENV FLASK_APP=app.py
ENV FLASK_ENV=dev

WORKDIR /nane

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

COPY . . 

WORKDIR /nane/app

CMD ["flask", "run", "--host=0.0.0.0", "--debug"]
