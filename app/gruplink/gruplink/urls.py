from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    url(r'^admon/', include(admin.site.urls)),
    

    # Examples:
    url(r'^$', 'main.views.home'),
    url(r'^login$', 'main.views.login_admin'),

    url(r'^logout', 'main.views.logout_view'),
    url(r'^administrador', 'main.views.load_admin'),
    
    url(r'^agregar_seccion', 'main.views.add_section'),
    url(r'^actualizar_secciones', 'main.views.update_sections'),
    url(r'^borrar_seccion/(?P<identification>\d+)', 'main.views.delete_section'),
    
    url(r'^agregar_slide', 'main.views.add_slide'),
    url(r'^actualizar_slide', 'main.views.update_slide'),
    url(r'^eliminar_slide/(?P<identification>\d+)$', 'main.views.delete_slide'),
    
    url(r'^agregar_aspecto', 'main.views.add_aspect'),
    url(r'^actualizar_aspecto', 'main.views.update_aspect'),
    url(r'^eliminar_aspecto/(?P<identification>\d+)$', 'main.views.delete_aspect'),

    url(r'^actualizar_contenido', 'main.views.update_content'),



    url(r'^infelcom', include('infelcom.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),


    url(r'^i18n/', include('django.conf.urls.i18n')),

)

urlpatterns += i18n_patterns('',
    url(r'^$', 'main.views.home'),
    url(r'^infelcom', 'infelcom.views.home'),
)
