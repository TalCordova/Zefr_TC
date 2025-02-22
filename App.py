from fastapi import FastAPI, File, UploadFile
from PIL import Image
import io
import torch
from torchvision import transforms
from tinyvgg import TinyVGG


# Initialize FastAPI app
app = FastAPI()

# Load the full model
model = TinyVGG(input_channels=3, hidden_units=16, output_shape=1)

# Load the weights
model.load_state_dict(torch.load("model_weights.pth", map_location=torch.device("cpu")))
model.eval()


# Define preprocessing
preprocess = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
])

import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("api")

# Root route to verify the server is working
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app! Visit /docs to use the API."}

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    # Validate file type
    logger.info(f"Received file: {file.filename}")
    if file.content_type not in ["image/jpeg", "image/png"]:
        return {"error": "Invalid file type. Please upload a JPEG or PNG image."}

    try:
        # Load and preprocess the image
        image = Image.open(io.BytesIO(await file.read())).convert("RGB")
        input_tensor = preprocess(image).unsqueeze(0)  # Add batch dimension

        # Make prediction
        with torch.no_grad():
            logits = model(input_tensor)
            probabilities = round(torch.sigmoid(logits).item(), 4)  # Rounded probability
            prediction = int(probabilities > 0.5)

        return {"prediction": prediction, "probability": probabilities}
    except Exception as e:
        logger.error(f"Error processing file {file.filename}: {str(e)}")
        return {"error": str(e)}

# Run the app locally
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)