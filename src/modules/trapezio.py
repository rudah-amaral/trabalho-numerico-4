from modules.expressoes import ExpressaoInvalidaError, criar_derivada, criar_funcao, traduzir_numero, criar_integral

def metodo_trapezio():
    print ("Método do Trapézio\n")
    funcao = input("Digite a função f(x): ")
    f = criar_funcao(funcao)
    a = traduzir_numero("Digite o limite inferior da integração: ")
    b = traduzir_numero("Digite o limite superior da integração: ")
    n = traduzir_numero("Digite o número de subintervalos: ")

    resultado = trapezio(f, a, b, n)
    erro = erro_truncamento_trapezio(f, n, [a, b])
    drp = desvio_relativo_percentual(funcao, resultado, [a, b])
    print(f"O valor da integral é: {resultado}, com erro de truncamento estimado: {erro}\nDesvio relativo percentual em relação à integral de referência: {drp}%\n")


def trapezio(f, a, b, n):

    h = (b - a) / n  
    integral = 0.5 *(f(a) + f(b))  

    for i in range(1, n):
        x_i = a + i * h
        integral += f(x_i)

    integral *= h  
    return integral

def erro_truncamento_trapezio(funcao, n, intervalos):


    
    df = criar_derivada(criar_funcao(funcao))
    if df == 0:
        raise ExpressaoInvalidaError(f"Não foi possível calcular a derivada: derivada é zero.")
    erro = (intervalos[1] - intervalos[0])**3 / (12 * n**2) * max(abs(df(intervalos[0])), abs(df(intervalos[1])))

    return erro

def desvio_relativo_percentual(funcao, integral_calculada, intervalos) -> float:
    try:
        integral_funcao = criar_integral(funcao)
        integral_referencia = integral_funcao(intervalos) 
        desvio = abs((integral_calculada - integral_referencia) / integral_referencia) * 100
        return desvio
    except ZeroDivisionError:
        raise ExpressaoInvalidaError("A integral de referência é zero, não é possível calcular o desvio relativo percentual.")