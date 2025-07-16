from flask import Blueprint, request, jsonify
from app.controllers import documentation_controller

documentation_bp = Blueprint('documentation', __name__)

@documentation_bp.get("/")
def documentation(): 
    return documentation_controller.documentation()