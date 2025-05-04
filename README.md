# 🌍 WHO Life Expectancy Predictor

A machine learning project that predicts the **life expectancy** of a country based on key health, economic, and social indicators from the **WHO Global Health Observatory** dataset.

---

## 📊 Features Used

This model considers the following features to estimate life expectancy:

- `Adult Mortality`: Probability of dying between 15 and 60 years per 1000 population.
- `Polio`: Polio (Pol3) immunization coverage among 1-year-olds (%).
- `Diphtheria`: DTP3 immunization coverage among 1-year-olds (%).
- `Alcohol`: Alcohol consumption (litres per capita).
- `Hepatitis B`: Hepatitis B immunization coverage among 1-year-olds (%).
- `Schooling`: Average number of years of schooling.
- `Infant Deaths`: Number of infant deaths per 1000 live births.
- `Measles`: Reported measles cases per 1000 population.
- `Under Five Deaths`: Deaths under age five per 1000 live births.
- `HIV/AIDS`: Deaths due to HIV/AIDS per 1000 population.
- `Thinness 1-19 Years`: Percentage of thinness in children aged 1–19.

---

## 📦 Tech Stack

- Python 🐍
- Pandas & NumPy for data handling
- Scikit-learn for modeling and preprocessing
- Streamlit for web app deployment
- Matplotlib & Seaborn for visualization

---

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/bhautik12345/WHO-Life-Expectancy-Predictor.git

2. **install dependencies**:
   ```bash
   pip install -r requirements.txt
3. **Run the Streamlit app**:
   ```bash
   streamlit run inference.py

