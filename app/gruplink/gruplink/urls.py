from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'main.views.home'),
    url(r'^logout', 'main.views.logout'),
    url(r'^administrador', 'main.views.load_admin'),
    
    url(r'^agregar_seccion', 'main.views.add_section'),
    url(r'^actualizar_secciones', 'main.views.update_sections'),
    url(r'^borrar_seccion/(?P<identification>\d+)$', 'main.views.delete_section'),
    
    url(r'^agregar_slide', 'main.views.add_slide'),
    url(r'^actualizar_slide', 'main.views.update_slide'),
    url(r'^eliminar_slide/(?P<identification>\d+)$', 'main.views.delete_slide'),
    # url(r'^gruplink/', include('gruplink.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^i18n/', include('django.conf.urls.i18n')),

)

urlpatterns += i18n_patterns('',
    url(r'^$', 'main.views.home'),
)
