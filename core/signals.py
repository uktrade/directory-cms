from core import models


def create_image_hash(sender, instance, *args, **kwargs):
    content_hash = models.ImageHash.generate_content_hash(instance.file)
    if not models.ImageHash.objects.filter(content_hash=content_hash).exists():
        models.ImageHash.objects.create(
            image=instance,
            content_hash=content_hash,
        )


def create_historic_slug(sender, instance, *args, **kwargs):
    models.HistoricSlug.objects.get_or_create(
        slug=instance.slug,
        page=instance
    )


def assign_service_to_page(sender, instance, created, *args, **kwargs):
    if created:
        models.Service.objects.get_or_create(
            slug=instance.view_app,
            page=instance
        )
