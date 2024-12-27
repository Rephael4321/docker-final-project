FROM python:3.11-slim
WORKDIR /app
COPY main.py /app/
COPY printColors.py /app/
COPY config.json /app/
COPY requirements.txt /app/
RUN pip install -r requirements.txt
ENV HOST_IP=0.0.0.0
EXPOSE 80
CMD ["python", "main.py"]