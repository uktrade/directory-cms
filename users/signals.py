from users.models import UserProfile


def set_status_for_new_users(sender, instance, created, *args, **kwargs):
    if created:
        profile = UserProfile(user_id=instance.id,
                              assignment_status=UserProfile.CREATED)
        profile.save()
