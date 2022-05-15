from django.urls import path
from . import views
urlpatterns=[
   path('home',views.home),

   path('contact',views.contact),
   path('con',views.con),
   path('about',views.about),
   path('ourservice',views.ourservice),
   path('gallery',views.gallery),
      
   path('doctorreg',views.doctorreg),
   path('docreg',views.docreg),
   path('doctorlog',views.doctorlog),
   path('doclog',views.doclog),

   path('signout',views.signout),  
     
   path('docshow',views.docshow),
   path('docdelete/<int:id>',views.docdelete),
   path('docedit/<int:id>',views.docedit),
   path('docedcode/<int:id>',views.docedcode),
      
   path('patientreg',views.patientreg),
   path('patreg',views.patreg),
   path('patientlog',views.patientlog),
   path('patlog',views.patlog), 
   
   path('doclist',views.doclist),
   path('timing',views.timing),
   path('docbook',views.docbook),
  
   path('patshow',views.patshow),
   path('patdelete/<int:id>',views.patdelete),
   path('patedit/<int:id>',views.patedit),
   path('patedcode/<int:id>',views.patedcode),  
    
   path('booking',views.docbooking),
   path('dbk',views.dbk),
   
   path('bookshow',views.bookshow),
   path('bkdelete/<int:id>',views.bkdelete),
   path('bkedit/<int:id>',views.bkedit),
   path('edbk/<int:id>',views.edbk),
   
   path('apporment',views.apporment),
   path('update/<int:id>',views.update),   
   path('upd',views.upd),
   # path('updelete/<int:id>',views.updelete),
   
   path('patdetails',views.patdetails),
   
   path('medical',views.medical),
   path('med',views.med),

   path('docsearch',views.docsearch),

  path('postComment', views.postComment),
  path('blogHome',views.blogHome),  
  path('search', views.search, name="search"),  
  path('<str:slug>', views.blogPost),  
]