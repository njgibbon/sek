from enum import Enum


class CheckResult(str, Enum):
    PASS = "PASS"  # nosec
    FAIL = "FAIL"
    ERROR = "ERROR"
    SKIP = "SKIP"
