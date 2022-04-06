import requests

image_data = open("./images/img4.jpg","rb").read()

response = requests.post("http://localhost:82/v1/vision/scene",files={"image":image_data}).json()
print("Label:",response["label"])
print(response)