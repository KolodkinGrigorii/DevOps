FROM python:alpine

WORKDIR /server/devops

COPY . .

CMD ["python", "app.py"]