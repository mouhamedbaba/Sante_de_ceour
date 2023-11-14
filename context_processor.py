from avatar.models import Avatar
from administration.models import Site

def all_context(request):
    user = request.user
    try :
        site = Site.objects.get(pk = 1)
    except Site.DoesNotExist :
        site = None
    try :
        avatar = Avatar.objects.get(user = user.pk, primary = 1)
        print(avatar)
    except Avatar.DoesNotExist :
        avatar = None
        print(avatar)
    context = {
        'avatar' : avatar,
        'site' : site,
        'path' : request.path
    }
    return context