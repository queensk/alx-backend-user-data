#!/usr/bin/env python3
"""
Regex-ing
"""
import re
from typing import List
import logging


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


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        log records using filter_datum.
        """
        record.msg = filter_datum(
            self.fields,
            self.REDACTION,
            record.getMessage(),
            self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)
