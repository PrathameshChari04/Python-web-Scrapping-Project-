import requests
import bs4

url = input("Enter your Url")

response = requests.get(url)

#print(type(response))
#https://techsoftindia.co.on
#print(response.text)
filename = "temp.html"
bs= bs4.BeautifulSoup(response.text,"html.parser")

formatted_text = bs.prettify()
print(formatted_text)

with open(filename,"w+") as f:
    f.write(formatted_text) 

list_imgs = bs.find_all('img')
print(list_imgs)

no_list_imgs =len(list_imgs)

anchor_tags = bs.find_all('a')

no_anchor_tags = len(anchor_tags)

print(" Number of anchor tags : ",no_anchor_tags)

print("Number of image tags : ",no_list_imgs)

