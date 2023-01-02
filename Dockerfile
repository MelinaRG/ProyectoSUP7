FROM tiangolo/uvicorn-gunicorn-fastapi
RUN pip install peewee
RUN pip install aiofiles
RUN pip install pandas
RUN pip install jinja2==3.0.3
RUN pip install psycopg2-binary
RUN pip install python-multipart
RUN pip install fastapi_login   
COPY ./app /app