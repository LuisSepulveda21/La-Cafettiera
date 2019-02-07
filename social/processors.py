# creacion de diccionario que puede ser usado en cualquier view-template
from .models import Link


def ctx_dict(request):
    ctx = {}
    links = Link.objects.all()
    for link in links:
        # {'link_key':'link'}
        ctx[link.key] = link.url
    return ctx
