from core import models


def create_image_hash(sender, instance, *args, **kwargs):
    content_hash = models.ImageHash.generate_content_hash(instance.file)
    if not models.ImageHash.objects.filter(content_hash=content_hash).exists():
        models.ImageHash.objects.create(
            image=instance,
            content_hash=content_hash,
        )


def create_document_hash(sender, instance, *args, **kwargs):
    content_hash = models.DocumentHash.generate_content_hash(instance.file)
    if not models.DocumentHash.objects.filter(
        content_hash=content_hash
    ).exists():
        models.DocumentHash.objects.create(
            document=instance,
            content_hash=content_hash,
        )
