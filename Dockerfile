FROM python:3.12
COPY . /mbm
WORKDIR /mbm
RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver"]

