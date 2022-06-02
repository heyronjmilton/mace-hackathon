from gevent import monkey; monkey.patch_all()
from flask import Flask, Response, render_template, stream_with_context, request
from gevent.pywsgi import WSGIServer
import json
import csv
import time
import plant_check
import READEACH


with open("condition.csv",mode='w') as csvfile :     
    mywriter=csv.writer(csvfile)
    mywriter.writerow("0")                 #gotta call specfic plant csv
    csvfile.close()

def conditon_send(condit):
    with open("condition1.csv",mode='w',newline="") as csvfile :     
        mywriter=csv.writer(csvfile)
        mywriter.writerow(condit) 
        csvfile.close()

        

def send_value(value):
  with open("value.csv",mode='w',newline="") as csvfile :
    mywriter=csv.writer(csvfile)
    mywriter.writerow(value)
    csvfile.close()
   

app = Flask(__name__)

@app.route("/")
def render_index():
  return render_template("hackton.html")

@app.route("/farm-page")
def render_farm():
  return render_template("farm.html")

@app.route("/farm_listen")
def farm_listen():

  def respond_to_client():
    
    
    while True:
        sector_moisture = []
        sector_motor = []
        sector_plant = [] 
        sector_plant_health = []


        for r in range(1,10) :
          sector_moisture.append(READEACH.moist(r))

        for r in range(1,10) :
          sector_motor.append(READEACH.motor(r))

        for r in range(1,10) :
          sector_plant.append(plant_check.sec_color(READEACH.color(r)))
          
        for r in range(1,10):
          sector_plant_health.append(plant_check.check_health(READEACH.color(r)))

        _data = json.dumps({"sector_plant" : sector_plant,"sector_motor" : sector_motor,"sector_moisture" : sector_moisture,"sector_plant_health" : sector_plant_health})
        yield f"id: 1\ndata: {_data}\nevent: online\n\n"
        time.sleep(1)
  return Response(respond_to_client(), mimetype='text/event-stream')
  

@app.route('/farm-page/button', methods=['POST'])
def feedback():
  conditon_send("0")
  coordinates = request.form.get("coordinates")
  print(coordinates)
  if coordinates :
    conditon_send("1")
  else :
    condition_send("0")
  send_value(coordinates)
  return render_template("farm.html")

@app.route("/listen")
def listen():

  def respond_to_client():
    while True:
        humidity = 0
        tempreature = 0
        moisture = 0
        

        for r in range(1,10) :
          moisture += int(READEACH.moist(r))

        for r in range(1,10) :
          humidity += int(READEACH.humidity(r))


        for r in range(1,10) :
          tempreature += int(READEACH.temp(r))
          
        humidity = int(humidity/9)
        tempreature = int(tempreature/9)
        moisture = int(moisture/9)


        _data = json.dumps({"Humidity":humidity, "Tempreature":tempreature,"Moisture" : moisture})
        yield f"id: 1\ndata: {_data}\nevent: online\n\n"
        time.sleep(0.1)
  return Response(respond_to_client(), mimetype='text/event-stream')



                                                                    #WSGI - Web Server Gateway Interface
if __name__ == "__main__":
 
  http_server = WSGIServer(("0.0.0.0", 8080), app)
  http_server.serve_forever() 