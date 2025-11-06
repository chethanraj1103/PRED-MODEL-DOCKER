🧠 Predictive Model API — Flask + Docker + Render








A clean, production-ready Machine Learning Prediction API built with Flask and scikit-learn, containerized using Docker, and deployed on Render. This project demonstrates a full end-to-end workflow — from training and saving a model to serving predictions through a live REST API.

🚀 Live Demo

🔗 https://pred-model-vy56.onrender.com

(Access the running API — returns prediction results for your input JSON.)

⚙️ Tech Stack
Layer	Technology
Language	Python 3.10
Framework	Flask
Machine Learning	scikit-learn
Model Serving	Flask REST API
Containerization	Docker
Deployment	Render (Cloud Hosting)
🔍 Endpoints
Method	Endpoint	Description
GET	/	Welcome route
GET	/health	Returns model load status
POST	/predict	Returns prediction result for given input
🧩 Example Usage
🔹 Request
curl -X POST "http://127.0.0.1:5000/predict" \
     -H "Content-Type: application/json" \
     -d '{"input": {"MedInc": 8.3252, "HouseAge": 41.0, "AveRooms": 6.98, "AveBedrms": 1.02, "Population": 322.0, "AveOccup": 2.55, "Latitude": 37.88, "Longitude": -122.23}}'

🔹 Response
{
  "n": 1,
  "predictions": [4.23]
}

🛠️ Run Locally (No Docker)
# Clone repo
git clone https://github.com/chethanraj1103/PRED-MODEL-DOCKER.git
cd PRED-MODEL-DOCKER

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run app
python app.py


Server will start at 👉 http://127.0.0.1:5000

🐳 Run with Docker
docker build -t pred-model-api .
docker run -p 5000:5000 pred-model-api


✅ Open your browser → http://127.0.0.1:5000

📦 Project Structure
PRED-MODEL-DOCKER/
│
├── app.py               # Flask application entry point
├── pipeline.pkl         # Trained ML model
├── requirements.txt     # Dependencies
├── Dockerfile           # Container setup
├── .gitignore           # Ignore unnecessary files
└── README.md            # Project documentation

📈 What This Project Demonstrates

Model training, serialization, and API serving

Flask-based RESTful service with validation

Containerization using Docker

Cloud deployment with Render

Local and production testing

🧑‍💻 Author

Chethan Raj B R
🔗 GitHub

🏷️ Topics

flask machine-learning api docker render deployment scikit-learn python mlops

💬 Next Steps (Optional Enhancements)

Add request logging (timestamp + prediction)

Include API-key authentication for secure access

Attach sample dataset and training notebook

Add a simple web UI for interactive predictions