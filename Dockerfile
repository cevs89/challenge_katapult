FROM python:3.8.2

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV DJANGO_SETTINGS_MODULE katapult.settings


COPY requirements/base.txt /code/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./applications /code/app

CMD ["python", "manage.py", "runserver", "0.0.0.0", "8000"]
