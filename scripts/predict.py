from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import sys

def predict_image(path):
    model = load_model('breast_cancer_model.h5')
    img = Image.open(path).convert('RGB')
    img = img.resize((128, 128))
    img_array = np.array(img).astype('float32') / 255.0
    img_array = img_array.reshape(1, 128, 128, 3)
    pred = model.predict(img_array)[0][0]
    label = "Malignant" if pred > 0.5 else "Benign"
    confidence = round(pred if pred > 0.5 else 1 - pred, 2)
    print(f"Prediction: {label} ({confidence * 100:.2f}% confidence)")

# Usage: python predict.py path/to/image.png
if __name__ == "__main__":
    predict_image(sys.argv[1])