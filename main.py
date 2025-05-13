def analisar_lista(lista_numeros):

    if not lista_numeros:
        return {
            "média": 0,
            "maior": None,
            "menor": None,
            "pares": 0
        }

    soma = sum(lista_numeros)
    media = soma / len(lista_numeros)
    maior = max(lista_numeros)
    menor = min(lista_numeros)
    pares = sum(1 for numero in lista_numeros if numero % 2 == 0)

    return {
        "média": round(media, 2),
        "maior": maior,
        "menor": menor,
        "pares": pares
    }

if __name__ == "__main__":
    numeros = [10, 23, 5, 8, 12, 33, 42, 7, 19, 28, 3, 16, 9, 50, 21]
    resultados = analisar_lista(numeros)
    print(f"Média: {resultados['média']}")
    print(f"Maior número: {resultados['maior']}")
    print(f"Menor número: {resultados['menor']}")
    print(f"Quantidade de números pares: {resultados['pares']}")
