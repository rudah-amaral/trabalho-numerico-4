from modules.expressoes import ExpressaoInvalidaError, criar_funcao, traduzir_numero
from modules.trapezio import trapezio, erro_truncamento_trapezio, desvio_relativo_percentual
from modules.simpson import simpson, erro_truncamento_simpson
def comparar_metodos():
    print("Comparação entre os métodos do Trapézio e de Simpson\n")
    
    
    funcao = input("Digite a função f(x): ")
    f = criar_funcao(funcao)
    a = traduzir_numero("Digite o limite inferior da integração: ")
    b = traduzir_numero("Digite o limite superior da integração: ")
    n = traduzir_numero("Digite o número de subintervalos (deve ser par): ")

    if n % 2 != 0:
        raise ExpressaoInvalidaError("O número de subintervalos deve ser par para o método de Simpson.")

    resultado_trapezio = trapezio(f, a, b, n)
    resultado_simpson = simpson(f, a, b, n)

    erro_trapezio = erro_truncamento_trapezio(f, n, [a, b])
    erro_simpson = erro_truncamento_simpson(f, n, [a, b])

    drp_trapezio = desvio_relativo_percentual(funcao, resultado_trapezio, [a, b])
    drp_simpson = desvio_relativo_percentual(funcao, resultado_simpson, [a, b])

    print(f"\nResultados:")
    print(f"Método do Trapézio: {resultado_trapezio}, com erro de truncamento estimado: {erro_trapezio}\nDesvio relativo percentual: {drp_trapezio}%\n")
    print(f"Método de Simpson: {resultado_simpson}, com erro de truncamento estimado: {erro_simpson}\nDesvio relativo percentual: {drp_simpson}%\n")
    if drp_trapezio < drp_simpson:
        print("O método do Trapézio apresentou menor desvio relativo percentual em relação à integral de referência.\n")
    elif drp_simpson < drp_trapezio:
        print("O método de Simpson apresentou menor desvio relativo percentual em relação à integral de referência.\n")   
    else:
        print("Ambos os métodos apresentaram o mesmo desvio relativo percentual em relação à integral de referência.\n")

