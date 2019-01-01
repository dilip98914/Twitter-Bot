import requests
from bs4 import BeautifulSoup as bs
import os

url = 'https://www.pexels.com/search/model/'

# getting the page
page=requests.get(url)
# telling soup to parse text as html
soup=bs(page.text,'html.parser')

# find by tags
image_tags=soup.findAll('img')


# scrappind data into images folder
os.chdir('images')
x=0
for image in image_tags:
	try:
		# getting url of individual image
		url=image['src']
		img=requests.get(url)
		if img.status_code==200:
			# creation of individual image
			with open('image-'+str(x)+'.jpg','wb') as f:
				f.write(img.content)
				f.close()
				x+=1
	except:
		print('error creating image files')
		pass



