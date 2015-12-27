print "please input your keyword you want google to search:"#inurl:index.php?option=
keyword=raw_input()
print "please input the number of pages you want google to search:"
num_page=int(raw_input())
'''
here is the "google" from :
__author__ = "Anthony Casagrande <birdapi@gmail.com>, " + \
    "Agustin Benassi <agusbenassi@gmail.com>"
__version__ = "1.1.0"

Google-Search-API-1.1.10 from internet
https://pypi.python.org/pypi/Google-Search-API
'''
all_urls=[]


from google import google

search_results = google.search(keyword, num_page)
i=0
for obj in search_results:
	all_urls.append(obj.link)
	i=i+1
print i




def save_url_to_file(url):
    list3=url.split("/")[2]
    four_url=[]
    domain1="http://"+list3
    domain2="https://"+list3
    domain3=domain1+"/"+url.split("/")[3]
    domain4=domain2+"/"+url.split("/")[3]
    four_url.append(domain1)
    four_url.append(domain2)
    four_url.append(domain3)
    four_url.append(domain4)    
    for ur in four_url:
        file=open("urls.txt","ab+")
        all_lines=file.readlines()
        #print all_lines
        if ur+"\r\n" not in all_lines:
            file.write(ur+"\r\n")
            file.flush()
            file.close()      
for url in all_urls:
    save_url_to_file(url)
