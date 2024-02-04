FROM python:3

WORKDIR /app

COPY requirements.txt .
COPY ./templates/index.html .
COPY main.py .


RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py" ]
