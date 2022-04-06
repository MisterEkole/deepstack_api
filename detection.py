from deepstack_sdk import ServerConfig, Detection, detection

config=ServerConfig('http://localhost:81')
detection=Detection(config)
response=detection.detectObject('./images/img2.jpg',output='img2_output.jpg')

for obj in response:
    print('Name: {}, Confidence: {}, x_min:{}, y_min{},x_max{},y_max{}'.format(obj.label,obj.confidence,obj.x_min,obj.y_min,obj.x_max,obj.y_max))