FROM tiangolo/uvicorn-gunicorn-fastapi
RUN pip install uvicorn
EXPOSE 80
COPY . /app