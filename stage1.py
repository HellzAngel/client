import os
from flask import *
app=Flask(__name__)
def convert_bytes(num):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0
    return num

def getFileSize(fileName,path):
    if os.path.isfile(path+'/'+fileName):
        file_info = os.stat(path+'/'+fileName)
        return convert_bytes(file_info.st_size)

    
path=input('Enter the path:')
try:
    #1 question
    os.chdir(path)
    print('You are in ',path)
    files=os.listdir(path)
    info={}
     #2 question
    print("File name               File size                path")
    print("**************************************************************************************************")
    for i in files:
        print(i,"          ",getFileSize(i,path),'         ',path)
        info[i]=[getFileSize(i,path),path]
    print("**************************************************************************************************")
    
except:
    print('File not found in directory')

#question 3
@app.route('/',methods=['POST'])
def getInfo():
    return jsonify(info)

if(__name__ == '__main__'):
    app.run(debug=True)
