b = 1
d = 5


def test_function():
    # b = 2
    # print('Я в локальной области видимости функции test_function d:', d)
    # print('Я в локальной области видимости функции test_function')
    def inner_function():
        # c = b + 4
        # print('Я в объемлющей области видимости функции test_function d:', d)
        # print(c)
        print('Я в объемлющей области видимости функции test_function') # результат функции отображается только при
                                                                        # вызове функции test_function
    inner_function()

# inner_function() # Ошибка: программа не может найти такое имя
test_function()