import email
from click import password_option
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import userForm

def homepage(request):
    # data = {
    #     'title' : 'New Home Page',
    #     'bdata' : 'This is Django website',
    #     'clist' : ['PHP','JAVA','DJANGO'],
    #     'numbers' : [10,20,30,40,50,60,90],
    #     'student_details' : [
    #         {'Name' : 'Manish', 'Phone' : 9876543210},
    #         {'Name' : 'Kumar', 'Phone' : 9876983210}
    #     ]
    # }
    return render(request,"index.html")

def aboutUs(request):
    return render(request,"about.html")

def account(request):
    return render(request,"account.html")

def bookdetail(request):
    return render(request, "book-detail.html")

def cart(request):
    return render(request, "cart.html")

def ebooks(request):
    return render(request, "ebooks.html")

def contact(request):
    return render(request, "contact.html")

def courseDetails(request,courseid):
    return HttpResponse(courseid)

def form(request):
    finalans = 0
    fn = userForm()
    data = {'forms' : fn}
    try:
        if request.method =='POST':
            n1 = int(request.POST.get('name'))
            n2 = int(request.POST.get('email'))
            n3 = int(request.POST.get('phone'))
            finalans = int(n1+n2+n3)
            data= {
                #'n1' : n1,
                #'n2' : n2,
                #'n3' : n3,
                'forms' : fn,
                'output' : finalans
            }
            url = "/thank/?output = {}".format(finalans)
            return redirect(url)
    except:
        pass
    return render(request,"form.html",data)

def UserForm(request):
    #finalans =""
    try:
        num =  request.GET.get('email')
        num2 = request.GET.get('phone')
       # finalans = str(num,num2)
        
    except:
        pass
    return render(request,"userform.html")

def Thank(request):
    if request.method == "GET":
        output=request.GET.get('output')
    return render(request,'thank.html',{'output':output})

def submitform(request):
    finalans = 0
    data = {}
    try:
        if request.method =='POST':
            n1 = int(request.POST.get('name'))
            n2 = int(request.POST.get('email'))
            n3 = int(request.POST.get('phone'))
            finalans = int(n1+n2+n3)
            data= {
                'n1' : n1,
                'n2' : n2,
                'n3' : n3,
                'output' : finalans
            }
            url = "/thank/?output = {}".format(finalans)
            return HttpResponse(finalans)
    except:
        pass
    return render(request,"form.html",data)
   