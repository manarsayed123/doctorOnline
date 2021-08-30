def upload_user_image(instance, filename):
    return 'users/{0}/{1}'.format(instance.id, filename)
