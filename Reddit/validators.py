from django.core.validators import RegexValidator


class CustomValidators:
    """Custom validators"""
    letters_only = RegexValidator(
        r'^[a-zA-Z]*$',
        "Only letters are allowed",
        "You can use letters only"
    )
