from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse,HttpResponseRedirect
from barberapp.models import*
import os
import random
import string
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

def index(request):
	return render(request,'index.html')

def about(request):
	return render(request,'about.html')

def codes(request):
	return render(request,'codes.html')

def contact(request):
	bid=request.GET['bid']
	bdetails=barber_register.objects.all().filter(id=bid)
	return render(request,'contact.html',{'bd':bdetails})

def gallery(request):
	q=barber_register.objects.all()
	print(q)
	return render(request,'gallery.html',{'data':q})

def icons(request):
	return render(request,'icons.html')

def single(request):
	return render(request,'single.html')

def barber(request):
	pdata=service_register.objects.all()
	return render(request,'barber.html',{'query':pdata})

def userreg(request):
	return render(request,'userreg.html')

def userlog(request):
	return render(request,'userlog.html')

def barberlog(request):
	return render(request,'barberlog.html')

def userdata(request):
	if request.method == 'POST':
		var_name= request.POST['name']
		var_email= request.POST['email']
		var_phone= request.POST['phone']
		var_password= request.POST['password']

		Query=user_register(name=var_name,email=var_email,phone=var_phone,password=var_password)
		Query.save()
		return render(request,'index.html')
	else:
		return render(request,'userreg.html')


def barberdata(request):
	if request.method == 'POST':
		var_img=request.FILES['fileupload']
		var_name= request.POST['name']
		var_email= request.POST['email']
		var_phone= request.POST['phone']
		var_password= request.POST['password']
		var_servicename= request.POST['servicename']
		
		pid=service_register.objects.get(id=var_servicename)
		pdata=service_register.objects.all().filter(id=var_servicename)
		print(pdata,"=================")


		Query=barber_register(name=var_name,email=var_email,phone=var_phone,password=var_password,Image=var_img,servicename=pid)
		Query.save()
		return render(request,'index.html')
	else:
		return render(request,'barber.html',{'query':query})

def userlogin(request):
	if request.method == 'POST':
		var_email= request.POST['email']
		var_password= request.POST['Password']
		lquery=user_register.objects.all().filter(email=var_email,password=var_password)
		if lquery:
			for x in lquery:
				request.session['userid']=x.id
				request.session['forview']=x.id
				user_id=request.session['userid']

			return render(request,'index.html')
		else:
			return render(request,'index.html')
	else:
		return render(request,'index.html')

def barberlogin(request):
	if request.method == 'POST':
		var_email= request.POST['email']
		var_password= request.POST['password']
		lquery=barber_register.objects.all().filter(email=var_email,password=var_password)
		if lquery:
			for x in lquery:
				request.session['barberid']=x.id
				request.session['forview']=x.id
				user_id=request.session['barberid']

			return render(request,'admin/barberindex.html')
		else:
			return render(request,'admin/barber.html')
	else:
		return render(request,'barberlog.html')

def logout(request):
	if request.session.has_key('userid'):
		del request.session['userid']
		del request.session['forview']
		return render(request,'index.html')
	elif request.session.has_key('barberid'):
		del request.session['barberid']
		del request.session['forview']
		return render(request,'index.html')

	elif request.session.has_key('adminid'):
		del request.session['adminid']
		del request.session['forview']

		return render(request,'index.html')
	else:

		return render(request,'userlog.html')



def booking(request):
	if request.session.has_key('userid'):
		if request.method == 'POST':
			var_date= request.POST['date']
			var_time= request.POST['time']
			var_barbername= request.POST['barber']
			pid=barber_register.objects.get(id=var_barbername)
			Query=barber_register.objects.all().filter(id=var_barbername)

			for x in Query:
				var_name=x.name
				var_email=x.email

			username=request.session['userid']
			cid=user_register.objects.get(id=username)
			x = ''.join(random.choices(var_name + string.digits, k=8))
			y = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
			subject = 'welcome to Whats App'
			message = f'Hi {var_name}, thank you for registering in Our Shop. your user username: {var_name} and  email: {var_email}. Follow https://Wa.me/+18478527243 or https://www.tinder.com'
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [var_email, ]
			send_mail( subject, message, email_from, recipient_list )
			# Query=barber_register.objects.all().filter(id=barber_id)

			Query=booking_register(username=cid,barbername=pid,date=var_date,time=var_time)
			Query.save()
		return render(request,'index.html')
	else:
		return render(request,'userlog.html')

def table(request):
	if request.session.has_key('barberid'):
		barber_id=request.session['barberid']
		Query=booking_register.objects.all().filter(id=barber_id)
		return render(request,'table.html',{'data':Query})
	else:
		return render(request,'table.html')

def approve(request):
	barber_id=request.GET['fid']
	q=booking_register.objects.all().filter(id=barber_id).update(status="Approved")
	return HttpResponseRedirect('/table/')

def cancel(request):
	barber_id=request.GET['fid']
	q=booking_register.objects.all().filter(id=barber_id).update(status="cancelled")
	return HttpResponseRedirect('/table/')


def adminindex(request):
	return render(request,'admin/index.html')

def cards(request):
	return render(request,'admin/cards.html')

def blocks(request):
	return render(request,'admin/blocks.html')

def carousels(request):
	return render(request,'admin/carousels.html')

def forms(request):
	return render(request,'admin/forms.html')

def people(request):
	return render(request,'admin/people.html')

def pricing(request):
	return render(request,'admin/pricing.html')

def adminlogin(request):
	return render(request,'admin/adminlogin.html')

def adminlog(request):
	if request.method == 'POST':
		var_email= request.POST['email']
		var_password= request.POST['Password']
		lquery=User.objects.all().filter(email=var_email,password=var_password)
		if lquery:
			for x in lquery:
				request.session['adminid']=x.id
				request.session['forview']=x.id
				adminid=request.session['adminid']

			return render(request,'admin/index.html')
		else:
			return render(request,'admin/adminlogin.html')
	else:
		return render(request,'admin/adminindex.html')

def usertable(request):
	q=user_register.objects.all()	
	return render(request,'admin/usertable.html',{'data':q})

def barbertable(request):
	q=barber_register.objects.all()	
	return render(request,'admin/barbertable.html',{'data':q})

def bookingtable(request):
	q=booking_register.objects.all()	
	return render(request,'admin/bookingtable.html',{'data':q})


def addservices(request):
	return render(request,'admin/addservices.html')

def addservice(request):
	if request.method == 'POST':
		var_name= request.POST['servicename']

		Query=service_register(servicename=var_name)
		Query.save()
		return render(request,'admin/addservices.html')
	else:
		return render(request,'userreg.html')


def barberorder(request):
	if request.session.has_key('barberid'):
		barberid=request.session['barberid']
		Query=booking_register.objects.all().filter(barbername=barberid)
		return render(request,'admin/bookingtable.html',{'data':Query})
	else:
		return render(request,'index.html')

def mybookings(request):
	if request.session.has_key('userid'):
		userid=request.session['userid']
		Query=booking_register.objects.all().filter(username=userid)
		return render(request,'mybookings.html',{'data':Query})
	else:
		return render(request,'index.html')
	

def barberindex(request):
	return render(request,'admin/barberindex.html')

def changepassword(request):
	# user_id=request.GET['uid']
	# print(user_id,'11111111111111111111')
	# user=user_register.objects.filter(id=user_id)
	# for x in user:
	# 	password=x.password
	# 	print(password,'#######')

	if request.method == 'POST':
		user_id=request.session['userid']
		# print(user_id,'11111111111111111111')

		user=user_register.objects.filter(id=user_id)
		for x in user:
			password=x.password
			print(password,'#######')

		oldpassword= request.POST['oldpassword']
		newpassword= request.POST['newpassword']
		confirmPassword= request.POST['confirmPassword']
		if password == oldpassword:
			if newpassword==confirmPassword:
				user_register.objects.filter(id=user_id).update(password=newpassword)
				return HttpResponseRedirect('/logout/')
			else:
				return render(request,'changepassword.html',{'msg': "newpassword and confirmPassword doesn't match"})
		else:
			return render(request,'changepassword.html',{'msg': "  oldpassword doesn't match"})
		return render(request,'changepassword.html')
	return render(request,'changepassword.html')

def userdetials(request):
	userid=request.session['userid']
	q=user_register.objects.filter(id=userid)
	return render(request,'userdetials.html',{'data':q})

def barberbooking(request):
	if request.session.has_key('barberid'):
		barberid=request.session['barberid']
		Query=booking_register.objects.all().filter(barbername=barberid)
		return render(request,'admin/barberbooking.html',{'data':Query})
	else:
		return render(request,'index.html')



	























	
		








