import requests

class Iftttnotify:
    def __init__(self,event_name,api_key):
        self.event_name = event_name
        self.api_key = api_key
        # self.json_data = json_data

    def notify(self,json_data={}):
        url = f"https://maker.ifttt.com/trigger/{self.event_name}/json/with/key/{self.api_key}"

        # json_data = {"value1":"Ahmed", "value2":"Hello"}

        print("sending . . .")
        try:
            response = requests.post(url,json_data)
        except ConnectionError:
            print("internet issues")

        print(response.text)

        if response.status_code == 200:
            print("well done")
        else:
            print("Error")
    

    