import base64
from fastapi import FastAPI
import os
from pydantic import BaseModel, Field
import uuid

class InputImage(BaseModel):
    img: str = Field(
        title="Base64 encoded image"
    )

app = FastAPI()

def decode_img_b64(encoded_img: str):
    try:
        os.makedirs("images", exist_ok=True)
        img_bytes = base64.b64decode(encoded_img)
        path = f"images/{uuid.uuid1()}.jpg"
        with open(path, "wb") as imgfile:
            imgfile.write(img_bytes)
        print(f"Image '{path}' have been saved")
    except Exception as e:
        print("An error ocurred while decoding and saving image.")
        print(repr(e))
        raise
    return path

def delete_image(path: str):
    try:
        os.remove(path)
        print(f"Image '{path}' removed successfully")
    except Exception as e:
        print(f"An error ocurred while removing the image '{path}'.")
        print(repr(e))
        raise

@app.get("/")
def app_status():
    return {
        "status": "App is online!"
    }

@app.post("/caption_image")
def caption_image(data: InputImage):
    path = decode_img_b64(data.img)
    # Predict
    delete_image(path)    
    return {
        "status": "Image processed successfully",
        "caption": "this is just a test"
    }