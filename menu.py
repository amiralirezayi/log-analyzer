from print import print_user_report , print_product_report , print_error_report , print_shomare_khate_kharab


def show_menu():
    print()
    print("=================== Menu ===================")
    print("1. User Reports")
    print("2.Product Analysis")
    print("3.Error Reporting ")
    print("4.Numbers of faulty lines")
    print("0. Exit")
    print("============================================")


def run_menu(list_extract_informatains,list_extract_products,por_foroshtarin_mahsol,kam_foroshtarin_mahsol,list_extract_error,list_khate_kharab):
    while True:
        show_menu()
        choice = input("Enter the desired option:").strip()

        if choice == "1":
            print_user_report(list_extract_informatains)

        elif choice == "2":
            print_product_report(list_extract_products,por_foroshtarin_mahsol,kam_foroshtarin_mahsol)

        elif choice == "3":
            print_error_report(list_extract_error)

        elif choice == "4":
            print_shomare_khate_kharab(list_khate_kharab)

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid option, please try again.")