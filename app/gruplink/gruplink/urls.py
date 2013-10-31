from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'main.views.home'),
    url(r'^agregar_seccion', 'main.views.add_section'),
    url(r'^actualizar_secciones', 'main.views.update_sections'),
    url(r'^borrar_seccion/(?P<identification>\d+)$', 'main.views.delete_section'),
    # url(r'^gruplink/', include('gruplink.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
