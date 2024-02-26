FROM python:3.12-slim
COPY . .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000", "--proxy-headers"]