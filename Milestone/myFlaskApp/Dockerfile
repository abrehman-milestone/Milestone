FROM python:3.10

EXPOSE 5000

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . /app/

# Set the default command to run the Flask app
CMD ["python", "app.py"]

