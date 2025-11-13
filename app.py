from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def handle_request():
    """
    מטפל בבקשות HTTP GET. 
    מחזיר 'OK' רק אם הפרמטר 'myparam' שווה ל-'11'.
    """
    
    param_name = 'myparam'
    # קבלת הערך של הפרמטר מחלק השאילתה (Query String) ב-URL
    input_value = request.args.get(param_name)
    
    # הגדרת ברירת המחדל (המחרוזת הארוכה)
    response_text = "read=t-חלק שני=myparam,,2,2,Number" 

    # יישום הלוגיקה ההפוכה:
    # אם הקלט שווה ל-"11"
    if input_value == "11":
        # מחזירים את התשובה הקצרה "OK"
        response_text = "OK"
        
    # החזרת התשובה כטקסט נקי
    return response_text, 200, {'Content-Type': 'text/plain; charset=utf-8'}
