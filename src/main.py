def calculate(expression):
    try:
        a, b = expression.split('+')
        return float(a.strip()) + float(b.strip())
    except Exception:
        raise ValueError("Invalid expression")
