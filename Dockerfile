FROM   python:latest


WORKDIR /src



COPY ./requrements.txt/src



RUN pip install -r requrements.txt


COPY . .


CMD ["uvicorn","main.py:app","--host","8000"]
