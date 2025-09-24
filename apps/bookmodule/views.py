from django.http import HttpResponse
def index(request):
    name = request.GET.get("name") or "world!"  
    return HttpResponse("Hello, "+name)

 
def index2(request, val1 = 0):  
    return HttpResponse("value1 = "+str(val1))
