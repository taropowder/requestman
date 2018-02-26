import requests
import re
tag = """POST /wp-login.php HTTP/1.1
Host: 123.206.74.236
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
Referer: http://123.206.74.236/wp-login.php?redirect_to=http%3A%2F%2F123.206.74.236%2Fwp-admin%2F&reauth=1
Cookie: csrftoken=3P6IlSagE94fM8q0KUBvOjBBunadwAOY; wp-settings-1=libraryContent%3Dbrowse%26hidetb%3D1%26editor%3Dtinymce%26mfold%3Do; wp-settings-time-1=1519547481; wordpress_test_cookie=WP+Cookie+check
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 111

log=123&pwd=123&wp-submit=%E7%99%BB%E5%BD%95&redirect_to=http%3A%2F%2F123.206.74.236%2Fwp-admin%2F&testcookie=1
"""
'''&pwd=123&wp-submit=%E7%99%BB%E5%BD%95&redirect_to=http%3A%2F%2F123.206.74.236%2Fwp-admin%2F&testcookie=1'''

mothed = re.findall('^\n*([A-Z]+)',tag)
page_url=re.findall('^\n*[A-Z]+ (/.+) ',tag)
headers=re.findall('(.+:.+?)\n',tag)
headers_list=[]
request_url=''
for header in headers:
    each_header = re.findall('([A-Z].+?): (.+)', header)
    headers_list.append(each_header)
    if "Host" in header:
        request_url = "http://"+each_header[0][1]+page_url[0]
headers_dist = {}
for header_list in headers_list:
    headers_dist[header_list[0][0]]=header_list[0][1]
if mothed[0] == "GET":
    result=requests.get(request_url,headers_dist)
    print(result.text)
if mothed[0] == "POST":
    post_value = re.findall('\n\n(.+)', tag)
    post_dist = {}
    if "&" in post_value[0]:
        post_list = re.findall('(.+?)=(.+?)&', post_value[0])
        post_last = re.findall('^.+&(.+?)=(.+?)$', post_value[0])
        post_list.append(post_last[0])
        for post in post_list:
            post_dist[post[0]]=post[1]
    else:
        post = re.findall('(.+?)=(.+?)$',post_value[0])
        post_dist[post[0][0]]=post[0][1]
    result = requests.post(request_url,headers_dist,post_dist)
    print(result.text)



