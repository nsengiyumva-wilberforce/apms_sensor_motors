from flask import Flask, request
import touch
import current_water
app = Flask(__name__)

@app.route('/sensor-data', methods=['GET', 'POST'])
def handle_sensor_data():
    if request.method == 'POST':
        data = request.form.get('data')
        sensorCategory = request.form.get('sensorCategory')
        sensorId = request.form.get('sensorId')
        if(sensorCategory == 'Security Section'):
            print("inside security control section")
            if (data =="1"):
                print("Security control activated")
                touch.get_sensor_status(1)
            elif(data =="0"):
                print("security control deactivated")
                touch.get_sensor_status(2)
        elif(sensorCategory =='Water sensor'):
            print("inside the water control section")
            if (data == "1"):
                print("Water sensor activated")
                current_water.get_water_sensor_status(1)
            elif(data =="0"):
                print("Water sensor deactivated")
                current_water.get_water_sensor_status(2)
        print('sensor Id :', sensorId)
        print('Sensor name is:', sensorCategory)
        print('Received data:', data)
        # Process the received data as needed
        return {'message': 'Data received successfully'}

    # Handle GET requests if necessary
    data = GPIO.input(10)
    return {'data': data}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)