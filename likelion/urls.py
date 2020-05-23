from django.contrib import admin
from django.urls import path
import workout.views
import blog.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wordcoung',workout.views.home, name = "home"),
    path('about',workout.views.about, name = "about"),
    path('result/',workout.views.result, name = "result"),
    
    path('',blog.views.list, name = "list"),
    path('blog/<int:blog_id>',blog.views.detail, name = "detail"),
    path('blog/new',blog.views.new, name = "new"),
    path('blog/create',blog.views.create, name = "create"),
    path('blog/edit/<int:blog_id>',blog.views.edit, name = "edit"),
    path('blog/update/<int:blog_id>',blog.views.update, name = "update"),
    path('blog/delete/<int:blog_id>',blog.views.delete, name = "delete"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
