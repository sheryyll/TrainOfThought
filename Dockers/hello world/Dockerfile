FROM python:3.8-alpine
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["flask", "--app", "app", "run", "--host=0.0.0.0"]