from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HackMe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'Consultorio.views.get_all', name='paciente_list'),
    url(r'^nuevo$', 'Consultorio.views.crear_paciente', name='nuevo_px'),
    url(r'^editar/(?P<pk>\d+)$', 'Consultorio.views.update_paciente', name='editar_paciente'),
    url(r'^borrar/(?P<pk>\d+)$', 'Consultorio.views.delete_paciente', name='borrar_paciente'),

    url(r'^admin/', include(admin.site.urls)),
)
