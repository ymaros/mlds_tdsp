from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.inception_v3 import InceptionV3, preprocess_input
import numpy as np
import pickle
import uvicorn
import tempfile
import os
from model_loader import load_caption_model

class ImageCaptioner:
    def __init__(self):
        self.caption_model = None
        self.tokenizer = None
        self.inception_model = None
        self.initialize_models()

    def initialize_models(self):
        """Initialize all required models"""
        print("Loading caption model...")
        model_path = '../../src/models/caption_model.keras'
        weights_path = '../../src/models/weights/caption_model.weights.h5'
        self.caption_model = load_caption_model(model_path, weights_path)
        
        print("Loading tokenizer...")
        with open('../../src/models/tokenizer.pkl', 'rb') as f:
            self.tokenizer = pickle.load(f)
        
        print("Setting up InceptionV3...")
        base_model = InceptionV3(weights='imagenet', input_shape=(299, 299, 3))
        base_model.layers.pop()
        self.inception_model = tf.keras.Model(inputs=base_model.inputs, 
                                            outputs=base_model.layers[-2].output)

    def extract_features(self, image_path):
        """Extract features from image using InceptionV3"""
        img = load_img(image_path, target_size=(299, 299))
        img_array = img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)
        features = self.inception_model.predict(img_array, verbose=0)
        return features

    def generate_caption(self, image_path):
        """Generate caption for the given image"""
        # Extract features
        features = self.extract_features(image_path)
        
        # Initialize sequence with start token
        in_text = 'start'
        max_length = 34
        
        # Generate caption word by word
        for _ in range(max_length):
            sequence = self.tokenizer.texts_to_sequences([in_text])[0]
            sequence = tf.keras.preprocessing.sequence.pad_sequences(
                [sequence], maxlen=max_length)
            yhat = self.caption_model.predict(
                [features.reshape(1, 2048), sequence], verbose=0)
            word_idx = np.argmax(yhat)
            
            word = None
            for word, index in self.tokenizer.word_index.items():
                if index == word_idx:
                    break
                    
            if word is None:
                break
                
            in_text += ' ' + word
            if word == 'end':
                break
        
        final_caption = in_text.replace('start ', '').replace(' end', '')
        return final_caption

# Initialize FastAPI
app = FastAPI(
    title="Image Captioning API",
    description="API for generating captions from images using a deep learning model",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the captioner at startup
captioner = None

@app.on_event("startup")
async def startup_event():
    global captioner
    captioner = ImageCaptioner()
    print("Captioner initialized successfully!")

@app.post("/generate-caption/")
async def generate_caption(file: UploadFile = File(...)):
    """Generate a caption for the uploaded image"""
    try:
        # Verify file is an image
        if not file.content_type.startswith('image/'):
            raise HTTPException(status_code=400, detail="File uploaded is not an image")

        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as temp_file:
            contents = await file.read()
            temp_file.write(contents)
            temp_file_path = temp_file.name

        try:
            # Generate caption
            caption = captioner.generate_caption(temp_file_path)
            
            return JSONResponse(content={
                "filename": file.filename,
                "caption": caption
            })
            
        finally:
            # Clean up
            os.unlink(temp_file_path)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    """Check if the API is running and models are loaded"""
    return {
        "status": "healthy",
        "models_loaded": captioner is not None
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)