"""Restaurant URL Configuration

Список `urlpatterns` визначає маршрути URL-адрес до подань.
    Для отримання додаткової інформації, будь ласка, зверніться до:
        https://docs.djangoproject.com/en/4.1/topics/http/urls

    Приклади:
        Function views (Подання функцій)
            1. Add an import: from my_app import views (Додати import: from my_app імпортувати views)
            2. Add a URL to urlpatterns:  path('', views.home, name='home')
                (Додайте URL-адресу до urlpatterns: path('', views.home, name='home'))

        Class-based views (Погляди на основі класів)
            1. Add an import: from other_app.views import Home (Додати import: from other_app.views import Home)
            2. Add a URL to urlpatterns: path('', Home.as_view(), name='home')
                (Додайте URL-адресу до urlpatterns: path('', Home.as_view(), name='home'))

        Including another URLconf (Включно з іншим URLconf)
            1. Import the include() function: from django.urls import include, path
                (Імпортуйте функцію include(): from django.urls import include, path)
            2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
                (Додайте URL-адресу до шаблонів urlpatterns: path('blog/', include('blog.urls')))
"""

from django.contrib import admin
from django.urls import path, include

from main_page.views import main_page

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", main_page),
    path("account/", include("account.urls")),
    path("", include("main_page.urls")),
]
