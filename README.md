
# Multiple Disease Prediction

![License](https://img.shields.io/badge/license-MIT-green)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![Build Status](https://img.shields.io/github/workflow/status/SachinMhete678/multiple_disease_prediction/CI)

## Overview

**Multiple Disease Prediction** is an advanced machine learning application that predicts the likelihood of various diseases based on user inputs. The application currently supports predictions for:

- **Heart Disease**
- **Lung Cancer**
- **Diabetes**
- **Thyroid Disorders**

Built using cutting-edge models, this tool provides detailed predictions and interactive visualizations to help users understand their health risks.

### 🛠 Key Features

- **Disease Prediction**: Predict the risk of heart disease, lung cancer, diabetes, and thyroid disorders based on user data.
- **Interactive Visualizations**: View interactive charts and graphs to better understand prediction results.
- **Real-time Feedback**: Get instant predictions and insights.

## 🚀 Live Demo

Experience the application in action: [Try the Live Demo!](https://diseaseprediction-rxeokrq7eufo6vrdnhbxhd.streamlit.app/)


## 📦 Installation

### Clone the Repository

```bash
git clone https://github.com/SachinMhete678/multiple_disease_prediction.git
cd multiple_disease_prediction
```

### Set Up Your Environment

Create a virtual environment and install the required packages:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### Run the Application

Start the Streamlit app locally:

```bash
streamlit run app.py
```

## 🎯 Usage

1. **Input Data**: Use the interactive form to enter patient details.
2. **Select Disease**: Choose which disease you want to predict (Heart Disease, Lung Cancer, Diabetes, Thyroid).
3. **Submit**: Click on the "Predict" button to get results.
4. **View Results**: The prediction results will display probabilities for the selected disease along with interactive visualizations.

## 🧩 Disease Prediction Models

### Heart Disease
- **Model**: Logistic Regression
- **Features**: Age, Gender, Blood Pressure, Cholesterol levels, etc.

### Lung Cancer
- **Model**: Random Forest Classifier
- **Features**: Age, Smoking history, Cough duration, etc.

### Diabetes
- **Model**: Support Vector Machine (SVM)
- **Features**: Glucose level, Insulin level, BMI, etc.

### Thyroid Disorders
- **Model**: Gradient Boosting
- **Features**: Age, TSH levels, T3 levels, etc.

## ⚙️ Configuration

Modify model parameters or update the dataset in `config.yaml`. This file allows you to configure your models and data sources.

## 🧑‍💻 Development

To contribute to this project:

1. **Fork the Repository**
2. **Create a Branch**: `git checkout -b feature-branch`
3. **Commit Changes**: `git commit -am 'Add new feature'`
4. **Push to Branch**: `git push origin feature-branch`
5. **Open a Pull Request**

Refer to [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **[Streamlit](https://streamlit.io/)**: For creating easy-to-use interactive web apps.
- **[Scikit-learn](https://scikit-learn.org/)**: For robust machine learning algorithms.
- **[Pandas](https://pandas.pydata.org/)**: For efficient data manipulation.

## 📬 Contact

For questions or feedback, feel free to contact me at [your.email@example.com](mailto:sachinmhetre678@gmail.com).

