FROM python:3
LABEL Name="Python Tensorflow Demo App" Version=1.1.0 
ARG port=5000
ENV PORT=$port

WORKDIR /
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY hello_tensorflow.py .

EXPOSE $port

CMD ["python", "hello_tensorflow.py"]

