from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from .views import home, single_page, category, author

urlpatterns = [
    path('', home , name = 'home'),
    path('post/<int:id>', single_page , name = 'single_page'),
    path('category/<name>', category , name = 'category'),
    path('author/<int:id>', author , name = 'author'),
    # path('widget', widget, name = 'Widget'),
]


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)