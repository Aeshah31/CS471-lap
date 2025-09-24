from django.http import HttpResponse
def index(request):
    name = request.GET.get("name") or "world!"  #add this line
    return HttpResponse("Hello, "+name)

