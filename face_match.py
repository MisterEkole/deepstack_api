import requests

image_data1 = open("./images/img2.jpg","rb").read()
image_data2 = open("./images/img4.jpg","rb").read()

response = requests.post("http://localhost:80/v1/vision/face/match",files={"image1":image_data1,"image2":image_data2}).json()

print(response)