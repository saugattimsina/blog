
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import  settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogging/', include('blogging.urls')),
    path('accounts/', include('accounts.urls')),

]

urlpatterns += staticfiles_urlpatterns(

)

urlpatterns += static(settings.MEDIA_URL, ducoment_root=settings.MEDIA_ROOT)
