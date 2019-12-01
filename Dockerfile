FROM python:3.7

ADD . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["/Database/Create.py"]
CMD ["/Database/Populate.py"]
CMD ["/Database/Query.py"]