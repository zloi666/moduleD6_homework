from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from library import views
from library.views import AuthorEdit, AuthorList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.books_list),
    path('index/', views.index),
    path('index/book_increment/', views.book_increment),
    path('index/book_decrement/', views.book_decrement),
    path('publishers/', views.publisher),
    path('library/', include('library.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)