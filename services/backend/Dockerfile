FROM apache/spark:3.4.0-python3

WORKDIR /app

RUN wget --no-check-certificate https://jdbc.postgresql.org/download/postgresql-42.2.5.jar && \
    mv postgresql-42.2.5.jar /opt/spark/jars && \
    apt-get update && \
    apt-get install -y openjdk-11-jdk

COPY requirements.txt .
RUN pip3 install -r requirements.txt

RUN pip install --upgrade pip


COPY src/ .


