from groups import models


def create_groupinfo_for_new_group(sender, instance, **kwargs):
    if kwargs['created']:
        instance.info = models.GroupInfo.objects.create(
            group=instance, name_singular=instance.name
        )
