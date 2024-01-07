From jupyter/basenotebook:v1

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt