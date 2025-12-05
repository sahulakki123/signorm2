from django.shortcuts import render,redirect
from .models import student
from django.urls import reverse 
from urllib.parse import urlencode

# Create your views he.
def landing(req):
    return render(req,'landing.html')

def register(req):
    return render(req,'register.html')

def data(req):
    if req.method=='POST':
        n=req.POST.get('name')
        e=req.POST.get('email')
        c=req.POST.get('contact')
        g=req.POST.get('gender')
        d=req.POST.get('details')
        q=req.POST.get('qualification')
        ed=req.POST.get('education')
        i=req.FILES.get('profile_pic')
        doc=req.FILES.get('document')
        a=req.FILES.get('audio')
        v=req.FILES.get('video')
        p=req.POST.get('password')
        cp=req.POST.get('cpassword')
        print(n,e,c,g,d,q,ed,i,doc,a,v,p,cp)
        user=student.objects.filter(email=e)
        if user:
               err='Email already exists'
               return render(req,'register.html',{'y':err})
        else:
            if p==cp:
                student.objects.create(name = n ,email =e ,contact=c ,details=d ,gender=g ,qualification= q ,education=ed ,profile_pic = i,document= doc,video=v ,audio = a,password=p)
                msg='Registration Done'
                return render(req , 'login.html',{'x':msg})
            else:
                pmsg='Password and confirm password not match'
                data={'name':n,'email':e,'image':i,'audio':a,'video':v,'contact':c,'gender':g,'document':doc,'qualification':q,'details':d,'eduaction':ed}
                return render(req,'register.html',{'pmsg':pmsg,'data':data})
    
# def showdata(req):
#     data=Student.objects.all()
#     return render(req , 'showdata.html',{'mydata':data})
    

def login(req):
    return render(req,'login.html')

def logindata(req):
    if req.method=='POST':
        # print(req.POST)
        le=req.POST.get('loginemail')
        lp=req.POST.get('loginpassword')
        print(le,lp)
        user=student.objects.filter(email=le)
        if user:
            userdata=student.objects.get(email=le)
            id = userdata.id
            name=userdata.name
            email=userdata.email
            password=userdata.password
            contact=userdata.contact
            image=userdata.profile_pic
            print(name,email,password,image)
            data={'id': id , 'name':name,'email':email,'contact':contact,'password':password,'image':image}
            if lp==password:
                # return render(req,'dashboard.html',{'data':data})
                baseurl=reverse('dashboard')
                data=urlencode(data)
                url=f'{baseurl}?{data}'
                return redirect(url)
            else:
                msg='email and password not match'
                return render(req,'login.html',{'msg':msg,'email':le})
        else:
            lmsg='Email id not registered'
            return render(req,'register.html',{'lmsg':lmsg})
        
def dashboard(req):
    print(req.GET)
    e=req.GET.get('email')
    p=req.GET.get('password')
    print(e,p)
    if e and p:
        id=req.GET.get('id')
        n=req.GET.get('name')
        e=req.GET.get('email')
        p=req.GET.get('password')
        c=req.GET.get('contact')
        i=req.GET.get('image')
        print(n,e,c,p,i)
        data={'id': id ,'name':n,'email':e,'contact':c,'password':p,'image':i}
        return render(req,'dashboard.html',{'data':data})
    else:
        # return render(req,'login.html')
        url=reverse('login')
        return redirect(url)
    
def query(req,pk):
    userdata= student.objects.get(id=pk)
    data={
    'id': userdata.id,
    'name':userdata.name,
    'email':userdata.email,
    'password':userdata.password,
    'contact':userdata.contact,
    'image':userdata.profile_pic
    }
    return render(req,)
    
    
    