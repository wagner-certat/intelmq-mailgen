"""
This file provides a Key-Key Map for X-ARF-Keys and IntelMQ-Keys

This Mapping contains field which ar common for all X-ARF reports
"""

common_keys = [
    # X-ARF, IntelMQ
    ("Reported-From", None), # This is be the config["sender"] value from mailgen
    ("Report-ID", None), # This might be populated with the Ticketnumber generated by mailgen
    ("Date", "time.source"), # This maps to the time.source field, conversion from time.source to RFC 3339 is necessary or TODO check if time.source is always in RFC3339
    ("TLP", None), # Cannot be determined. Field is optional anyway...
    ("User-Agent", None), # This should not be mapped. Generating software would be mailgen
    ("Attachment", None), # This might be populated with a cleaned version of intelmqs "raw" field
    ("Version", None), # Optional field which should always be 0.2
    ("Occurences", None), # Cannot be determined. Field is optional anyway...
]


classification_taxonomy_xarf_map = [
    # Based on https://github.com/certtools/intelmq/blob/master/intelmq/bots/experts/taxonomy/expert.py
    ("Fraud", "Fraud"),
    ("Intrusion Attempts", "Login-Attack"),
    ("Malicious Code", "Malware-Attack"), # this might be to wide, maybe a stripdown to certain classification.types is required.
]
