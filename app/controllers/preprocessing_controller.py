
from flask import jsonify, request
import pandas as pd

from app.services.preprocessing_service import drop_missing_values, fill_missing_values
from app.utility.series import convert_to_list_of_dict


def handle_missing_value():
    data = request.get_json()
    print(data)
    #extract data
    method = data.get('method')
    value = data.get('value')
    series = data.get('series', [])
    
    if not all([method, series]):
        return jsonify({"message": "The data is malformed"}), 400

    #series->DataFrame obj
    df = pd.DataFrame(series)
    df.set_index('index', inplace=True)

    if method == "dropna":
        new_df =  drop_missing_values(df)
    elif method == "none":
        new_df = df; 
    else:
        new_df = fill_missing_values(df, method, value); 
            
    print('df', new_df)
    
    return jsonify({
        "message": "Processed successfully", 
        # "series": [{str(idx): val} for idx, val in new_df['value'].items()],
        "series": convert_to_list_of_dict(new_df) 
    }), 200