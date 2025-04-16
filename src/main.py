def calculate(expression):
    expression = expression.strip()
    if not expression:
        raise ValueError("La expresión está vacía")

    try:
        result = eval(expression)
        return result
    except ZeroDivisionError:
        raise
    except SyntaxError:
        raise
    except Exception:
        raise ValueError("Expresión inválida")
