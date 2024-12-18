# 🍷 ML Project: MLOps with MLflow and DAGsHub

Welcome to this wine-quality prediction project, where we combine the power of machine learning with modern MLOps practices! Using MLflow and DAGsHub, this project is designed to make your ML workflows seamless, collaborative, and efficient. Whether you're a beginner or an expert, dive in and make the most out of this cutting-edge stack! 🍇

## 🚀 Features

- **Experiment Tracking:** Monitor and manage your experiments with MLflow.
- **Version Control:** Collaborate effectively using DAGsHub.
- **FastAPI Web App:** Easily predict wine quality through a user-friendly interface.

## 🛠 Prerequisites

Before you start, make sure you have the following installed:

- Python (>=3.7)
- Git

## 📖 Setup Instructions

### 1. Clone the Repository

Begin by cloning the repository to your local machine:

```bash
git clone https://github.com/palassaha/Wine-Quality-Prediction
cd Wine-Quality-Prediction
```

### 2. Create a Virtual Environment

To ensure dependency isolation, create a virtual environment:

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

Activate your virtual environment:

- **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

### 4. Install Requirements

Install all necessary dependencies:

```bash
pip install -r requirements.txt
```

### 5. Run the Application

Launch the application by executing:

```bash
python app.py
```

Your app is now live at [http://127.0.0.1:8080](http://127.0.0.1:8080)! 🎉

### 6. Train the Model

Train the model by navigating to:

```
http://127.0.0.1:8080/train
```

Alternatively, you can train the model by running:

```
python main.py
```


This will trigger the training pipeline and prepare your model for predictions. 🏋️‍♂️ After training, an artifacts folder will be generated, containing the `model.joblib` file along with detailed metrics and performance scores of the trained model.

### 7. Make Predictions

Head to the homepage, input the necessary wine features, and click **Predict** to see the wine quality score instantly! 🍷

### 8. Retrain the Model

Want to tweak the model? Simply edit the parameters in the `params.yaml` file and retrain for improved results. 💡

## 📌 Next Steps

Stay tuned for instructions on deployment, advanced usage, and scaling this project for production!

---

Happy predicting! 🌟

