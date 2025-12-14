# 🏠 House Price Predictor

A machine learning web application that predicts house prices based on key features like size, bedrooms, location quality, and age.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange.svg)

## 🚀 Live Demo

**[Try the app here!](https://housepricepredictor-h4bavwkg9dnrajclotiuqp.streamlit.app/)**

## 📊 Features

- **Interactive Interface**: Easy-to-use sliders and input fields
- **Real-time Predictions**: Instant price estimates based on house features
- **Confidence Intervals**: Shows typical price range (±10%)
- **Transparent Model**: View the exact inputs used for prediction

## 🛠️ Technologies Used

- **Python 3.8+**: Core programming language
- **Pandas**: Data manipulation and analysis
- **scikit-learn**: Machine learning model (Random Forest Regressor)
- **Streamlit**: Web application framework
- **NumPy**: Numerical computations

## 📈 Model Details

- **Algorithm**: Linear Regression / Random Forest Regressor
- **Training Data**: 1000+ houses with features like size, bedrooms, bathrooms, age, garage, location quality
- **Accuracy**: R² score of ~0.95 (model explains 95% of price variance)
- **RMSE**: Average prediction error of $X,XXX

## 🏗️ Project Structure
```
house-price-predictor/
├── app.py                    # Streamlit web application
├── house_price_model.pkl     # Trained ML model
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
├── data/                     # Training data
└── notebooks/                # Data exploration & model training scripts
```

## 💻 Local Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Steps

1. **Clone the repository**
```bash
git clone https://github.com/kanavsaras/HousePricePredictor.git

cd house-price-predictor
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
streamlit run app.py
```

4. **Open your browser**
- The app will automatically open at `https://housepricepredictor-h4bavwkg9dnrajclotiuqp.streamlit.app/`

## 🎯 How to Use

1. **Enter house details**:
   - Size in square feet
   - Number of bedrooms and bathrooms
   - Age of the house
   - Location quality (1-10 scale)

2. **Click "Predict Price"**

3. **View results**:
   - Estimated price
   - Typical price range
   - Input summary

## 🧠 What I Learned

This project taught me:

- **Data Preparation**: Loading, cleaning, and exploring datasets
- **Feature Engineering**: Understanding which features impact house prices
- **Model Training**: Implementing and evaluating ML models
- **Model Deployment**: Creating interactive web apps with Streamlit
- **Version Control**: Managing code with Git and GitHub
- **Problem Solving**: Debugging issues like:
  - Handling indentation in Streamlit's reactive model
  - Ensuring logical predictions through proper data patterns
  - Managing variable scope in if blocks

## 🔮 Future Improvements

- [ ] Add more features (school ratings, crime rates, distance to amenities)
- [ ] Implement advanced models (XGBoost, Neural Networks)
- [ ] Add data visualization charts
- [ ] Include model explainability (SHAP values)
- [ ] Create API endpoints for integration
- [ ] Add user authentication for saving predictions
- [ ] Implement A/B testing for model versions



## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📧 Contact

**Your Name** - [kanavsaras@gmail.com](mailto:kanavsaras@gmail.com)

Project Link: [https://housepricepredictor-h4bavwkg9dnrajclotiuqp.streamlit.app/](https://github.com/kanavsaras/house-price-predictor)

---

⭐ **If you found this project helpful, please give it a star!**
