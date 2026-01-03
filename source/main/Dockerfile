FROM python:3

COPY etc ./etc
RUN chmod 444 ./etc

WORKDIR /app

RUN pip3 install --no-cache-dir Flask lxml

COPY app.py ./app.py
COPY templates ./templates
COPY styles ./styles

EXPOSE 8000

CMD ["python", "app.py"]
