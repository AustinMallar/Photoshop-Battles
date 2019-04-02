from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from two_factor.urls import urlpatterns as tf_urls
from django.conf.urls import url
from two_factor.gateways.twilio.urls import urlpatterns as tf_twilio_urls

urlpatterns = [
    url(r'', include(tf_twilio_urls)),
    url(r'', include(tf_urls)),
    path('admin/', admin.site.urls),
    path('',include('application.urls',namespace='application')),
    path('account/',include('accounts.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)