#!/usr/bin/env python3
"""
Regex-ing
"""
import re


def filter_datum(fields, redaction, message, separator):
    """
    returns the log message obfuscated:
    """
    pattern = r"(?:" + "|".join(fields) + r")=.*?" + separator
    return re.sub(pattern, lambda m: m.group(0).split(
        "=")[0] + "=" + redaction + separator, message)
