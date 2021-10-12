from .models import Profile


def activate_user(backend, user, response, is_new=False, *args, **kwargs):
    if is_new:
        user.is_active = True
        user.save()


def save_profile_pic(backend, user, response, is_new=False, *args, **kwargs):
    if is_new and backend.name == "facebook":
        Profile.objects.filter(user=user).update(
            profile_pic='https://graph.facebook.com/{0}/picture/?type=large&access_token={1}'.format(response['id'],
                                                                                                     response[
                'access_token']))
    elif backend.name == 'google-oauth2':
        if is_new and response.get('picture'):
            Profile.objects.filter(user=user).update(
                profile_pic=response['picture'])
