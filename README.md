Breast Cancer Detection using Deep Learning

This project applies deep learning techniques (CNN) to detect and classify breast cancer using histopathological images from the [BreaKHis dataset](https://www.kaggle.com/datasets/ambarish/breakhis).

##  Objective

To build a CNN-based classification model that can distinguish between benign and malignant breast cancer tissue images using the BreaKHis dataset.

---

## 📂 Project Structure

breast_cancer_detection/
├── notebooks/             # Jupyter notebooks for training, EDA, evaluation
│   └── main.ipynb
├── model/                 # Saved models (.h5) - not pushed to Git
├── requirements.txt       # Python dependencies
├── README.md              # Project overview
├── .gitignore             # Ignoring large or unnecessary files
└── BreaKHis_v1/           # [Ignored] Original dataset directory (not uploaded)

---

## Dataset

- **Name**: BreaKHis
- **Classes**: Benign, Malignant
- **Image sizes**: 40x, 100x, 200x, 400x magnification
- **Note**: Dataset is too large for GitHub and should be downloaded manually.

 Download from [Kaggle](https://www.kaggle.com/datasets/ambarish/breakhis)

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yashas2604/breast-cancer-detection.git
   cd breast-cancer-detection

2.	Install dependencies:
   pip install -r requirements.txt
