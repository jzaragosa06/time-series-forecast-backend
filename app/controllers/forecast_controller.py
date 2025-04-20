from flask import jsonify

def info():
    return jsonify({
        "message": "ts forecast info", 
    })