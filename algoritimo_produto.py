# Inicializando a lista de produtos
produtos = []

# Pergunta inicial para o usuário
resposta = 'sim'

# Loop para cadastro de múltiplos produtos
while resposta == 'sim':
    # Cadastro de um produto

    # Solicitando informações do produto
    descricao_prod = input('Digite a descrição do produto: ')
    tipo_embalagem = input('Qual o tipo de embalagem deste produto: ')

    # Solicitando o valor do produto
    while True:
        try:
            valor_prod = float(input('Insira o valor do produto: '))

            # Calculando o valor com ICMS
            icms_rate = 0.18
            valor_com_icms = valor_prod + (valor_prod * icms_rate)

            # Criando o dicionário do produto
            produto = {
                'descricao': descricao_prod,
                'embalagem': tipo_embalagem,
                'valor_total': valor_com_icms
            }

            # Adicionando o produto à lista
            produtos.append(produto)

            break  # Saindo do loop interno após o cadastro bem-sucedido
        except ValueError:
            print(
                'Valor inválido! Por favor, insira um número válido para o valor do produto.')

    # Pergunta ao usuário se deseja cadastrar outro produto
    resposta = input(
        'Deseja cadastrar mais algum produto? (sim ou não): ').strip().lower()

# Exibindo os produtos cadastrados
print("\nProdutos cadastrados:")
for p in produtos:
    print(f"Descrição: {p['descricao']}, Embalagem: {
          p['embalagem']}, Valor Total (com ICMS): R$ {p['valor_total']:.2f}")
