from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request, 'us/login.html')
    elif request.POST.get('username') == 'admin':
        # return redirect("/blog/register")
        return render(request,"blog/register.html")
    else:
        return HttpResponse("用户名不为admin,请重新输入")



