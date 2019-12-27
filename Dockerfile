FROM python:3-slim

COPY . /
WORKDIR /

RUN chmod 444 main.py

ENTRYPOINT ["python", "main.py"]
CMD ["abcde", "0"]
