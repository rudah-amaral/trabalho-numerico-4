from modules.expressoes import ExpressaoInvalidaError, criar_derivada, criar_funcao, traduzir_numero, criar_integral

def metodo_simpson():
    print ("Método de Simpson\n")
    funcao = input("Digite a função f(x): ")
    f = criar_funcao(funcao)
    a = traduzir_numero("Digite o limite inferior da integração: ")
    b = traduzir_numero("Digite o limite superior da integração: ")
    n = traduzir_numero("Digite o número de subintervalos (deve ser par): ")

    if n % 2 != 0:
        raise ExpressaoInvalidaError("O número de subintervalos deve ser par para o método de Simpson.")

    resultado = simpson(f, a, b, n)
    erro = erro_truncamento_simpson(f, n, [a, b])
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


    
    df = criar_derivada(criar_funcao(criar_funcao(criar_funcao(funcao))))
    if df == 0:
        raise ExpressaoInvalidaError(f"Não foi possível calcular a derivada: derivada zera.")
    erro = (intervalos[1] - intervalos[0])**5 / (180 * n**4) * max(abs(df(intervalos[0])), abs(df(intervalos[1])))

    return erro

def desvio_relativo_percentual(funcao, integral_calculada, intervalos) -> float:
    try:
        integral_funcao = criar_integral(funcao)
        integral_referencia = integral_funcao(intervalos)
        desvio = abs((integral_calculada - integral_referencia) / integral_referencia) * 100
        return desvio
    except ZeroDivisionError:
        raise ExpressaoInvalidaError("A integral de referência é zero, não é possível calcular o desvio relativo percentual.")