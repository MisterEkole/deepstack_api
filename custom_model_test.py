import requests

image_data = open("./custom_model/cell_images/Test/img14.png","rb").read()

response = requests.post("http://localhost:80/v1/vision/custom/custom_model/model/smear_analyser",files={"image":image_data}).json()

for object in response["predictions"]:
    print(object["label"])

print(response)