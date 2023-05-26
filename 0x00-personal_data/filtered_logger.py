#!/usr/bin/env python3
"""
Regex-ing
"""
import re
from typing import List


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:
    """
    returns the log message obfuscated:
    """
    pattern = r"(?:" + "|".join(fields) + r")=.*?" + separator
    return re.sub(pattern, lambda m: m.group(0).split(
        "=")[0] + "=" + redaction + separator, message)
