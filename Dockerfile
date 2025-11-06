# 1️⃣ Use a lightweight Python image
FROM python:3.10-slim

# 2️⃣ Set the working directory inside the container
WORKDIR /app

# 3️⃣ Copy your dependency file
COPY requirements.txt .

# 4️⃣ Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 5️⃣ Copy your app code and model into the container
COPY app.py .
COPY pipeline.pkl .

# 6️⃣ Expose port 5000 (the port Flask/Gunicorn will use)
EXPOSE 5000

# 7️⃣ Start the web server (Gunicorn)
CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:5000", "app:app"]
