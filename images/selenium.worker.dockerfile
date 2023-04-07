FROM python:alpine3.17

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/home

RUN mkdir -p ./www ./src

RUN pip install requests selenium pytest behave robotframework html-testrunner beautifulsoup4 behave-html-formatter

ENTRYPOINT ["python3", "./src/start.py"]