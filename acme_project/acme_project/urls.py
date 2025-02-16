from django.views.generic.edit import CreateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, reverse_lazy
from django.contrib.auth import logout
from django.shortcuts import redirect
from .forms import CustomUserCreationForm
def custom_logout(request):
    logout(request)
    return redirect('login')  # Перенаправление на страницу входа

urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('birthday/', include('birthday.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('logout/', custom_logout, name='logout'),
    path(
            'auth/registration/',
            CreateView.as_view(
                template_name='registration/registration_form.html',
                form_class=CustomUserCreationForm,
                success_url=reverse_lazy('pages:homepage'),
            ),
            name='registration',
        ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'core.views.page_not_found'
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)