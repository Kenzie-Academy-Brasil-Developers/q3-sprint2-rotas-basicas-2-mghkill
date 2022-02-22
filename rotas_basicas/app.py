from datetime import datetime
from flask import Flask

app = Flask(__name__)

time = int(datetime.now().strftime("%H"))

@app.route('/')
def home():
    
    return {"data": "Hello Flask!"}

@app.route('/current_datetime')
def current_datetime():
    format_time = datetime.today().strftime("%d/%m/%y %I:%M %p")
    msg = {}
    if(time < 12):
        msg = {"current_datetime": format_time,"message": "Bom dia!"}
    elif(time > 12) and (time < 18):
        msg = {"current_datetime": format_time,"message": "Boa tarde!"}
    else:
        msg = {"current_datetime": format_time,"message": "Boa noite!"}
    
    return msg


    


