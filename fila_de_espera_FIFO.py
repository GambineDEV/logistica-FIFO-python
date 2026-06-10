fila_de_espera = [
    [123654, "Joinville", 0.5],
    [123712, "Chapecó", 0.8],
    [123891, "Blumenau", 1.5],
]
pedidos_despachados = []

print("""
Opção 1: (Cadastrar novo pacote)
Opção 2: (Despachar próximo pacote da fila)
Opção 3: (Gerar relátorio diário e sair)""")

while True:

    op = int(input("Digite a opção desejada: "))
    if op == 1:
        id_pedido = input("Digite o numero do pedido: ")
        cidade = input("Digite a cidade de destino: ")
        peso = float(input("Digite o peso do pacote: "))
        novo_pacote = [id_pedido, cidade, peso]
        fila_de_espera.append(novo_pacote)
        print("Pedido {} adicionado ao fim da fila de despacho" .format(id_pedido))
        
        
    elif op == 2:
        removido = fila_de_espera.pop(0)
        print("Pedido {} despachado!" .format(removido[0]))
        pedidos_despachados.append(removido)

    elif op == 3:
        print("Relátorio diário")
        print("Pedidos despachados no dia: {}" .format(pedidos_despachados))
        print("Pedidos pendentes: {}" .format(fila_de_espera))
        break
    else:
        print("Opção inválida! Digite novamente.")