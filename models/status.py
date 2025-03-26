from enum import Enum


class StatusEnum(str, Enum):
    PENDING = 'pending'
    APPROVED = 'approved'
    FAILED = 'failed'