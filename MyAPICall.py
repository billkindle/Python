import requests

response = requests.get('http://corsicatech.com')

print(response.status_code)  
#Response as String  
print(response.text)    
#Response as JSON
print(response.json())