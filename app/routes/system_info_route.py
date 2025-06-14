from flask import Blueprint, request, jsonify
from app.controllers import system_info_controller

system_info_bp = Blueprint("system_info", __name__)

@system_info_bp.get("/")
def system_info(): 
    return system_info_controller.system_info()