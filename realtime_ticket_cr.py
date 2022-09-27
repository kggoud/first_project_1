
import requests

import json
class Incident:

    api_url="https://dev81550.service-now.com/api/now/table/incident"
    headers={"accept":"application/json","content-type":"application/json"}
    
    descrip={"shot_description":"money detected"#,"ticket creation testing from service now api"}

    def __init__(self,user,pasword):
        self.user= user_id
        self.pasword= pasword

    def test (self):
        response=requests.post(self.api_url,auth=(self.user,self.posward)
        headers=(self.headers),data=json.dumps(self.descrip))

    print(response.json())
x=Incident("admin","oX7ph!O7HVn+")
x.note