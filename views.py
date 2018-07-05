from django.shortcuts import render, redirect
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .models import Article

# Create your views here.

def index(request):
	var= Article.objects.all()
	paginator = Paginator(var,2)
	page = request.GET.get('page')
	try:
		p = paginator.page(page)
	except PageNotAnInteger:
		p = paginator.page(1)
	except EmptyPage:
		p = paginator.page(paginator.num_pages)
	return render(request,"index.html",{"var":p})

def detail(request,i_id):
	myarticle = Article.objects.all().filter(pk=i_id)

	return render(request,'second.html',{'var':myarticle})