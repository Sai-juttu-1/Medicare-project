"""Pure validation and cleaning functions for raw patient data.

YOUR JOB: complete every function marked TODO.
Each takes messy text in and returns a clean value out — or raises
InvalidRecordError explaining what is wrong.
(Module 4 functions + Module 9 exceptions, working together.)
"""


class InvalidRecordError(Exception):
    """Raised when a patient row cannot be repaired safely."""
    # Nothing to add — inheriting from Exception is enough (Module 9).


def clean_name(raw_name: str) -> str:
    """Return the name stripped of extra spaces, in Title Case.

    >>> clean_name("  priya sharma ")
    'Priya Sharma'

    Raise InvalidRecordError("name is missing") if the result is empty.
    """
    # TODO 1: strip spaces, apply .title(), handle the empty case
    return raw_name.strip().title()
    raise NotImplementedError


def parse_age(raw_age: str) -> int:
    """Convert age text to int; must be between 1 and 120.

    Raise InvalidRecordError for non-numbers ("abc") and out-of-range ages.
    HINT: wrap int(...) in try/except ValueError.
    """
    # TODO 2
    text = (raw_age or "").strip()
    try:
        age = int(raw_age)
    except ValueError:
        raise InvalidRecordError("Invalid age")    
    if 1<=age<=120 :
        return age
    else:            
        raise InvalidRecordError("enter valid age")
    

    


def parse_fee(raw_fee: str) -> float:
    """Convert a fee like '1,250.50' to 1250.50 (float).

    Steps: remove commas, strip spaces, reject empty / non-numeric /
    negative values with InvalidRecordError.
    """
    # TODO 3
    raw_fee = raw_fee.strip().replace(",", "")

    if not raw_fee:
        raise InvalidRecordError("Fee is empty")

    try:
        fee = float(raw_fee)
    except ValueError:
        raise InvalidRecordError("Invalid fee")

    if fee < 0:
        raise InvalidRecordError("Fee cannot be negative")

    return fee


def clean_department(raw_dept: str, default: str = "General") -> str:
    """Return the department in Title Case, or the default when blank.

    WHY a default: reception sometimes leaves the field empty; the
    clinic's rule is to file such visits under General.
    """
    # TODO 4 (two lines are enough)
    raw_dept = raw_dept.strip()
    return raw_dept.title() if raw_dept else default
    raise NotImplementedError
