from avatar.models import Avatar
from administration.models import Site

def all_context(request):
    user = request.user
    try :
        site = Site.objects.get(pk = 1)
    except Site.DoesNotExist :
        site = None
    try :
        avatar = Avatar.objects.get(pk = user.pk)
    except Avatar.DoesNotExist :
        avatar = None
    context = {
        'avatar' : avatar,
        'site' : site
    }
    return context