FROM python:3.7

ADD . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["/Database/Queries.py"]
CMD ["/Database/Queries2.py"]