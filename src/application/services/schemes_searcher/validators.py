import phonenumbers
import email_validator
from datetime import datetime

from src.application.services.schemes_searcher.types import Type


class Validator:
    def _validate_date(self, data: str) -> bool:
        for fmt in ("%Y-%m-%d", "%d.%m.%Y"):
            try:
                _ = datetime.strptime(data, fmt)
                return True
            except ValueError:
                pass
        return False

    def _validate_number(self, data: str) -> bool:
        if data[:2] != "+7":
            return False
        try:
            _ = phonenumbers.parse(data, region="RU")
            return True
        except phonenumbers.NumberParseException:
            return False

    def _validate_email(self, data: str) -> bool:
        try:
            _ = email_validator.validate_email(data)
            return True
        except email_validator.EmailNotValidError:
            return False

    def validate(self, data: str) -> str:
        print(data)
        if self._validate_date(data):
            return Type.date

        if self._validate_number(data):
            return Type.phone_number

        if self._validate_email(data):
            return Type.email

        return Type.text


validator = Validator()
