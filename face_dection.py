import requests

image_data = open("./images/img1.jpg","rb").read()

response = requests.post("http://localhost:80/v1/vision/face",files={"image":image_data}).json()

print(response)