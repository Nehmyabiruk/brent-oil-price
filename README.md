Final Submission: Brent Oil Price Change Point Analysis
Overview
This repository contains the final submission for the 10 Academy Week 10 challenge, analyzing Brent oil price change points using Bayesian methods and presenting results via a Flask-React dashboard.
Structure

data/: Datasets including BrentOilPrices.csv, Events.csv, and preprocessed data.
src/: Scripts for preprocessing (preprocessing.py), Bayesian modeling (bayesian_model.py), and dashboard (app/).
plots/: EDA and model output plots.
Final_Report.pdf: Comprehensive analysis report.
Blog_Post.md: Non-technical summary for stakeholders.

Setup
pip install pandas numpy matplotlib pymc arviz flask
cd src/app/backend
python app.py
# In another terminal
cd src/app/frontend
npm install
npm start

Results
The analysis identified key change points aligned with events like the 2014 OPEC decision, 2020 COVID-19 crash, and 2022 Russia-Ukraine conflict.
