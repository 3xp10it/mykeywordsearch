from pygoogle import pygoogle
print "please input your keyword you want google to search:"
keyword=raw_input()
g=pygoogle(query=keyword)
all_urls=g.get_urls()
f=open("urls.txt","wb")

def save_url_to_file(url,file):
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
        file.write(ur+"\r\n")
        file.flush()
for url in all_urls:
    save_url_to_file(url,f)
f.close()     

               



