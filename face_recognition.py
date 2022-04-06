import requests
#Image registration
image_1=open("./images/img3.jpg","rb").read()
user_name='Yann LeCun'

response=requests.post("http://localhost:80/v1/vision/face/register",files={"image":image_1}, data={'userid':user_name}).json()

#Face recognition
img_data=open("./images/img3.jpg","rb").read()

pred=requests.post("http://localhost:80/v1/vision/face/recognize",files={"image":img_data}).json()
for user in pred['predictions']:
    print(user['userid'])
print('Full response: ', pred)