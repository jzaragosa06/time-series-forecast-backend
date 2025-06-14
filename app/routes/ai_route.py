#Run pip install flask-blueprint
from flask import Blueprint
ai_bp = Blueprint('ai_bp',__name__)

@ai_bp.get('/')
def ai_info():
    return

@ai_bp.post('/explain/forecast')
def explain_forecast():
    return


@ai_bp.post('/explain/series')
def explain_series():
    return