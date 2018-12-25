FROM python:3.6-alpine

WORKDIR /var/app

COPY requirements.txt requirements.txt
RUN python --version
RUN python -m venv venv
RUN venv/bin/pip install --upgrade pip
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY migrations migrations
COPY bmw_rent_app.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP bmw_rent_app.py

EXPOSE 5000
ENTRYPOINT ["sh"]
CMD ["boot.sh"]
