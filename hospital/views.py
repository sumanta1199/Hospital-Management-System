from unicodedata import name
from django.shortcuts import render,redirect
from hospital.forms import DoctorReg,PatientReg,Booking,DocUpdate,Contact
from hospital.models import doctor,patient,booking,docupdate,Post, BlogComment,contact
from django.http import HttpResponse
from django.contrib.auth  import authenticate,  login, logout
from hospital.templatetags import extras
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def home(request):
  return render(request,'home.html')
def contact(request):
  return  render(request,'contact.html')
def con(request):
  if request.method=="POST":
    c=Contact(request.POST)
    if c.is_valid():
      try:
        c.save()
        messages.success(request, "Thanks for Contact!!!")
        return render(request,'contact.html')
      except:
        pass
    else:
      c= Contact()
    return render(request,'contact.html')

   
def about(request):
   return render(request,'about.html')

def ourservice(request):
  return render(request, 'ourservice.html')

def gallery(request):
  return render(request, 'gallery.html')
   
def doctorreg(request):
   return render(request,'doctor.html')
   
def docreg(request):
  if request.method=="POST":
    dr=DoctorReg(request.POST)
    if dr.is_valid():
      try:
        dr.save()
        messages.success(request, "Your Account has been successfully created!!")
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
           messages.success(request, "Logged In Sucessfully!!")
           return render(request,'docwel.html')
         else:
            return render(request,'docwel.html')
      except:
          return render(request,'docwel.html')

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return render(request, "home.html")

def patientreg(request):
   return render(request,'patient.html')
   
def patreg(request):
  if request.method=="POST":
    pr=PatientReg(request.POST)
    if pr.is_valid():
      try:
        pr.save()
        messages.success(request, "Your Account has been successfully created!!")
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
          messages.success(request, "Logged In Sucessfully!!")            
          return render(request,'patwel.html')
         else:
            messages.error(request, "Invalid credentials! Please try again")
            return render(request,'patwel.html')
      except:
          return render(request,'patwel.html')

# def patlog(request):
#    if request.method=='POST':
#       email=request.POST['email']
#       pwd=request.POST['pwd']
#       try:
#          e=patient.objects.get(email=email)
#          p=patient.objects.get(pwd=pwd)
#          if e and p is not None:
#            messages.success(request, "Logged In Sucessfully!!")
#            return render(request,'patwel.html')
#          else:
#             messages.error(request, "Invalid credentials! Please try again")
#             return redirect('patwel')
#       except:
#           return render(request,'patwel.html')  

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
    du=DocUpdate(request.POST)
    if du.is_valid():
     try:     
      du.save()
      return render(request,'docwel.html')
     except:
       pass
    else:
       du=DocUpdate()
       b=booking.objects.all()
    return render(request, 'apporment.html',{'b':b})
    
# def updelete(request,id):
#   du=docupdate.objects.get(id=id)
#   du.delete()
#   return redirect("../apporment")
   
def patdetails(request):
   p=patient.objects.all()
   return render(request,'patientdetails.html',{'p':p})   

def medical(request):
   return render(request,'medical.html') 
  
def med(request):
  if request.method=='POST':
      name=request.POST['name']
      
      try:
         n=docupdate.objects.filter(name=name)
         
         if n is not None:
           return render(request,'history.html',{'n':n})
         else:
            return HttpResponse('Patient are not avaliable')
      except:
          # return render(request,'medical.html')
          pass

def docsearch(request):
  if request.method=='POST':
      name=request.POST['name']
      
      try:
         d=doctor.objects.filter(name=name)
         
         if d is not None:
           return render(request,'docsearch.html',{'d':d})
         else:
            return HttpResponse('Doctor are not avaliable')
      except:
          # return render(request,'home.html')
          pass

def blogHome(request): 
    allPosts= Post.objects.all()
    context={'allPosts': allPosts}
    return render(request, "blogHome.html", context)

def search(request):
    query=request.GET['query']
    if len(query)>78:
        allPosts=Post.objects.none()
    else:
        allPostsTitle= Post.objects.filter(title__icontains=query)
        allPostsAuthor= Post.objects.filter(author__icontains=query)
        allPostsContent =Post.objects.filter(content__icontains=query)
        allPosts=  allPostsTitle.union(allPostsContent, allPostsAuthor)
    if allPosts.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    params={'allPosts': allPosts, 'query': query}
    return render(request, 'blogSearch.html', params)

def blogPost(request, slug): 
    post=Post.objects.filter(slug=slug).first()
    comments= BlogComment.objects.filter(post=post, parent=None)
    replies= BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    context={'post':post, 'comments': comments, 'user': request.user, 'replyDict': replyDict}
    return render(request, "blogPost.html", context)

def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= Post.objects.get(sno=postSno)
        parentSno= request.POST.get('parentSno')
        if parentSno=="":
            comment=BlogComment(comment= comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent= BlogComment.objects.get(sno=parentSno)
            comment=BlogComment(comment= comment, user=user, post=post , parent=parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully")        
    return redirect("{post.slug}")


          