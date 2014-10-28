from django.conf.urls import patterns, url
import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^$', views.get_all, name='paciente_list'),
    #url(r'^new$', views.crear_paciente, name='nuevo_px'),
    #url(r'^editar/(?P<pk>\d+)$', views.update_paciente, name='editar_paciente'),
    #url(r'^borrar/(?P<pk>\d+)$', views.delete_paciente, name='borrar_paciente'),
)