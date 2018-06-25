FROM python:alpine
ADD . /usr/src/app
WORKDIR /usr/src/app
RUN mv settings.prod.py settings.py && pip install -r requirements.txt
EXPOSE 80
CMD ["python", "front.py"]
