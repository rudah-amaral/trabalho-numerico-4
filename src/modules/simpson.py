from modules.expressoes import ExpressaoInvalidaError, criar_derivada, criar_funcao, traduzir_numero, criar_integral

def metodo_simpson():
    print ("Método de Simpson\n")
    funcao = input("Digite a função f(x): ")
    f = criar_funcao(funcao)
    a = traduzir_numero(input("Digite o limite inferior da integração: "), "limite inferior")
    b = traduzir_numero(input("Digite o limite superior da integração: "), "limite superior")
    n = traduzir_numero(input("Digite o número de subintervalos (deve ser par): "), "número de subintervalos")

    if n != int(n) or n < 2 or int(n) % 2 != 0:
        raise ExpressaoInvalidaError("O número de subintervalos deve ser um inteiro par (≥ 2) para o método de Simpson.")

    n = int(n)

    resultado = simpson(f, a, b, n)
    erro = erro_truncamento_simpson(funcao, n, [a, b])
    drp = desvio_relativo_percentual(funcao, resultado, [a, b])
    print(f"O valor da integral é: {resultado}, com erro de truncamento estimado: {erro}\nDesvio relativo percentual em relação à integral de referência: {drp}%\n")

def simpson(f, a, b, n):
    h = (b - a) / n  
    integral = f(a) + f(b)  

    for i in range(1, n):
        x_i = a + i * h
        if i % 2 == 0:
            integral += 2 * f(x_i)
        else:
            integral += 4 * f(x_i)

    integral *= h / 3  
    return integral

def erro_truncamento_simpson(funcao, n, intervalos):

    ordem = 4
    h = (intervalos[1] - intervalos[0]) / n
    df = criar_derivada(funcao, ordem)
    if df == 0:
        raise ExpressaoInvalidaError(f"Não foi possível calcular a derivada: derivada zera.")
    erro = ((intervalos[1] - intervalos[0]) * h**4  / 180) * max(abs(df(intervalos[0])), abs(df(intervalos[1])))

    return erro

def desvio_relativo_percentual(funcao, integral_calculada, intervalos) -> float:
    try:
        integral_funcao = criar_integral(funcao)
        integral_referencia = integral_funcao(intervalos)
        desvio = abs((integral_calculada - integral_referencia) / integral_referencia) * 100
        return desvio
    except ZeroDivisionError:
        raise ExpressaoInvalidaError("A integral de referência é zero, não é possível calcular o desvio relativo percentual.")