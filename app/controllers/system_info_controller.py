from flask import jsonify
import platform

def system_info():
    return jsonify({
        "title": "Automated time series forecast for Univariate time series",
        "description": "Forecast univariate time series (with index or without index)",
        "api_version": "0.0.1",
        "python_version": platform.python_version(),
        "system": platform.uname().system,
        }
    )