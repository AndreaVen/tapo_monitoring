
from PyP100 import PyP110
from dotenv import load_dotenv
import os
from flask import Flask, render_template
import numbers
app = Flask(__name__)


@app.route('/')
def index():
    
    load_dotenv()
    mail=os.environ['tapo_mail']
    psw=os.environ['tapo_psw']
    blanket= PyP110.P110("192.168.1.49", mail, psw)
    bedroom_AC = PyP110.P110("192.168.1.38", mail, psw)
    oven = PyP110.P110("192.168.1.225", mail, psw)
    pc_hub = PyP110.P110("192.168.1.113", mail, psw)
    whashing_machine = PyP110.P110("192.168.1.92", mail, psw)
    main_fridge = PyP110.P110("192.168.1.191", mail, psw)
    instant_pot = PyP110.P110("192.168.1.118", mail, psw)
    livingroom_AC = PyP110.P110("192.168.1.110", mail, psw)





    instant_pot.handshake()
    instant_pot.login()

    hub=pc_hub.getEnergyUsage()["current_power"]/1000

    livingroom_AC_power=livingroom_AC.getEnergyUsage()["current_power"]/1000

    hot_pot_power=instant_pot.getEnergyUsage()["current_power"]/1000
    blanket_power=blanket.getEnergyUsage()["current_power"]/1000
    oven_power=oven.getEnergyUsage()["current_power"]/1000
    bedroom_AC_power=bedroom_AC.getEnergyUsage()["current_power"]/1000
    main_fridge_power=main_fridge.getEnergyUsage()["current_power"]/1000
    washing_machine_power=whashing_machine.getEnergyUsage()["current_power"]/1000

    total_power=calculate_total_power([hot_pot_power,hub,blanket_power,oven_power,bedroom_AC_power,livingroom_AC_power,washing_machine_power,main_fridge_power])


    return render_template('index.html',hot_pot_value=hot_pot_power,pc_hub=hub,blanket=blanket_power,
                           oven=oven_power,bedroom_ac=bedroom_AC_power,washing_machine=washing_machine_power,livingroom_ac=livingroom_AC_power,
                           fridge=main_fridge_power,tot_pot=total_power)


def calculate_total_power(sensors):
    total=0
    for sensor_value in sensors:
        if isinstance(sensor_value, numbers.Number):
            total+=sensor_value

    total=str(round(total, 2))
    return total



if __name__ == "__main__":
   
    app.run(debug=True, host='0.0.0.0')
