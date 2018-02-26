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
print("import requests")
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
        print('requests_url="'+request_url+'"')
print('headers={')
for header_list in headers_list:
    print("    '%s' : '%s'," % (header_list[0][0] , header_list[0][1]) )
print("}")
if mothed[0] == "GET":
    print("result=requests.get(requests_url,headers)")
if mothed[0] == "POST":
    post_value = re.findall('\n\n*(.+)&', tag)
    print(post_value)
    post_list=[]
    if "&" in post_value[0]:
        post_list = re.findall('(.+?)=(.+?)&', post_value[0])
        post_last = re.findall('^.+&(.+?)=(.+?)$', post_value[0])
        post_list.append(post_last[0])
    else:
        post_only = re.findall('(.+?)=(.+?)$',post_value[0])
        post_list[0]=post_only
    print("data={")
    for post in post_list:
        print("    '%s' : '%s'," % (post[0],post[1]))
    print('}')
    print("result = requests.post(requests_url,headers,data)")
    #