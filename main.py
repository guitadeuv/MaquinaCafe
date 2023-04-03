MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

lucro = 0
suprimentos = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def tem_suprimentos(ingredientes_pedido):
    tem_suficiente = True
    for item in ingredientes_pedido:
        if ingredientes_pedido[item] >= suprimentos[item]:
            print(f"Desculpe, a maquina não tem {item} suficientes")
            tem_suficiente = False
    return tem_suficiente

def processar_dinheiro():
    print('Insira o dinheiro (R$ 0,50/ R$ 1,00/ R$ 2,00/ R$ 5,00)')
    total = int(input('Quantas moedas de R$0,50 ?: ')) * 0.50
    total += int(input('Quantas moedas de R$1,00 ?: ')) * 1
    total += int(input('Quantas notas de R$2,00 ?: ')) * 2
    total += int(input('Quantas notas de R$5,00 ?: ')) * 5
    return total

def tem_dinheiro_suficiente(pagamento, custo_bebida):
    if pagamento >= custo_bebida:
        troco = round(pagamento - custo_bebida, 2)
        print(f"Certo, você pagou R${pagamento}, sua bebida custa R${custo_bebida} e o seu troco é de: R${troco}")
        global lucro
        lucro += custo_bebida
        return True
    else:
        print('Desculpe, você não inseriu dinheiro suficientepara está bebida')
        return False

def fazer_cafe(cafe_escolhido, ingredientes):
    for item in ingredientes:
        suprimentos[item] -= ingredientes[item]
    print(f"Prontinho, aqui está o seu {cafe_escolhido} ☕")

maquinaLigada = True

while maquinaLigada:
    pedido = input('O que você quer pedir? (espresso/latte/cappuccino):')
    if pedido == 'off':
        maquinaLigada = False
    elif pedido == 'status':
        print(f"Água: {suprimentos['water']}ml")
        print(f"Leite: {suprimentos['milk']}ml")
        print(f"Café: {suprimentos['coffee']}ml")
        print(f"Dinheiro: {lucro}")
    else:
        bebida = MENU[pedido]
        if tem_suprimentos(bebida['ingredients']):
            pagamento = processar_dinheiro()
            if tem_dinheiro_suficiente(pagamento, bebida['cost']):
                fazer_cafe(pedido, bebida['ingredients'])