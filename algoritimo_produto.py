# deseja cadastrar outro produto?

resposta = 'sim'
while resposta == 'sim':

    # 1 peça ao usuário as seguintes informações de produtos: descrição do produto, valor do produto, tipo de embalagem.

    descrição_prod = str(input('digite a descrição do produto aqui: '))
    while True:
        try:
            valor_prod = float(input('insira o valor do produto: '))
        except ValueError:
            print('Esta informação não é valida, por favor insira um numero real')
        else:
            break

    tipo_embalagem = str(input('Qual o tipo de embalagem deste produto: '))

# 2 Crie uma função Lambda que, a partir do valor do produto, retorne o valor do ICMS (considere aplicar 18% sobre o valor do produto).

    valor = valor_prod
    icms = valor_prod*0.18
    def soma(valor, icms): return valor + icms
    print(soma(valor, icms))

# 3 deseja cadastrar um novo produto?
    resposta = input('Deseja cadastrar mais algum produto?')

# 4 adicionar a coleção:

armazenamento_info = {'tony stark': [
    'genio', 'bilionário', 'playboy', 'filantropo']}

print(armazenamento_info['tony stark'])


# 4 finalizar cadastro do produto
