import requests
requests_url="http://123.206.74.236/wp-login.php"
headers={
    'Host' : '123.206.74.236',
    'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language' : 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Referer' : 'http://123.206.74.236/wp-login.php?redirect_to=http%3A%2F%2F123.206.74.236%2Fwp-admin%2F&reauth=1',
    'Cookie' : 'csrftoken=3P6IlSagE94fM8q0KUBvOjBBunadwAOY; wp-settings-1=libraryContent%3Dbrowse%26hidetb%3D1%26editor%3Dtinymce%26mfold%3Do; wp-settings-time-1=1519547481; wordpress_test_cookie=WP+Cookie+check',
    'Connection' : 'close',
    'Upgrade-Insecure-Requests' : '1',
    'Content-Type' : 'application/x-www-form-urlencoded',
    'Content-Length' : '111',
}
data={
    'log' : '123',
    'pwd' : '123',
    'wp-submit' : '%E7%99%BB%E5%BD%95',
    'redirect_to' : 'http%3A%2F%2F123.206.74.236%2Fwp-admin%2F',
    'testcookie' : '1',
}
result = requests.post(requests_url,headers,data)
print(result.text)