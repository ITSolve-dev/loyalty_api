from enum import Enum


class RoleType(str, Enum):
    DEVELOPER = "DEVELOPER"
    EMPLOYEE = "EMPLOYEE"
    OWNER = "OWNER"
    CUSTOMER = "CUSTOMER"
