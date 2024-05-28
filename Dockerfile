FROM python:3.8-slim-buster

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt


# Expose the port that the app will be running on
EXPOSE 8501

# Set the entrypoint command to run the app.py file
CMD ["streamlit", "run", "--server.port", "8501", "app.py"]