from django.core.exceptions import ValidationError
import datetime

def validate_year(year):
    try:
        y = int(year)
        if not (y >= 1900 and y <= datetime.datetime.now().year):
            raise ValidationError("Podano niepoprawny rok wydania")
    except ValueError:
        raise ValidationError("Podano niepoprawny rok wydania")