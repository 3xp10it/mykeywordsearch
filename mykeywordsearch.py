from pygoogle import pygoogle
import time
print "please input your keyword you want google to search:"
keyword=raw_input()
all_urls=[]

for i in range(2):
    g=pygoogle(query=keyword)
    urls=g.get_urls()
    all_urls.extend(urls)
    time.sleep(2)

#实验证明搜索一次和搜索三次结果一样
'''
g=pygoogle(query=keyword)
urls=g.get_urls()
all_urls.extend(urls)
print len(all_urls)
'''

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
