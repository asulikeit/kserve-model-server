FROM asulikeit/kserve-temp:0.1.0

WORKDIR /app

COPY model_server.py .

ENTRYPOINT ["python", "model_server.py"]
