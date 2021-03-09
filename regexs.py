import re

nospace = re.compile(r"[^\s]+")

quotation = re.compile(r"\"[A-Za-z]+\"")

twonum = re.compile(r"([-]?[0-9]+[.]?[0-9]*)([\\,])+([-]?[0-9]+[.]?[0-9]*)")

likely_name = re.compile(r"[A-Z][a-z]+[\s][A-Z][a-z]+[\s]([A-Z][a-z]*)?|[A-Z][.][\s][A-Z][a-z]+[\s]([A-Z][a-z]*)?")
