from users.models import UserProfile, CREATED


def set_status_for_new_users(sender, instance, created, *args, **kwargs):
    if created:
        profile = UserProfile(user_id=instance.id,
                              assignment_status=CREATED)
        profile.save()
