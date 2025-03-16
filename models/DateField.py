from flask_restful import fields
from datetime import date

class DateField(fields.Raw):
    def format(self, value):
        if isinstance(value, date):
            return value.strftime("%Y-%m-%d")  # Formato ISO
        return None