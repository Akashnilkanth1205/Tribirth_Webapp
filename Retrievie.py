#pip install git+https://github.com/ozgur/python-firebase
from firebase import  firebase
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
from scipy.fft import fftshift
import os
import glob
from flask import Flask,render_template
import streamlite
import json


#retrieve json file from firebase
firebase = firebase.FirebaseApplication('https://tribirth-f4422-default-rtdb.firebaseio.com/',None)
result = firebase.get("0","")
#print(result)

jtopy=json.dumps(result) #json.dumps take a dictionary as input and returns a string as output.
dict_json=json.loads(jtopy) # json.loads take a string as input and returns a dictionary as output.

# print(dict_json["FIELD1"])

my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.1)
     my_bar.progress(percent_complete + 1)


def Data_Preprocess(x):
 sig = [np.array(x)]
 # print(sig)
 return sig

def Apply_Filter(sig):
    sos = signal.butter(1, [0.1, 20], 'band', fs=100, output='sos')
    filtered = signal.sosfilt(sos, sig)
    #print (filtered)
    return filtered


def Plot_Graph(filtered):
   t = np.linspace(0, 15,1500, False)
   t = t[:filtered.size]
   plt.plot(t.squeeze(), filtered.squeeze())
   plt.suptitle('Filtered Scan Data')
   plt.axis([0, 15, 0, 400])
   # plt.show()
   plt.savefig("output.jpg")

Data = Data_Preprocess(dict_json["FIELD1"])
Filtered_data = Apply_Filter(Data)
Plot_Graph(Filtered_data)
print(Filtered_data)



# app = Flask(__name__)
# picFolder = os.path.join('venv')
# app.config['UPLOAD_FOLDER'] = venv
# @app.route("/")
# def index():
#  output = os.path.join(app.config["UPLOAD_FOLDER"],'output.jpg')
#  return render_template["index.html",user_image = output]

# if __name__== "__main__":
#     app.run(debug=True)






#  return Filtered_data
 # print(Filtered_data)



# json_object = json.dumps(Filtered_data,"FIELD1")
# print(json_object)










# Filtered_data= firebase.post('tribirth-f4422-default-rtdb/Customer',Data)

# print(result)
#
#     return Filtered_data


# if __name__== "__main__":
#     app.run(debug=True)




# data_items= Filtered_data.items()
# data_list = list(data_items)
# df = pd.DataFrame(data_list)
# print(df)
#pd.DataFrame(json.loads(""))
# print(Data)
# Plot_Graph(Filtered_data)
#
# df = pd.DataFrame(Plot_Graph())
# print (Plot_Graph())
# for i in Data['FIELD1']:
#
#     print(i)

