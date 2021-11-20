from enum import IntEnum


class EntityType(IntEnum):

    post = 0

    comment = 1


class ReasonType(IntEnum):
    ITS_SPAM = 0
    SEXUAL_ACTIVITY = 1
    SALE_OF_ILLEGAL_OR_REGULATED_GOODS = 2
    SCAM_OR_FRAUD = 3
    FALSE_INFORMATION = 4

