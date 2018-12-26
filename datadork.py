from bs4 import BeautifulSoup
import requests
import csv

#insert website or url you want to look for other urls in 
re=requests.get('https://www.bing.com/search?q=data+breach&qs=n&form=QBLH&sp=-1&pq=data+breach&sc=8-11&sk=&cvid=ECCC11EA1B3C4539B6A1FB7F47036922')
bs=BeautifulSoup(re.text.encode('utf-8'), "html.parser")

#insert name of csv file you want the urls to be written in 
csv_file = open('test7.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['base'])



#def writing():
	#with open("test7.csv", "a") as f:
    #writeFile = csv.writer(f)
    #writeFile.writerow(link.attrs['href'])

#grabs all links that are page and prints in terminal and csv 
for link in bs.find_all('a') :
	if link.has_attr('href'):
		base = link.attrs['href']
		print (link.attrs['href'])
		#with open("test7.csv", "a") as f:
    		#writeFile = csv.writer(f)
    	csv_writer.writerow ([base])


csv_file.close()

