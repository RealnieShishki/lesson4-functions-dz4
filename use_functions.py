
def my_account():
    account = 0
    purchase_hystory = {}
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню: ')

        if choice == '1':
            deposit = int(input('Введите сумму пополнения: '))
            account += deposit
            pass
        elif choice == '2':
            purchase_sum = int(input('Введите сумму покупки: '))
            if purchase_sum >= account:
                print('Суммы на вашем счете не достаточно!')
            else:
                purchase_name = input('Введите название покупки: ')
                account -= purchase_sum
                purchase_h = {purchase_name: purchase_sum}
                purchase_hystory.update(purchase_h)
            pass
        elif choice == '3':
            for i in purchase_hystory.items():
                print(i)
            pass
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')


my_account()



# В задании этого нет, но если название покупки будет совпадать то код работать будет не корректно.
# Реализовать можно так, при добавлении ключ\значение в словарь, проверять на присутствие идиентичного ключа и складывать значения в случае успеха,