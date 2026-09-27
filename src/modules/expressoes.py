import math
import sympy

CONTEXTO_MATEMATICO = {
    "math": math,
    # trigonometricas
    "sin": math.sin, "cos": math.cos, "tan": math.tan,
    "asin": math.asin, "acos": math.acos, "atan": math.atan, "atan2": math.atan2,
    # hiperbolicas
    "sinh": math.sinh, "cosh": math.cosh, "tanh": math.tanh,
    # logaritmos e exponenciais
    "log": math.log, "log10": math.log10, "log2": math.log2, "exp": math.exp,
    # raizes e potencias
    "sqrt": math.sqrt, "pow": math.pow,
    # constantes
    "pi": math.pi, "e": math.e,
    # fatorial
    "factorial": math.factorial,
}

class ExpressaoInvalidaError(Exception):
    """Levantada quando uma expressão digitada pelo usuário não pode ser interpretada ou avaliada."""

def criar_funcao(expressao):
    expressao = expressao.replace("^", "**")

    def traduzindo_expressao(x):
        try:
            return eval(expressao, {"__builtins__": {}}, {**CONTEXTO_MATEMATICO, "x": x})
        except Exception as e:
            raise ExpressaoInvalidaError (f"Não foi possível avaliar f({x}): {e}") from e
    return traduzindo_expressao

def criar_derivada(expressao):
    expressao = expressao.replace("^", "**")
    x = sympy.symbols("x")

    try:
        expr_sympy = sympy.sympify(expressao)
        derivada_sympy = sympy.diff(expr_sympy, x)
    except Exception as e:
        raise ExpressaoInvalidaError(f"Não foi possível derivar '{expressao}': {e}") from e
    derivada_lambda = sympy.lambdify(x, derivada_sympy, modules=["math"])

    def dfuncao(valor):
        try:
            return float(derivada_lambda(valor))
        except Exception as e:
            raise ExpressaoInvalidaError(f"Não foi possível avaliar f'({valor}): {e}") from e

    return dfuncao

def criar_integral(expressao):
    expressao = expressao.replace("^", "**")
    x = sympy.symbols("x")

    try:
        expr_sympy = sympy.sympify(expressao)
        integral_sympy = sympy.integrate(expr_sympy, x)
    except Exception as e:
        raise ExpressaoInvalidaError(f"Não foi possível integrar '{expressao}': {e}") from e
    integral_lambda = sympy.lambdify(x, integral_sympy, modules=["math"])

    def ifuncao(intervalos):
        try:
            return float(integral_lambda(intervalos[1]) - integral_lambda(intervalos[0]))
        except Exception as e:
            raise ExpressaoInvalidaError(f"Não foi possível avaliar ∫f(x) no intervalo {intervalos}: {e}") from e

    return ifuncao

def traduzir_numero(expressao: str, nome_campo: str = "valor") -> float:
    expressao = expressao.replace("^", "**")

    try:
        resultado =  eval(expressao, {"__builtins__":{}}, CONTEXTO_MATEMATICO)
        return float(resultado)
    except Exception as e:
        raise ExpressaoInvalidaError (f"Não foi possível interpretar {nome_campo} = '{expressao}': {e}") from e


