def get_profile_data(backend, strategy, details, response, user=None, *args, **kwargs):
    url = None

    if backend.name == 'facebook':
        url = "http://graph.facebook.com/{}/picture?type=large".format(
            response['id']
        )

    if url:
        user.facebook_avatar = url
        user.save()
