from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware 
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import io

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL_PATH = 'deface_detector.keras'
try:
    model = load_model(MODEL_PATH)
except Exception as e:
    raise RuntimeError(f"Lỗi load mô hình: {e}")

@app.post("/predict")
async def predict_deface(file: UploadFile):
    try:
        if not file.content_type.startswith('image/'):
            raise HTTPException(status_code=400, detail="File phải là ảnh!")
        
        content = await file.read()
        img = Image.open(io.BytesIO(content)).convert('RGB')
        img = img.resize((224, 224))
        img_array = np.array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        # Predict
        pred = model.predict(img_array, verbose=0)[0][0]
        result = "Normal" if pred > 0.5 else "Defaced"

        return {"filename": file.filename, "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi: {str(e)}")