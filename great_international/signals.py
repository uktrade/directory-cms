def inherit_tags_from_parent(sender, instance, *args, **kwargs):
    parent = instance.get_parent().specific
    if hasattr(parent, 'tags'):
        instance.tags.add(*parent.tags.all())


def tags_propagate_to_descendants(sender, instance, action, *args, **kwargs):
    if action == 'post_add':
        for child in instance.get_children():
            if hasattr(child.specific, 'tags'):
                child.specific.tags.add(*instance.tags.all())
                child.specific.save()
