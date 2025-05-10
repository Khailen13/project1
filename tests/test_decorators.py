from src.decorators import log


def test_log_1(capsys):
    """Проверка вывода в консоль успешного завершения работы функции"""

    @log()
    def my_function(x, y):
        return x + y

    my_function(5, 1)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"


def test_log_2(capsys):
    """Проверка вывода в консоль ошибки 'division by zero'"""

    @log()
    def my_function(x, y):
        return x / y

    my_function(5, 0)
    captured = capsys.readouterr()
    assert captured.out == "my_function error: division by zero. Inputs: (5, 0), {}\n"


def test_log_3():
    """Проверка записи результатов в файл"""

    file_name = "my_log.txt"

    @log(file_name)
    def my_function(x, y):
        return x / y

    # Запись успешного результата
    my_function(1, 2)
    file = open(file_name, "r")
    assert file.read() == "my_function ok"

    # Запись результата при ошибке 'division by zero'
    my_function(1, 0)
    file = open(file_name, "r")
    assert file.read() == "my_function error: division by zero. Inputs: (1, 0), {}"
