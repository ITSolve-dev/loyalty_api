from core import DeclareModuleAppException, NotFoundInstanceException


class ScansException(DeclareModuleAppException):
    MODULE = "scans"


class LoyaltyTicketsException(DeclareModuleAppException):
    MODULE = "loyalty_tickets"


class ScansPermissionException(ScansException):
    ERROR = "permission_error"
    DESCRIPTION = "Such profile can scan that subject profile"


class LoyaltyTicketsNotFoundException(LoyaltyTicketsException, NotFoundInstanceException):
    pass
