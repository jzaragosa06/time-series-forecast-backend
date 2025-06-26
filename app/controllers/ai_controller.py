from flask import jsonify, request
import os
import json

from app.services.ai_service import generateResponse

def explainForecast():
    data = request.get_json()
    prompt = data.get('prompt', '')
    series_context = data.get('series_contex')
    series = data.get('series', [])


    try:
        return jsonify({"message": "okay"})
    except Exception as e:
        print("error:", e)
        return jsonify({"error": str(e)}), 500

def testGenerate():
    return jsonify({"response": generateResponse()})