import urllib.request
import json

url = "http://bfyxcx-ip-223-178-84-101.tunnelmole.net/get-traffic-status"

with urllib.request.urlopen(url) as response:
    if response.status == 200:
        data = json.loads(response.read().decode())
        print(data)
        traffic_status = data.get('trafficStatus')
        print(f"Traffice Status: {traffic_status}")
    else:
        print(f"Failed to retrieve traffic status.")
