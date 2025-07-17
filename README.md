# Backend for Automated Time Series Forecasting

This repository contains the **simplified backend** for my capstone project:  
**_“Automated Time Series Forecasting: Using Hybrid Forecasting Approach.”_**

 <p>
    Refer to this link for the <a href="https://drive.google.com/file/d/1ezv9vKa8NNZ1Isd4c1vs9Tl0QWcCdldI/view?usp=sharing"> research's extended abstract. </a> You can read the <a href="https://www.linkedin.com/in/jun-jun-zaragosa/details/projects/"> full document </a> and explore my other projects.
</p>

Originally, the full system was implemented using **PHP’s Laravel framework** (serving Blade templates) alongside a dedicated **Python Flask application** for the core forecasting logic.  

For this simplified version, I’ve rewritten the backend with a clean separation between backend and frontend:  
- **Frontend:** React.js  
- **Backend:** Python Flask (lightweight and fast for development)

---

## Overview
This backend powers the key features of the original capstone project. It focuses on:
- Preprocessing univariate time series data
- Validating time series inputs
- Generating forecasts using a **hybrid forecasting model**

---

## Researchers Behind the Original Study
- **Paulet Crysline Pajo** – Project Leader  
- **Jun Jun M. Zaragosa** – Lead Programmer  
- Leynard Guinumtad  
- Janeil Capales  
- Camile Marticio  
- Jann Daerick Finulliar  

---

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Documentation / Welcome page |
| `/api/system-info` | GET | Returns information about the running application |
| `/api/preprocess/handle-missing-values` | POST | Perform preprocessing on univariate time series (handles missing values) |
| `/api/preprocess/check-series` | POST | Validate if a given series is valid (univariate) |
| `/api/forecast` | GET | Get information about the forecast model (algorithmic framework) |
| `/api/forecast/univariate` | POST | Perform **n‑step** forecast using the hybrid model |

---

## Tech Stack
- **Backend:** Python, Flask  
- **Frontend:** React.js (separate repository)  
- **Original System:** PHP (Laravel) + Python (Flask)  

---

## 📂 Project Structure (Backend)
backend/
├── app/ # Core Flask application
├── api/ # API route definitions
├── models/ # Forecasting models and utilities
├── requirements.txt # Python dependencies
└── README.md # This file

---

## About the Study
This backend is a **simplified version** of a more extensive system developed for the study:  
**Automated Time Series Forecasting: Using Hybrid Forecasting Approach.**  
It demonstrates how to preprocess, validate, and forecast time series data efficiently.
