from django.shortcuts import render,redirect
from hospital.forms import DoctorReg,PatientReg,Booking,DocUpdate
from hospital.models import doctor,patient,booking,docupdate
# Create your views here.
def home(request):
   return render(request,'home.html')
   
def contact(request):
  return render(request,'contact.html')
   
def about(request):
   return render(request,'about.html')
   
   
def doctorreg(request):
   return render(request,'doctor.html')
   
def docreg(request):
  if request.method=="POST":
    dr=DoctorReg(request.POST)
    if dr.is_valid():
      try:
        dr.save()
        return render(request,'doctor.html')
      except:
        pass
    else:
      dr=DoctorReg()
    return render(request,'doctor.html') 
        
    
def docshow(request):
  d=doctor.objects.all()
  return render(request,'docshow.html',{'d':d})

def docdelete(request,id):
   d=doctor.objects.get(id=id)
   d.delete()
   return redirect('../docshow')
   
def docedit(request,id):
  d=doctor.objects.get(id=id)
  return render(request,'docedit.html',{'d':d})
  
def docedcode(request,id):
  d=doctor.objects.get(id=id)
  reg=DoctorReg(request.POST,instance=d)
  if reg.is_valid():
    reg.save()
    return redirect('../docshow')
  return render(request,'docedit.html',{'d':d})

def doctorlog(request):
  return render(request,'doctorlog.html')

 
     
def doclog(request):
   if request.method=='POST':
      email=request.POST['email']
      pwd=request.POST['pwd']
      try:
         e=doctor.objects.get(email=email)
         p=doctor.objects.get(pwd=pwd)
         if e and p is not None:
           return render(request,'docwel.html')
         else:
            return render(request,'doctorlog.html')
      except:
          return render(request,'doctorlog.html')



def patientreg(request):
   return render(request,'patient.html')
   
def patreg(request):
  if request.method=="POST":
    pr=PatientReg(request.POST)
    if pr.is_valid():
      try:
        pr.save()
        return render(request,'patient.html')
      except:
        pass
    else:
      pr=PatientReg()
    return render(request,'patient.html') 

def patshow(request):
  p=patient.objects.all()
  return render(request,'patshow.html',{'p':p})

def patdelete(request,id):
   p=patient.objects.get(id=id)
   p.delete()
   return redirect('../patshow')
   
def patedit(request,id):
  p=patient.objects.get(id=id)
  return render(request,'patedit.html',{'p':p})
  
def patedcode(request,id):
  p=patient.objects.get(id=id)
  reg=PatientReg(request.POST,instance=p)
  if reg.is_valid():
    reg.save()
    return redirect('../patshow')
  return render(request,'patedit.html',{'p':p})


  
def patientlog(request):
   return render(request,'patientlog.html')
   
def patlog(request):
   if request.method=='POST':
      email=request.POST['email']
      pwd=request.POST['pwd']
      try:
         e=patient.objects.get(email=email)
         p=patient.objects.get(pwd=pwd)
         if e and p is not None:
           return render(request,'patwel.html')
         else:
            return render(request,'patientlog.html')
      except:
          return render(request,'patientlog.html')

def doclist(request,):
  d=doctor.objects.all()
  return render(request,'doclist.html',{'d':d})
  
def timing(request):
  return render(request,'timing.html')
  
def docbook(request):
  d=doctor.objects.all()
  return render(request,'docbook.html',{'d':d})


  
 
def docbooking(request):
   return render(request,'booking.html')



def dbk(request):
   if request.method=="POST":
     b=Booking(request.POST)
     if b.is_valid():
       try:
          b.save()
          return render(request,'success.html')
       except:
          pass
   else:
      b=Booking()
   return render(request,'booking.html')
   
def bookshow(request):
  b=booking.objects.all()
  return render(request,'bookshow.html',{'b':b})
  
def bkdelete(request,id):
  b=booking.objects.get(id=id)
  b.delete()
  return redirect('../bookshow')
  
def bkedit(request,id):
   b=booking.objects.get(id=id)
   return render(request,'bookedit.html',{'b':b})
   
def edbk(request,id):
  b=booking.objects.get(id=id)
  book=Booking(request.POST,instance=b)
  if book.is_valid():
    book.save()
    return redirect('../bookshow')
  return render(request,'bookedit',{'b':b})
  
def apporment(request):
  b=booking.objects.all()
  return render(request,'apporment.html',{'b':b})
  
def update(request,id):
   u=booking.objects.get(id=id)
   return render(request,'update.html',{'u':u})
   
def upd(request):
   if request.method=="POST":
    up=DocUpdate(request.POST)
    if up.is_valid():
     try:     
      up.save()
      return render(request,'docwel.html')
     except:
       pass
    else:
       up=DocUpdate()
    return render(request,'apporment.html',{'b':up})


   
def patdetails(request):
   p=patient.objects.all()
   return render(request,'patientdetails.html',{'p':p})   
def medical(request):
   return render(request,'medical.html') 
  
  
def med(request):
  if request.method=='POST':
      name=request.POST['name']
      
      try:
         n=docupdate.objects.get(name=name)
         
         if n is not None:
           return render(request,'history.html',{'n':n})
         else:
            return render(request,'medical.html')
      except:
          return render(request,'medical.html')