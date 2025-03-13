"""
Конфигурация URL для проекта MySite.
Список `urlpatterns маршрутирует URL -адреса для просмотров.
Для получения дополнительной информации,
пожалуйста, см.: Https: docs.djangoproject.comen4.2topicshttpurls
Примеры: Просмотры функций 1. Добавьте импорт: от My_app Import Views 2. Добавить URL в urlpatterns: path ('', views.home, имя = 'Home')
На основе класса. Home.as_view (), name = 'Home'), включая еще один UrlConf 1. Импортировать функцию include (): из Django.urls Import Incult, Path 2. Добавить URL в urlpatterns: path ('blog', include ('blog.urls')))
"""
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
