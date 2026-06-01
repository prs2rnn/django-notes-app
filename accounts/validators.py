from django.core.exceptions import ValidationError


def validate_avatar_size(file):
    max_size = 5 * 1024 * 1024

    if file.size > max_size:
        raise ValidationError('Image must be smaller than 5 MB')


def validate_avatar_extension(file):
    allowed_extensions = ('.jpg', '.jpeg', '.png', '.webp', '.gif')

    if not file.name.lower().endswith(allowed_extensions):
        raise ValidationError('Only JPG, PNG, GIF and WebP are allowed')
