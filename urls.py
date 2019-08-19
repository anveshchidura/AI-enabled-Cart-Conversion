from django.urls import path
from. import views

app_name="dell"

urlpatterns = [
	
	#path("",views.homepage,name="homepage"),
	path("",views.home),
	# path("midpage/",views.midpage),
	path("bum/",views.bumbum),


]	