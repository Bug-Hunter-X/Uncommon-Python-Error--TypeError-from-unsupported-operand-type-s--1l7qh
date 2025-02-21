def function_with_uncommon_error(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Unsupported operand type(s) for / ")
        return None

# Example of an uncommon error: passing a string to a function that expects a number
result1 = function_with_uncommon_error(10, "hello")  # TypeError
print(f"Result1: {result1}")

# Example of common error
result2 = function_with_uncommon_error(10, 0)  #ZeroDivisionError
print(f"Result2: {result2}")

# Example of no error
result3 = function_with_uncommon_error(10,2)
print(f"Result3: {result3}")