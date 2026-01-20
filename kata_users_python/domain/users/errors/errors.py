class EmailAlreadyExistsError(Exception):
    """Raised when an specific email already exists"""


class EmailDomainAlreadyExistsError(Exception):
    """Raised when the email domain already exists"""


class UserNotFoundError(Exception):
    """Raised when the user is not found"""
