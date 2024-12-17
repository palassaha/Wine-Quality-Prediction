from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn
import os
import numpy as np
from src.ML_Project.pipeline.prediction import PredictionPipeline


app = FastAPI()

templates = Jinja2Templates(directory = "templates")

# Serve static files (if needed for CSS/JS)
app.mount("/static", StaticFiles(directory = "static"), name = "static")

@app.get("/", response_class = HTMLResponse)
async def home_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/train", response_class = HTMLResponse)
async def training_pipeline():
    os.system("python main.py")
    return "Training Successful!"

@app.post("/predict", response_class = HTMLResponse)
async def predict(
    request: Request,
    fixed_acidity: float = Form(...),
    volatile_acidity: float = Form(...),
    citric_acid: float = Form(...),
    residual_sugar: float = Form(...),
    chlorides: float = Form(...),
    free_sulfur_dioxide: float = Form(...),
    total_sulfur_dioxide: float = Form(...),
    density: float = Form(...),
    pH: float = Form(...),
    sulphates: float = Form(...),
    alcohol: float = Form(...),
):

    try:
        data = [
            fixed_acidity,
            volatile_acidity,
            citric_acid,
            residual_sugar,
            chlorides,
            free_sulfur_dioxide,
            total_sulfur_dioxide,
            density,
            pH,
            sulphates,
            alcohol,
        ]
        data = np.array(data).reshape(1, 11)

        obj = PredictionPipeline()
        prediction = obj.predict(data)

        return templates.TemplateResponse(
            "results.html", {"request": request, "prediction": str(prediction)}
        )
    
    except Exception as e:
        print("The Exception message is:", e)
        return HTMLResponse(content = "Something went wrong", status_code = 500)
    
# if __name__ == "__main__":
#     uvicorn.run("app:app")