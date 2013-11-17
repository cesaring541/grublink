from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^/$', 'infelcom.views.home'),
    url(r'^/logout', 'infelcom.views.logout'),
    url(r'^/administrador', 'infelcom.views.load_admin'),
    
    url(r'^/agregar_seccion', 'infelcom.views.add_section'),
    url(r'^/actualizar_secciones', 'infelcom.views.update_sections'),
    url(r'^/borrar_seccion/(?P<identification>\d+)$', 'infelcom.views.delete_section'),
    
    url(r'^/agregar_slide', 'infelcom.views.add_slide'),
    url(r'^/actualizar_slide', 'infelcom.views.update_slide'),
    url(r'^/eliminar_slide/(?P<identification>\d+)$', 'infelcom.views.delete_slide'),
    
    url(r'^/agregar_aspecto', 'infelcom.views.add_aspect'),
    url(r'^/actualizar_aspecto', 'infelcom.views.update_aspect'),
    url(r'^/eliminar_aspecto/(?P<identification>\d+)$', 'infelcom.views.delete_aspect'),

    url(r'^/perfil/nuevo$', 'infelcom.views.load_profile_form'),
    url(r'^/perfil/(?P<identification>\d+)$', 'infelcom.views.load_profile'),
    url(r'^/agregar_miembro', 'infelcom.views.add_member'),
    url(r'^/actualizar_miembro/(?P<identification>\d+)$', 'infelcom.views.update_member'),
    url(r'^/eliminar_miembro/(?P<identification>\d+)$', 'infelcom.views.delete_member'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)