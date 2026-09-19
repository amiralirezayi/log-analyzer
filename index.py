from validation import is_valid_log_line , is_valid_error_line , is_valid_buy_details , is_valid_buy_amounts , find_invalid_line_numbers
from menu import run_menu

def read_text_file(get_file):
    file = open(get_file, "r")
    content = file.read()
    file.close()
    return content


def clean_lines(content):
    list_log = []
    for line in content.split("\n"):
        clean_line = line.strip()
        if clean_line == "":
            continue
        list_log.append(clean_line)
    return list_log


def tokenize_lines(list_log):
    list_log_parametr = []
    for log_line in list_log:
        log_parametr = log_line.split()
        list_log_parametr.append(log_parametr)
    return list_log_parametr


def build_log_dict(log_line):
    dic = {
        "date": "",
        "time": "",
        "event": "",
        "username": "",
        "status": "",
        "details": "",
    }

    dic["date"] = log_line[0]
    dic["time"] = log_line[1]
    dic["event"] = log_line[2]
    dic["username"] = log_line[3]
    dic["status"] = log_line[4]

    details = []
    if len(log_line) > 5:
        for c in range(5, len(log_line)):
            details.append(log_line[c])
        dic["details"] = details

    return dic


def build_logs_info(list_log_parametr):
    list_dic_info = []
    list_usernames = []
    list_error = []

    for log_line in list_log_parametr:

        if not is_valid_log_line(log_line):
            continue

        if log_line[2] == "ERROR":
            if not is_valid_error_line(log_line):
                continue
            if log_line[5][11:] not in list_error:
                list_error.append(log_line[5][11:])

        if log_line[3] not in list_usernames and log_line[3] != "system":
            list_usernames.append(log_line[3])

        dic = build_log_dict(log_line)

        if dic["event"] == "BUY":
            details = dic["details"]
            if not is_valid_buy_details(details):
                continue
            if not is_valid_buy_amounts(details):
                continue

        list_dic_info.append(dic)

    return list_dic_info, list_usernames, list_error


def build_user_stats(list_dic_info, list_usernames):
    list_extract_informatains = []
    for username in list_usernames:
        dic1 = {
            "username": "",
            "login": 0,
            "logout": 0,
            "count_buy": 0,
            "sum_price": 0,
            "first_login": "",
            "last_login": "",
        }
        dic1["username"] = username
        list_extract_informatains.append(dic1)

    for i in list_dic_info:
        if i["event"] == "LOGIN":
            for j in list_extract_informatains:
                if j["username"] == i["username"]:
                    j["login"] += 1
                    j["last_login"] = i["date"] + " " + i["time"]
                    if j["first_login"] == "":
                        j["first_login"] = i["date"] + " " + i["time"]

        if i["event"] == "LOGOUT":
            for j in list_extract_informatains:
                if j["username"] == i["username"]:
                    j["logout"] += 1

        if i["event"] == "BUY":
            for j in list_extract_informatains:
                if j["username"] == i["username"]:
                    j["count_buy"] += int(i["details"][1][6:])
                    j["sum_price"] += int(i["details"][2][6:]) * int(i["details"][1][6:])

    return list_extract_informatains


def build_product_stats(list_dic_info):
    products_list = []
    for i in list_dic_info:
        if i["event"] == "BUY" and i["details"][0][8:] not in products_list:
            products_list.append(i["details"][0][8:])

    list_extract_products = []
    for product in products_list:
        dic = {
            "product name": "",
            "tedad frosh": 0,
            "majmoe daramad": 0,
        }
        dic["product name"] = product
        list_extract_products.append(dic)

    for log in list_dic_info:
        if log["event"] == "BUY":
            for j in list_extract_products:
                if j["product name"] == log["details"][0][8:]:
                    j["tedad frosh"] += int(log["details"][1][6:])
                    j["majmoe daramad"] += int(log["details"][1][6:]) * int(log["details"][2][6:])

    return list_extract_products


def find_best_worst_product(list_extract_products):
    min_val = 0
    max_val = 0
    por_foroshtarin_mahsol = ""
    kam_foroshtarin_mahsol = ""

    for mahsol in list_extract_products:
        if mahsol["tedad frosh"] > max_val:
            max_val = mahsol["tedad frosh"]
            por_foroshtarin_mahsol = mahsol["product name"]

        if min_val == 0:
            min_val = mahsol["tedad frosh"]
            kam_foroshtarin_mahsol = mahsol["product name"]

        if mahsol["tedad frosh"] < min_val:
            min_val = mahsol["tedad frosh"]
            kam_foroshtarin_mahsol = mahsol["product name"]

    return por_foroshtarin_mahsol, kam_foroshtarin_mahsol


def build_error_stats(list_dic_info, list_error):
    list_extract_error = []
    for error in list_error:
        dic = {
            "error name": "",
            "tedad": 0,
        }
        dic["error name"] = error
        list_extract_error.append(dic)

    for log in list_dic_info:
        if log["event"] == "ERROR":
            for j in list_extract_error:
                if j["error name"] == log["details"][0][11:]:
                    j["tedad"] += 1

    return list_extract_error


content = read_text_file("log.txt")
list_log = clean_lines(content)
list_log_parametr = tokenize_lines(list_log)
list_dic_info, list_usernames, list_error = build_logs_info(list_log_parametr)
list_extract_informatains = build_user_stats(list_dic_info, list_usernames)
list_extract_products = build_product_stats(list_dic_info)
por_foroshtarin_mahsol, kam_foroshtarin_mahsol = find_best_worst_product(list_extract_products)
list_extract_error = build_error_stats(list_dic_info, list_error)
list_khate_kharab = find_invalid_line_numbers(content)

run_menu(list_extract_informatains ,list_extract_products ,por_foroshtarin_mahsol ,kam_foroshtarin_mahsol ,list_extract_error ,list_khate_kharab)