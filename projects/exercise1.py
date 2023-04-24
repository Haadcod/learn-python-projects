"""Python program to find the requests module -version,liscence,copyright information,aurthor name,ducument url,tilte and description"""
import requests
print("Python requests module-version",requests.__version__)
print("Liscence:",requests.__license__)
print("copyright information:",requests.__copyright__)
print("author:",requests.__author__)
print("Description:",requests.__description__)
print("url",requests.__url__)
print("Title",requests.__title__)
"""python program to check for the status code issued by a server in response to client request 
   made to the server. This includes all attributes and methods available to theobject on successfull request"""
res=requests.get("https://google.com/")
print("The response of https://google.com/:")
print(res.status_code)
res=requests.get("https://amazon.com/")
print("The response of https://amazon.com/:")
print(res.status_code)
res=requests.get("https://w3resource.com//")
print("The response of https://w3resource.com:")
print(res.status_code)
