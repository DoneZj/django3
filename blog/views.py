from django.shortcuts import render, HttpResponse, render_to_response, redirect


# Create your views here.
def index(request,type,size):

    # return HttpResponse("type="+type+";size="+size)
    return render(request,"index.html")

def login(request):
    name = request.POST.get('username')
    passwd = request.POST.get('passwd')
    data={'username':name,'userpasswd':passwd}
    return render(request, 'blog/login.html',data)
    # return render(request, 'blog/login.html',locals())

def register(request):
    return render(request, 'blog/register.html')
    # return  render_to_response('blog/register.html')
    # return  redirect('blog/register.html')

def success(request):
    return HttpResponse("blog login Success")