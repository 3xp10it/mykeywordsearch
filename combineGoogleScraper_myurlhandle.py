#need python3 coz GoogleScraper require it.
print("please input your keyword you want google to search:")#inurl:index.php?option=
keyword=input()
print("please input the number of pages you want google to search:")
num_page=int(input())
print("please input the method you want google to search {http,selenium,http-async} :")
method=input()
print("please input the browser you want google to use,this take \
	effects only in [selenium] method,[http] or [http-async] any \
	is ok,coz take no effects,input one of {firefox,chrome,phantomjs} here:")
browser=input()





all_urls=[]

from GoogleScraper import scrape_with_config, GoogleSearchError

# See in the config.cfg file for possible values
config = {
    'use_own_ip': True,
    'keyword': keyword,
    'search_engines': ['google'],#google,yahoo,baidu...is ok,see GoogleScraper source.
    'num_pages_for_keyword': num_page,
    'scrape_method': method,
    'sel_browser': browser,
    'do_caching': False
}

try:
    search = scrape_with_config(config)
except GoogleSearchError as e:
    print(e)

# let's inspect what we got

for serp in search.serps:
    '''
    print(serp)
    print(serp.search_engine_name)
    print(serp.scrape_method)
    print(serp.page_number)
    print(serp.requested_at)
    print(serp.num_results)
    '''
    # ... more attributes ...
    for link in serp.links:
        #link=link.split(">")[]
        #print(type(link))
        #print(link.link)
        all_urls.append(link.link)








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
    file=open("urls.txt","a+")
    file.close()   
    for ur in four_url:
        file=open("urls.txt","r+")  
        '''
        python3下不可写成"ab+",although in linux,且"a+"不能支持readlines,读不出来数据,i chosed "a+" for file write,and close file,then "r+" for f.readlines(),
        于是python3下还得事先创建url.txt,因为上面的"r+"会发现没有urls.txt文件
        file=open("urls.txt","ab+")  python2 下可以"ab+" 
        '''
        all_lines=file.readlines()
        print(all_lines)
        print(len(all_lines))
        file.close()

        #if ur+"\r\n" not in all_lines:
        if ur+"\n" not in all_lines:
        	'''
        	python3下write(ur+"\r\n")也只能在字符串后加到"\n",不会加上"\r\n",python2下write(ur+"\r\n")是加上"\r\n"
        	所以python2下的if ur+"\r\n" not in all_lines要写成if ur+"\n" not in all_lines
        	'''
        	#print(type(ur))
        	#print(type("\r\n"))
        	#print(type(ur+"\r\n"))
        	file=open("urls.txt","a+")
        	#file.write(ur+"\r\n"),python3下写成 ur+"\r\n" 或 ur+"\n" 效果一样
        	file.write(ur+"\n")
        	file.flush()
        	file.close()
for url in all_urls:
    save_url_to_file(url)
