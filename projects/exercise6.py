"""Python code to send a request to a web page and stop waiting for a response after a given number of seconds """
import requests
import requests.exceptions

print("timeout=0.001")
try:
    res=requests.get("https://github.com/",timeout=0.001)
    print(res.text)
except requests.exceptions.RequestException as e:
    print(e)