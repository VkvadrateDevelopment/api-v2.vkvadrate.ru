FROM python:3.12
COPY . .
RUN pip install --default-timeout=100 requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]