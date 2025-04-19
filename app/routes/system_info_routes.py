from flask import Blueprint, request, jsonify

system_info_bp = Blueprint("system_info", __name__)

@system_info_bp.get("/")
def system_info(): 
    return "TS forecast"