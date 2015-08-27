def soma_quadrado(n):
    if n>O:
        menores=quadrado_menores(n)
        ultimo=menor[-1]
    else:
       '''lista=[ultimo]
        n-=ultimo
        lista.extend(soma_quadrado(n))
        return lista'''
        lista_escolhida=gerar_solucao(menores,n)
        while menores:
            lista_escolhida-2=gerar_solucao(menores,n)
            if (lista_escolhida-2)<len(lista_escolhida):
                lista_escolhida=lista_escolhida-2
    return lista_escolhida

def gerar_solucao(menores, n):
    ultimo=menores.pop()
    lista_escolhida=[ultimo]
    lista_escolhida.extend(soma_quadrado(n-ultimo))
    return lista_escolhida
