"""python progam to send a request to a web page and print the response text and content
   also get row socket response from the server """
import requests
res=requests.get("https://google.com/")
print("Response text o https://google.com//")
print(res.text)
print("\n============================================================")
print("\nThe content of the said url")
print(res.content)
print("\n=============================================================")
print("\nRaw data of the said url")
re=requests.get("https://api.github.com/events",stream=True)
print(re.raw)
print(re.raw.read(15))
