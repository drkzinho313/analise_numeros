from main import analisar_lista

lista_de_numeros = [10, 23, 5, 8, 12, 33, 42, 7, 19, 28, 3, 16, 9, 50, 21]
resultados_analise = analisar_lista(lista_de_numeros)

print(f"Média: {resultados_analise['média']}")
print(f"Maior número: {resultados_analise['maior']}")
print(f"Menor número: {resultados_analise['menor']}")
print(f"Quantidade de números pares: {resultados_analise['pares']}")
