FROM python:3.11

ADD requirements.txt /
RUN pip install -r /requirements.txt
ADD config.py /
ADD main.py /

ENTRYPOINT ["python","/main.py"]
