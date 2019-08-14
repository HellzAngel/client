import os
from flask import *
import requests
import json
app=Flask(__name__)
#question 1
port=input('Enter the port:')

def most_frequent(List): 
    counter = 0
    num = List[0] 
      
    for i in List: 
        curr_frequency = List.count(i) 
        if(curr_frequency> counter): 
            counter = curr_frequency 
            num = i 
  
    return num 
#question 2
@app.route('/getInformation',methods=['POST'])
def fileStatistic():
    url='http://localhost:5000/'
    response=requests.post(url,json={}).json()
    info={}
    info['number_of_file_recived']=len(response)
    fileSize=[]
    listOfFileEx=[]
    for i in response:
        fileSize.append(i['file_size'])
        listOfFileEx.append(i['extension'])
    max_extension=most_frequent(listOfFileEx)
    info['max_extension']=max_extension
    info['list_of_extension']=listOfFileEx
    info['file_size']=fileSize
    return jsonify(info)

#question 4
@app.rout('/get',methods=['GET'])
def get():
    url='http://localhost:5000/'
    response=requests.post(url,json={}).json()
    return jsonify(response)


if(__name__ == '__main__'):
    print('server running on port:',port)
    app.run(debug=True,port=port)