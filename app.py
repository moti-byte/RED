from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def handle_request():
    """
    מטפל בבקשות HTTP GET. 
    מחפש פרמטר בשם 'myparam' ומחזיר מחרוזת מותאמת אישית אם הערך הוא '11'.
    """
    
    # 1. הגדרת שם הפרמטר
    param_name = 'myparam'
    
    # 2. קבלת הערך של הפרמטר מחלק השאילתה (Query String) ב-URL
    # אם myparam לא קיים, input_value יהיה None
    input_value = request.args.get(param_name)
    
    response_text = "OK" # ברירת מחדל

    # 3. יישום הלוגיקה
    if input_value == "11":
        # התשובה המבוקשת כאשר myparam=11
        response_text = "read=t-חלק שני=myparam,,2,2,Number"
        
    # 4. החזרת התשובה כטקסט נקי
    return response_text, 200, {'Content-Type': 'text/plain; charset=utf-8'}

# הערה: ב-Render, שרת WSGI חיצוני (כמו Gunicorn) יריץ את האפליקציה, 
# ולכן בלוק if __name__ == '__main__': אינו הכרחי לפריסה.
