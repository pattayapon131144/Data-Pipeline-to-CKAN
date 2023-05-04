FROM python:3.8
WORKDIR /code
COPY . .
COPY requirement.txt  requirement.txt
RUN pip install -r /code/requirement.txt
COPY . .
CMD ["python", "scripy.py"]


