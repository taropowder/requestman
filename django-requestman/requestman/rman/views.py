from django.shortcuts import render
import re
def home(request):
    context={}
    if request.method == "POST":
        context['result']="import requests\r"
        tag = request.POST.get('code')
        context['tag']=tag
        mothed = re.findall('^\n*([A-Z]+)', tag)
        page_url = re.findall('^\n*[A-Z]+ (/.+) ', tag)
        headers = re.findall('(.+:.+?)\n', tag)
        headers_list = []
        for header in headers:
            each_header = re.findall('([A-Z].+?): (.+)\r', header)
            headers_list.append(each_header)
            if "Host" in header:
                request_url = "http://" + each_header[0][1] + page_url[0]
                context['result']=context['result']+'requests_url="' + request_url + '"\r'
        context['result'] = context['result']+"headers={\r"
        for header_list in headers_list:
            context['result'] = context['result'] +"    '%s' : '%s',\r" % (header_list[0][0], header_list[0][1])
        context['result'] = context['result']+"}\r"
        if mothed[0] == "GET":
            context['result'] = context['result']+"result=requests.get(requests_url,headers)\r"
        if mothed[0] == "POST":
            post_value = re.findall('\r\n\r\n(.+)', tag)
            post_list = []
            if "&" in post_value[0]:
                post_list = re.findall('(.+?)=(.+?)&', post_value[0])
                post_last = re.findall('^.+&(.+?)=(.+?)$', post_value[0])
                post_list.append(post_last[0])
            else:
                post_only = re.findall('(.+?)=(.+?)$', post_value[0])
                post_list[0] = post_only
            context['result'] = context['result'] + "data={\r"
            for post in post_list:
                context['result'] = context['result'] +"    '%s' : '%s',\r" % (post[0], post[1])
            context['result'] = context['result']+"}\r"
            context['result'] = context['result']+"result = requests.post(requests_url,headers,data)\r"
    return render(request, 'requestman.html', context)
# Create your views here.
