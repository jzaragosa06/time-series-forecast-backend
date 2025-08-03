from flask import jsonify, request
import os
import json

from app.services.ai_service import generateResponse

def explainForecast():
    data = request.get_json()
    prompt = data.get('prompt', '')
    description = data.get('description')
    series = data.get('series', [])

    final_prompt = (
        f"You are an AI assistant analyzing forecast results.\n"
        f"data_description: {description}.\n"
        f"Prompt: {prompt}\n\n"
        f"Forecast Data:\n{json.dumps(series, indent=2)}"
    )

    response = generateResponse(final_prompt)

    try:
        return jsonify({"message": "Successfully generated", "explanation": response}), 200
    except Exception as e:
        print("error:", e)
        return jsonify({"error": str(e)}), 500