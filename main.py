from views import *

def main():
    print('1 - CREATE, 2 - LISTING', '3 - RETRIEVE', '4 - UPDATE', '5 - DELETE','END - для завершения')
    choice = input('Выберите действие (1,2,3,4,5): ')
    if choice == '1':
        print(create_product())

    elif choice == '2':listing()
    elif choice == '3': retrieve_product()
    elif choice == '4':print(update_product())
    elif choice == '5':
        listing()
        print(delete_product())
    else:
        print()
        print('токого действия нет!')
        print()
        main()
              
flag = True
while flag:
    main()
    print()
    continue_ = input('Хотите продолжить работу?(yes/*any_key*)): ')
    print()
    if continue_ == 'yes':
        continue
    else:
        flag = False