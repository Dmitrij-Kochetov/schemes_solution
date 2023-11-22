from src.application.services.schemes_searcher.validators import validator
from src.application.services.schemes_searcher.types import Type


def test_validator_date_first() -> None:
    date = "1984-12-10"
    assert validator.validate(date) is Type.date


def test_validator_date_second() -> None:
    date = "10.12.1984"
    assert validator.validate(date) is Type.date


def test_validator_date_unformatted() -> None:
    date = "10111984"
    assert validator.validate(date) is not Type.date


def test_validator_email() -> None:
    email = "foo@bar.com"
    assert validator.validate(email) is Type.email


def test_validator_not_email() -> None:
    email = "foo_bar.com"
    assert validator.validate(email) is not Type.email


def test_validator_phone_number() -> None:
    number = "+7 911 233 54 11"
    assert validator.validate(number) is Type.phone_number


def test_validator_not_phone_number() -> None:
    number = "+49 655 344 22 91"
    assert validator.validate(number) is not Type.phone_number


def test_validator_text() -> None:
    number = "+49 655 344 22 91"
    assert validator.validate(number) is Type.text
