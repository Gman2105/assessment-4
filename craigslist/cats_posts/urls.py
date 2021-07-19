#URL'S FOR cats_posts

from django.contrib  import admin
from django.urls     import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categories/', include('cp_app.urls')),
]
