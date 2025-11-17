from django.shortcuts import render ,redirect
from.models import student
from django.http import HttpResponse
from django.urls import reverse
from urllib.parse import urlencode

# Create your views here.

def landing(req):
    return render(req, 'landing.html')
    
def register(req):
    return render(req,'register.html')

def registerdata(req):
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
            # print(n,e,c,g,d,q,ed,i,doc,a,v)
            user=student.objects.filter(email=e)
            if user:
                err='Email already exists'
                return render(req,'register.html',{'y':err})
            else:
                if p==cp:
                    student.objects.create(name = n ,email =e ,contact=c ,details=d ,gender=g ,qualification= q ,education=ed ,profile_pic = i,document= doc,video=v ,audio = a ,password=p)
                    msg='Registration Done'
                    return render(req , 'login.html',{'x':msg})
                else:
                    msg="password and conform password not matched"
                    data = {'name':n,'email':e,'contact':c ,'details':d ,'gender':g ,'qualification': q ,'education':ed ,'profile_pic' : i,'document': doc,'video':v ,'audio' : a ,'password':p}
                    return render(req , 'register.html',{'pmsg':msg,'data':data})
        
def login(req):
    return render(req,'login.html')          

def logindata(req):
    data=student.objects.all()
    if req.method=='POST':
        # print(req.POST)
        le=req.POST.get('email')
        lp=req.POST.get('password')
        # print(le,lp)
        user =student.objects.filter(email=le)
        if user:
            userdata=student.objects.get(email=le)
            name = userdata.name
            email = userdata.email
            contact = userdata.contact
            gender = userdata.gender
            details = userdata.details
            qualification = userdata.qualification
            education = userdata.education
            profile_pic = userdata.profile_pic
            document = userdata.document
            audio = userdata.audio
            video = userdata.video
            document = userdata.document
            password = userdata.password
            # print(name,email,contact,gender,details,qualification,education,profile_pic,document,audio,video,password)
            if password==lp:
                base_url=reverse('dashboard')
                data ={'name':name,'email':email,'contact':contact,'password':password}
                # return render(req, 'dashboard.html',data)
                url = f'{base_url}?{data}'
                return redirect(url)
                
            else:
                msss='Email & password not matched'
                return render(req, 'login.html',{'msss':msss})
            
        else:
            msgg="Email id not register"
            return render(req , 'register.html',{'msgg':msgg})

def dashboard(req):
    print(req.GET)
    e=req.GET.get('email')
    p=req.GET.get('password')
    print(e,p)
    if e and p:
        data={'name':req.GET.get('name'),'contact':req.GET.get('contact'),
              'gender':req.GET.get('gender'),'details':req.GET.get('details'),
              'qualification':req.GET.get('qualification'),'education':req.GET.get('education'),
              'profile_pic':req.GET.get('profile_pic'),'document':req.GET.get('document'),
              'audio':req.GET.get('audio'), 'video':req.GET.get('video'), 'password':req.GET.get('password')}
        return render(req, 'dashboard.html',data)
    else:
        return render(req, 'login.html')
    