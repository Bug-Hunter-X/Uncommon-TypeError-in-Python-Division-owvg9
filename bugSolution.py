def function_with_uncommon_error_solution(a, b):
    try:
        if not isinstance(b, (int, float)):
            raise TypeError("Divisor must be a number")
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError as e:
        print(f"Error: {e}")
        return None

# Example usage: The solution avoids the error by checking types
result = function_with_uncommon_error_solution(10, 'hello')
result2 = function_with_uncommon_error_solution(10, 0)
result3 = function_with_uncommon_error_solution(10, 2)