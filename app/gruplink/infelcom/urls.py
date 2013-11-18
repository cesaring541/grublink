from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns


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


    url(r'^/proyecto/nuevo$', 'infelcom.views.load_project_form'),
    url(r'^/proyecto/(?P<identification>\d+)$', 'infelcom.views.load_project'),
    url(r'^/agregar_proyecto', 'infelcom.views.add_project'),
    url(r'^/actualizar_proyecto/(?P<identification>\d+)$', 'infelcom.views.update_project'),
    url(r'^/eliminar_proyecto/(?P<identification>\d+)$', 'infelcom.views.delete_project'),

    url(r'^/producto/nuevo$', 'infelcom.views.load_product_form'),
    url(r'^/producto/(?P<identification>\d+)$', 'infelcom.views.load_product'),
    url(r'^/agregar_producto', 'infelcom.views.add_product'),
    url(r'^/actualizar_producto/(?P<identification>\d+)$', 'infelcom.views.update_product'),
    url(r'^/eliminar_producto/(?P<identification>\d+)$', 'infelcom.views.delete_product'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

)