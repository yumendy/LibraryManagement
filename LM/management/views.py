from django.shortcuts import render, render_to_response
from django.template import Context, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import *


def get_type_list():
	book_list = Book.objects.all()
	type_list = set()
	for book in book_list:
		type_list.add(book.typ)
	return list(type_list)


def index(req):
	username = req.session.get('username', '')
	if username:
		user = MyUser.objects.get(user__username=username)
	else:
		user = ''
	content = {'active_menu': 'homepage', 'user': user}
	return render_to_response('index.html', content)


def signup(req):
	if req.session.get('username', ''):
		return HttpResponseRedirect('/')
	status = ''
	if req.POST:
		post = req.POST
		passwd = post.get('passwd', '')
		repasswd = post.get('repasswd', '')
		if passwd != repasswd:
			status = 're_err'
		else:
			username = post.get('username', '')
			if User.objects.filter(username=username):
				status = 'user_exist'
			else:
				newuser = User.objects.create_user(username=username, password=passwd, email=post.get('email', ''))
				newuser.save()
				new_myuser = MyUser(user=newuser, nickname=post.get('nickname'), permission=1)
				new_myuser.save()
				status = 'success'
	content = {'active_menu': 'homepage', 'status': status, 'user': ''}
	return render_to_response('signup.html', content, context_instance=RequestContext(req))


def login(req):
	if req.session.get('username', ''):
		return HttpResponseRedirect('/')
	status = ''
	if req.POST:
		post = req.POST
		username = post.get('username', '')
		password = post.get('passwd', '')
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				auth.login(req, user)
				req.session['username'] = username
				return HttpResponseRedirect('/')
			else:
				status = 'not_active'
		else:
			status = 'not_exist_or_passwd_err'
	content = {'active_menu': 'homepage', 'status': status, 'user': ''}
	return render_to_response('login.html', content, context_instance=RequestContext(req))


def logout(req):
	auth.logout(req)
	return HttpResponseRedirect('/')


def setpasswd(req):
	username = req.session.get('username', '')
	if username != '':
		user = MyUser.objects.get(user__username=username)
	else:
		return HttpResponseRedirect('/login/')
	status = ''
	if req.POST:
		post = req.POST
		if user.user.check_password(post.get('old', '')):
			if post.get('new', '') == post.get('new_re', ''):
				user.user.set_password(post.get('new', ''))
				user.user.save()
				status = 'success'
			else:
				status = 're_err'
		else:
			status = 'passwd_err'
	content = {'user': user, 'active_menu': 'homepage', 'status': status}
	return render_to_response('setpasswd.html', content, context_instance=RequestContext(req))


def addbook(req):
	username = req.session.get('username', '')
	if username != '':
		user = MyUser.objects.get(user__username=username)
	else:
		return HttpResponseRedirect('/login/')
	if user.permission < 2:
		return HttpResponseRedirect('/')
	status = ''
	if req.POST:
		post = req.POST
		newbook = Book(
			name=post.get('name',''), \
			author=post.get('author',''), \
			typ=post.get('typ',''), \
			price=post.get('price', ''), \
			pubDate=post.get('pubdate', ''), \
			)
		newbook.save()
		status = 'success'
	content = {'user': user, 'active_menu': 'addbook', 'status': status}
	return render_to_response('addbook.html', content, context_instance=RequestContext(req))


def viewbook(req):
	username = req.session.get('username', '')
	if username != '':
		user = MyUser.objects.get(user__username=username)
	else:
		user = ''
	type_list = get_type_list()
	book_type = req.GET.get('typ', 'all')
	if book_type == '':
		book_lst = Book.objects.all()
	elif book_type not in type_list:
		book_type = 'all'
		book_lst = Book.objects.all()
	else:
		book_lst = Book.objects.filter(typ=book_type)

	if req.POST:
		post = req.POST
		keywords = post.get('keywords','')
		book_lst = Book.objects.filter(name__contains=keywords)
		book_type = 'all'

	paginator = Paginator(book_lst, 5)
	page = req.GET.get('page')
	try:
		book_list = paginator.page(page)
	except PageNotAnInteger:
		book_list = paginator.page(1)
	except EmptyPage:
		book_list = paginator.page(paginator.num_pages)

	content = {'user': user, 'active_menu': 'viewbook', 'type_list': type_list, 'book_type': book_type, 'book_list': book_list}
	return render_to_response('viewbook.html', content, context_instance=RequestContext(req))


def detail(req):
	username = req.session.get('username','')
	if username != '':
		user = MyUser.objects.get(user__username=username)
	else:
		user = ''
	Id = req.GET.get('id','')
	if Id == '':
		return HttpResponseRedirect('/viewbook/')
	try:
		book = Book.objects.get(pk=Id)
	except:
		return HttpResponseRedirect('/viewbook/')
	img_list = Img.objects.filter(book=book)
	content = {'user': user, 'active_menu': 'viewbook', 'book': book, 'img_list':img_list}
	return render_to_response('detail.html', content)