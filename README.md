# 🏠 Boston House Price Prediction

A Machine Learning web application that predicts Boston housing prices using a Linear Regression model built with Scikit-learn and deployed using Flask and Render.

## 🌐 Live Demo

https://bostonhousepricing-o53y.onrender.com

## 📂 GitHub Repository

https://github.com/ankit-akash/bostonhousepricing

---

## 📖 Project Overview

This project predicts the median value of owner-occupied homes in Boston based on various housing and locality features.

### The application demonstrates an end-to-end Machine Learning workflow:

- Data preprocessing
- Feature scaling using StandardScaler
- Linear Regression model training
- Model serialization using Pickle
- Flask web application development
- REST API creation
- Cloud deployment using Render

---

## 🛠️ Software & Tools Requirements

- GitHub Account
- Render Account
- Visual Studio Code (VS Code)
- Git

---

## 🚀 Tech Stack

### Machine Learning

- Scikit-learn
- NumPy
- Pandas

### Backend

- Flask
- Gunicorn

### Deployment

- Render

### Version Control

- Git
- GitHub

---

## 📊 Dataset Features

The model uses the following input features:

| Feature | Description                                          |
| ------- | ---------------------------------------------------- |
| CRIM    | Crime rate per capita                                |
| ZN      | Residential land zoned proportion                    |
| INDUS   | Non-retail business acres                            |
| CHAS    | Charles River dummy variable                         |
| NOX     | Nitric oxide concentration                           |
| RM      | Average number of rooms                              |
| AGE     | Proportion of owner-occupied units built before 1940 |
| DIS     | Distance to employment centers                       |
| RAD     | Accessibility to radial highways                     |
| TAX     | Property tax rate                                    |
| PTRATIO | Pupil-teacher ratio                                  |
| B       | Proportion of Black population                       |
| LSTAT   | Percentage of lower status population                |

---

## 📁 Project Structure

```text
bostonhousepricing/
│
├── app.py
├── requirements.txt
├── regmodel.pkl
├── scaler.pkl
├── templates/
│   └── home.html
├── LinearRegression_Project.ipynb
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/ankit-akash/bostonhousepricing.git
```

### Navigate to Project Directory

```bash
cd bostonhousepricing
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

---

## 🔌 API Usage (Postman)

### Endpoint

```http
POST /predict_api
```

### Sample Request

```json
{
  "data": {
    "CRIM": 0.00632,
    "ZN": 18.0,
    "INDUS": 2.31,
    "CHAS": 0.0,
    "NOX": 0.538,
    "RM": 6.575,
    "AGE": 65.2,
    "DIS": 4.09,
    "RAD": 1.0,
    "TAX": 296,
    "PTRATIO": 15.3,
    "B": 396.9,
    "LSTAT": 4.98
  }
}
```

---

## 📸 Application Screenshot

Add your screenshot here:

```markdown
![Homepage](screenshots/homepage.png)
```

---

## 🎯 Learning Outcomes

- Data preprocessing and feature scaling
- Linear Regression model development
- Model serialization using Pickle
- Flask web application development
- REST API implementation
- Git & GitHub workflow
- Deployment using Render

---

## 👨‍💻 Author

**Ankit Akash**

GitHub: https://github.com/ankit-akash

---

⭐ If you found this project useful, consider giving it a star!
