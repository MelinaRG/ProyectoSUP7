FROM python:3.7

EXPOSE 8080

# Upgrade pip and install requirements
COPY requirements.txt requirements.txt
RUN pip install -U pip
RUN pip install -r requirements.txt

# Copy app code and set working directory
COPY . .

# Run
ENTRYPOINT [“streamlit”, “run”, “TATools.py”, “–server.port=8080”, “–server.address=0.0.0.0”]