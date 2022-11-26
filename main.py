from time import sleep

from terminal import Terminal
from Seller import Salesman
from Order import Order
from Pizza import Pizza, PizzaBBQ, PizzaSeafood, PizzaPepperoni


current_terminal = Terminal()
current_terminal.add_dish_to_menu(Pizza())
current_terminal.add_dish_to_menu(PizzaBBQ())
current_terminal.add_dish_to_menu(PizzaPepperoni())
current_terminal.add_dish_to_menu(PizzaSeafood())


# # Включаем терминал
# terminal_activation = input("Хотите открыть смену?(да/нет)").lower().strip()
# while True:
#     if terminal_activation == 'да':
#         password = input("Введите пароль: ")
#         if password == 'admin14':
#             current_terminal.start_working(Salesman(input("Введите ФИО: ")))
#             break
#         else:
#             print("Неверный пароль!")
#             terminal_activation = ''
#     elif terminal_activation == 'нет':
#         print('Хорошего дня!')
#         break
#     else:
#         print('Неизвестная команда.')
#         terminal_activation = input("Хотите открыть смену?(да/нет)").lower().strip()

current_terminal.start_working(Salesman('Семёнов Данил Олегович'))
while current_terminal.activ:
    sleep(1)
    current_terminal.print_menu()
    seller_choose = input("1. Создать новый заказ.\n"
                          "2. Проверить активные заказы. \n\n"
                          "0. Закрыть смену. \n"
                          "->: ").strip()
    if seller_choose == "1":
        order = Order()
        order.add_amount()
        current_terminal.create_order(order)
    elif seller_choose == "2":
        current_terminal.check_orders()
        # print(current_terminal.orders)
        input("Нажмите любую клавишу.")
    elif seller_choose == "0":
        current_terminal.end_working()
    else:
        print("Неизвестная команда. ")

