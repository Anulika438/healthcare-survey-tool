# Healthcare Survey Tool - Income Spending Analysis

A web-based survey tool for collecting and analyzing healthcare spending patterns, developed for healthcare product development research.

## 📋 What This Project Does

- Collects survey data through a Flask web application
- Stores user information: Age, Gender, Income, and 5 expense categories
- Processes data using a Python User class
- Creates required visualizations in Jupyter notebook
- Exports charts for PowerPoint presentations

## 📁 Project Files
healthcare-survey-tool/
├── app.py                      # Flask web application
├── user_class.py               # Data processing class
├── survey_analysis.ipynb       # Jupyter notebook analysis
├── requirements.txt            # Python packages needed
├── README.md                   # This file
├── survey_data.csv            # Exported survey data
├── age_income_chart.png       # Chart 1 for PowerPoint
└── gender_spending_chart.png  # Chart 2 for PowerPoint

## 🚀 How to Run

1. **Install packages:**
   ```bash
   pip install -r requirements.txt

Start the web app:
bashpython app.py

Open browser:
http://localhost:5000

Fill out surveys and export CSV
Run analysis:
bashpython user_class.py

Open Jupyter notebook:

Open survey_analysis.ipynb in PyCharm
Run all cells



📊 Assignment Requirements Completed

✅ Flask Web Application: Survey form with age, gender, income, expenses
✅ Data Storage: CSV export functionality
✅ User Class: Python class that processes data and loops through CSV
✅ Jupyter Notebook: Loads CSV and performs analysis
✅ Required Visualizations:

Ages with highest income
Gender distribution across spending categories


✅ PowerPoint Charts: High-resolution PNG exports

🎯 How to Test

Run python app.py
Fill out 5-10 different surveys at http://localhost:5000
Export CSV from results page
Run python user_class.py to see analysis
Open Jupyter notebook and run all cells
Check that PNG chart files are created

📈 Charts Created

age_income_chart.png - Shows which ages have highest income
gender_spending_chart.png - Shows spending patterns by gender

These PNG files can be inserted directly into PowerPoint presentations.
🔧 Requirements
Flask==2.3.3
pandas==2.1.1
matplotlib==3.7.2
seaborn==0.12.2
jupyter==1.0.0
✅ Project Status: COMPLETE