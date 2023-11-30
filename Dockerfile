FROM python:3.9

RUN mkdir /DG
COPY . /DG/
WORKDIR /DG

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "127.0.0.1:8000"]