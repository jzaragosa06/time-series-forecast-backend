from flask import Blueprint, request, jsonify
from app.controllers import forecast_controller

forecast_bp = Blueprint("forecast", __name__)

@forecast_bp.get("/")
def info():
    return forecast_controller.info()

@forecast_bp.post("/univariate")
def forecast():
    return forecast_controller.forecast()