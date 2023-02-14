FROM python:3.11-slim
WORKDIR /code
COPY . .
RUN mkdir /var/html
RUN pip install --upgrade pip && pip install -r requirements.txt
ENTRYPOINT ["sh", "entrypoint.sh"]
