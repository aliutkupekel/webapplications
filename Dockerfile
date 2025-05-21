# 1. Choose the base Python image
FROM python:3.10-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy all project files into the container's working directory
COPY . .

# 4. Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 5. Expose the port Django will run on
EXPOSE 8000

# 6. Default command to start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
