def log(filename: str = "console"):
    """Регистрирует детали выполнения функций, такие как имя функции, передаваемые аргументы,
    результат выполнения и информация об ошибках"""

    def my_decorator(func):
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
                successful_result = f"{func.__name__} ok"
                if filename == "console":
                    print(successful_result)
                    return successful_result
                else:
                    with open(f"{filename}", "w") as f:
                        f.write(successful_result)
                        return successful_result
            except Exception as error_message:
                error_message = f"{func.__name__} error: {error_message}. Inputs: {args}, {kwargs}"
                if filename == "console":
                    print(error_message)
                    return error_message
                else:
                    with open(f"{filename}", "w") as f:
                        f.write(error_message)
                        return error_message

        return wrapper

    return my_decorator
