from flask import Flask, request, flash, url_for
import grovepi
import time

# Connect the Grove Button to digital port D3
button = 3
grovepi.pinMode(button,"INPUT")

# Connect the Grove Buzzer to digital port D5
buzzer = 5
grovepi.pinMode(buzzer,"OUTPUT")


app = Flask(__name__)
app.secret_key = "secret key"

@app.route("/")
def index():
    return """
        <form action="/alarm-on" method="post">
            Alarm time: <input type="text" name="alarm_time">
            <input type="submit" value="Set Alarm">
        </form>
    """

@app.route("/alarm-on", methods=["POST"])
def alarm_on():
    alarm_time = request.form["alarm_time"]
    print("Alarm set for " + alarm_time)
    return execute_alarm(alarm_time)

def execute_alarm(alarm_time):
    current_time = time.strftime("%H:%M")
    while current_time != alarm_time:
        time.sleep(1)
        current_time = time.strftime("%H:%M")
    for i in range(5):
        if(grovepi.digitalRead(button) == True):
            grovepi.digitalWrite(buzzer,0)
            return "<h2>Alarm off!</h2>"
        else:
            grovepi.digitalWrite(buzzer,1)
            time.sleep(0.5)
            grovepi.digitalWrite(buzzer,0)
            time.sleep(0.5)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

