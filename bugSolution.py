def function_with_uncommon_error(x, y):
    try:
        if isinstance(x,(int, float)) and isinstance(y,(int,float)):
            if y==0:
                print("Error: Division by zero")
                return None
            result = x / y
            return result
        else:
            print("Error: Unsupported operand type(s) for / ")
            return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
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

# Example of no error with float
result4 = function_with_uncommon_error(10.5,2)
print(f"Result4: {result4}")
