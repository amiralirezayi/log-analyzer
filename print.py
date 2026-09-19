def print_user_report(list_extract_informatains):
    for info in list_extract_informatains:
        print(
            f'{info["username"]} ==> login:{info["login"]} logout:{info["logout"]} '
            f'countbuy:{info["count_buy"]} sum price:{info["sum_price"]}  '
            f'last login: {info["last_login"]} first login: {info["first_login"]}'
        )


def print_product_report(list_extract_products, por_foroshtarin_mahsol, kam_foroshtarin_mahsol):
    print("---------------------------------------------------------------")
    print(f'por forosh tarin: {por_foroshtarin_mahsol}')
    print(f'kam forosh tarin: {kam_foroshtarin_mahsol}')
    for mahsol in list_extract_products:
        print(f'{mahsol["product name"]} ==> tedad forosh : {mahsol["tedad frosh"]} majmoe forosh : {mahsol["majmoe daramad"]}')
    print("---------------------------------------------------------------")


def print_error_report(list_extract_error):
    print("----------------------------------------------------------------")
    for error in list_extract_error:
        print(f'error name: {error["error name"]} tedad : {error["tedad"]}')
    print("----------------------------------------------------------------")

def print_shomare_khate_kharab(list_khate_kharab):
    print("----------------------------------------------------------------")
    print(f'shomare khathay kharab: {list_khate_kharab}')
    print("----------------------------------------------------------------")