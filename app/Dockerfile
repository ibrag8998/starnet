FROM python:3.9

# initial

ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1 PORT=80

EXPOSE 80

WORKDIR /app/

# install pipenv

RUN pip install pipenv==2020.11.15

# entrypoint setup

COPY ./entrypoint.sh ./

RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["sh", "./entrypoint.sh"]

# dependencies

COPY ./Pipfile* ./

RUN pipenv install --system --dev

# final

COPY . ./

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
