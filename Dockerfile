FROM python:latest
RUN mkdir /web_django
WORKDIR /web_django
COPY requirements.txt /web_django/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . .
EXPOSE 80
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]