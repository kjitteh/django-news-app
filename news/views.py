from django.shortcuts import render

from . models import Article, Category

# Create your views here.

def index(request):
	categories = Category.objects.all()

	featured_1 = Article.objects.first()
	featured_2 = Article.objects.all()[1]
	featured_3 = Article.objects.all()[2]

	top_news = Article.objects.all()[3:6]
	sports_news = Article.objects.filter(category__title='Sports')
	science_news = Article.objects.filter(category__title='Science')
	technology_news = Article.objects.filter(category__title='Technology')
	context = {
		'categories': categories, 'featured_1': featured_1, 
		'featured_2': featured_2, 'featured_3': featured_3,
		'top_news': top_news, 'sports_news': sports_news,
		'science_news': science_news, 'technology_news': technology_news
	}
	return render(request, 'index.html', context)


def detail(request, pk):
	latest_news = Article.objects.all()[:5]
	categories = Category.objects.all()
	news = Article.objects.get(id=pk)
	context = {
		'categories': categories, 'news': news,
		'latest_news': latest_news
	}
	return render(request, 'detail.html', context)


def category(request, pk):
	categories = Category.objects.all()
	category = Category.objects.get(id=pk)
	category_news = Article.objects.filter(category=category)
	context = {
		'categories': categories, 'category_news': category_news, 
		'category': category
	}
	return render(request, 'category.html', context)

