from datetime import datetime
from flask import Flask

app = Flask(__name__)

time = int(datetime.now().strftime("%H"))

@app.route('/')
def home():
    
    return {"data": "Hello Flask!"}

@app.route('/current_datetime')
def current_datetime():
    
    msg = {}
    if(time < 12):
        msg = {"current_datetime": datetime.now(),"message": "Bom dia!"}
    elif(time > 12) and (time < 18):
        msg = {"current_datetime": datetime.now(),"message": "Boa tarde!"}
    else:
        msg = {"current_datetime": datetime.now(),"message": "Boa noite!"}
    
    return msg


    


