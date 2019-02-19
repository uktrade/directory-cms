def inherit_tags_from_parent(sender, instance, *args, **kwargs):
    parent = instance.get_parent().specific
    if hasattr(parent, 'tags'):
        instance.tags.add(*parent.tags.all())


def tags_propagate_to_descendants(sender, instance, action, *args, **kwargs):
    if action == 'post_add':
        for child in instance.get_children():
            child.specific.tags.add(*instance.tags.all())
            child.specific.save()
            # save shouldn't be necessary if you use add but, in this case,
            # it doesn't seem to be working without it
