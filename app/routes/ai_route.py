#Run pip install flask-blueprint
from flask import Blueprint
from app.controllers import ai_controller

ai_bp = Blueprint('ai',__name__)

@ai_bp.post('/explain/forecast')
def explain_forecast():
    return ai_controller.explainForecast()

@ai_bp.get('/explain/test')
def testGen():
    return ai_controller.testGenerate()
