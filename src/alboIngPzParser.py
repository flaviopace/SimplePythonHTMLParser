import urllib2
from bs4 import BeautifulSoup
import sys

f = open('IngPZAll.txt', 'w')

url = "http://www.ordingpz.it/albo/Albolist.asp?pageno=1&t=Albo&RecPerPage=3000"
print url

try:
    data = urllib2.urlopen(url).read()
except:
	print url

soup = BeautifulSoup(data)

n =  soup.findAll("td",{"width":"100"})

#print n
numIscr = []

for i in n:
	numIscr.append(i.div.string)


for i in range(len(numIscr)):
	url = "http://www.ordingpz.it/albo/Alboview.asp?N__ISCR_="+str(numIscr[i])
	f.write(url+"\n")
	print "Parsing "+ str(i) + " of " + str(len(numIscr))
	print url

	try:
	    data = urllib2.urlopen(url).read()
	except:
		print url

	soup = BeautifulSoup(data)
	#print soup.prettify()
	n =  soup.findAll("td" , "ewTableHeader")
	
	fields = []

	for i in n:
		fields.append(i.string.encode('ascii','ignore'))
		
	n =  soup.findAll("div")

	values = [];

	#print n
	count = 0;

	for i in n:
		count=count+1;
		#print count
		if(i.string != None and count > 19):
			#print i.string
			values.append(i.string.encode('ascii','ignore'))


	for i in range(len(values)):
		try:
			f.write(str(fields[i]+ ": "+values[i]).encode('utf-8')+"\n")
		except:
			print fields[i]+ ": "+values[i] 

	f.write("\n")

f.close()

