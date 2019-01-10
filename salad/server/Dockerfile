FROM rodrigoibka/backend:1.0

ENV DEBIAN_FRONTEND noninteractive
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

# -- Install Application into container:
RUN mkdir /app

WORKDIR /app

COPY ./ /app/

# -- Install dependencies:
RUN pipenv install --deploy --system

EXPOSE 8080
ENTRYPOINT ["gunicorn", "-c", "gunicorn.py", "server:app"]
