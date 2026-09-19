VALID_STATUSES = ("SUCCESS", "FAILED")


def is_valid_log_line(log_line):
    if len(log_line) < 5:
        return False

    if log_line[4] not in VALID_STATUSES:
        return False
    return True


def is_valid_error_line(log_line):
    return len(log_line) >= 6 and log_line[5].startswith("ERROR_CODE=")


def is_valid_buy_details(details):
    if len(details) < 3:
        return False
    if not details[0].startswith("PRODUCT="):
        return False
    if not details[1].startswith("COUNT="):
        return False
    if not details[2].startswith("PRICE="):
        return False
    return True


def is_valid_buy_amounts(details):
    count_value = int(details[1][6:])
    price_value = int(details[2][6:])
    return count_value >= 0 and price_value >= 0


def find_invalid_line_numbers(content):

    invalid_line_numbers = []
    line_number = 0
    lines = content.split("\n")
    for raw_line in lines:
        line_number += 1
        line = raw_line.strip()

        if line == "":
            continue

        fields = line.split()

        if not is_valid_log_line(fields):
            invalid_line_numbers.append(line_number)
            continue

        if fields[2] == "ERROR" and not is_valid_error_line(fields):
            invalid_line_numbers.append(line_number)
            continue

        if fields[2] == "BUY" and not is_valid_buy_details(fields[5:]):
            invalid_line_numbers.append(line_number)
            continue

        if fields[2] == "BUY" and not is_valid_buy_amounts(fields[5:]):
            invalid_line_numbers.append(line_number)
            continue

    return invalid_line_numbers

