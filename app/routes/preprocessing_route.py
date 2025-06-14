from flask import Blueprint, request
from app.controllers import preprocessing_controller
preprocess_bp = Blueprint('blueprint',__name__)

@preprocess_bp.post('/check-index')
def check_index():
    return

@preprocess_bp.post('/check-value')
def check_value():
    return

@preprocess_bp.post('/handle-missing-values')
def handle_missing_value():
    return preprocessing_controller.handle_missing_value()

