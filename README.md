# Zefr_TC

Tal Cordova

talcordova56@gmail.com

0504971013

This is the data scientise role assignment for Zefr.

## Logo Detection API with FastAPI

This project demonstrates a logo detection model deployed using FastAPI. The model predicts whether a given image contains a target brand logo.

### Repository Contents
- `App.py`: FastAPI app to serve the model.
- `tinyvgg.py`: Model architecture (TinyVGG).
- `model_weights.pth`: Trained model weights.
- `requirements.txt`: Dependencies to run the app.
- `Zefr_DS_Tal_Cordova.ipynb`: Jupyter notebook used for training the model.

### Data Used

For the model development, I used [this dataset](https://universe.roboflow.com/raveesh-gupta/logo-dataset-3itmd).

### Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Zefr_TC.git
   cd Zefr_TC
2. **Create and Activate a Virtual Environment**: create a virtual environment to isolate dependencies:
   ```bash
   python -m venv venv
   ```
    Activate the virtual environment:
    * **On Windows**:
    ```bash
    venv\Scripts\activate
    ```
    * **On Linux/Mac**:
    ```bash
    source venv/bin/activate
    ```
3. **Install Dependencies** - Install the required Python packages listed in `requirements.txt`:
  ```bash
  pip install -r requirements.txt
  ```
4. **Run the App** - Start the FastAPI server locally:
  ```bash
  uvicorn App:app --reload
  ```
5. Test the API:
   Open your browser and navigate to:
  * Swagger UI: http://127.0.0.1:8000/docs


Use the /predict/ endpoint to upload an image and get predictions.

### Cloud Deployment

I deployed the model using AWS simple EC2 instance.

It is accesible here:

* Swagger UI: http://34.228.116.129:8000/docs

Using Swagger UI:

1. Navigate to the link provided above.

2. Explore the endpoints available on the Swagger UI.

3. Use the /predict/ endpoint to upload an image file and receive predictions from the model.

If there are any question - feel free to contact me.
