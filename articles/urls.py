from django.urls import path ,include
from .import views
urlpatterns = [
     path('',views.ArticleListView.as_view(),name='home'),
      path('add/',views.ArticleCreateView.as_view(),name='add'),
       path('details/<int:pk>',views.ArticleDetailView.as_view(),name='details'),
        path('addcomment/<int:pk>',views.ArticleCommentView.as_view(),name='Addcomment'),
       path('edit/<int:pk>',views.ArticleUpdateView.as_view(),name='edit'),
       path('delete/<int:pk>',views.ArticleDeleteView.as_view(),name='delete'),
        path('comment/<int:id>',views.addcomment,name='comment'),
         path('about',views.about,name='about'),


]
