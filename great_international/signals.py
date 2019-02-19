def inherit_tags_from_parent(sender, instance, *args, **kwargs):
    parent = instance.get_parent().specific
    if hasattr(parent, 'tags'):
        instance.tags.add(*parent.tags.all())
