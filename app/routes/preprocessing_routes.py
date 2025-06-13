from flask import Blueprint
clean_bp = Blueprint('blueprint',__name__)

@clean_bp.post('/check-index')
def check_index():
    return

@clean_bp.post('/check-value')
def check_value():
    return

@clean_bp.post('/fill-missing')
def fill_missing():
    return

