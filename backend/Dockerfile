FROM python:3.11.4

WORKDIR /app

COPY src/requirements.txt .


RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt



COPY src/. .

EXPOSE 8000

CMD ["python", "main.py"]
