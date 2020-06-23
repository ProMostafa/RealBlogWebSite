from django.shortcuts import render 
from django.http import HttpResponseRedirect
from django.views.generic import ListView ,DetailView
from django.views.generic.edit import CreateView ,UpdateView ,DeleteView
from django.urls import reverse_lazy

# Create your views here.

from .models import Article 

class ArticleListView(ListView):
	queryset= Article.objects.all().order_by("date")
	template_name='articles/home.html'
	context_object_name= 'objs'
	#print(context_object_name)
	# ListView allow for one object to send to change  override get_context_data
	# for passing 2 model must modifiy get_context_data to support 2 models
	'''
	def get_context_data(self, *args, **kwargs):
		context = super(ArticleListView, self).get_context_data(*args,**kwargs)
		context['comments'] = Comment.objects.all()
		print(Comment.objects.all())
		return context
'''

def AddComment(request):
	form=Article
	return render(request,'articles/comment.html',)


class ArticleCreateView(CreateView):
	model=Article
	template_name='articles/article.html'
	fields= '__all__'


# While this view is executing, self.object will contain the object that the view is operating
class ArticleDetailView(DetailView):
	model=Article
	template_name='articles/details.html'
	context_object_name= 'obj'  


class ArticleCommentView(DetailView):
	model=Article
	template_name='articles/comment.html'
	context_object_name= 'obj'

def addcomment(request,id):
	obj=Article.objects.get(id=id)
	obj.comment=request.POST['comment']
	obj.save()
	return HttpResponseRedirect('/')


class ArticleUpdateView(UpdateView):
	model=Article
	template_name='articles/edit.html'
	fields=['title','text']


class ArticleDeleteView(DeleteView):
	model=Article
	template_name='articles/delete.html'
	context_object_name='obj' 
	success_url=reverse_lazy('home')

def about(request):
	return render(request,'articles/about.html',)