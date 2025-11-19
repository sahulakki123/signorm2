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
    if req.method=='POST':
        # print(req.POST)
        le=req.POST.get('email')
        lp=req.POST.get('password')
        # print(le,lp)
        user =student.objects.filter(email=le)
        if user:    
            print('Hello') 
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
                print('hello')
                base_url=reverse('dashboard')
                data ={'name':name,'email':email,'contact':contact,'gender':gender,'password':password}
                # return render(req, 'dashboard.html',data)
                url = f'{base_url}?{data}'
                return redirect(url)  
            else:
                print('Hello')
                msss='Email & password not matched'
                return render(req, 'login.html',{'msss':msss})
            
        else:
            msgg="Email id not register"
            return render(req , 'register.html',{'msgg':msgg})

def dashboard(req):
    e=req.GET.get('email')
    p=req.GET.get('password')
    if e and p:
        n=req.GET.get('name')
        c=req.GET.get('contact')
        g=req.GET.get('gender')
        d=req.GET.get('details')
        q=req.GET.get('qualification')
        ed=req.GET.get('education')
        i=req.GET.get('profile_pic')
        do=req.GET.get('document')
        a=req.GET.get('audio')
        v=req.GET.get('video')
        data={'name':n,'contact':c,
              'gender':g,'details':d,
              'qualification':q,'education':ed,
              'profile_pic':i,'document':do,
              'audio':a, 'video':v, 'email':e,'password':p}
        return render(req, 'dashboard.html',data)
    else:
        # return render(req, 'login.html')
        url =reverse('login')
        return redirect(url)
    