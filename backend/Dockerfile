FROM ubuntu
FROM python:3.6

RUN apt-get update && apt-get install libpq-dev -y

WORKDIR /var/app

COPY requirements.txt requirements.txt
RUN python --version
RUN python -m venv venv
RUN venv/bin/pip install --upgrade pip
RUN venv/bin/pip install -r requirements.txt

COPY app app
COPY bmw_rent_app.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP bmw_rent_app.py

EXPOSE 5000
ENTRYPOINT ["bash"]
CMD ["boot.sh"]
