FROM python:3.9

WORKDIR /app

COPY . .

RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

ENV PYTHONUNBUFFERED=1

CMD python manage.py collectstatic && python manage.py migrate