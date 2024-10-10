import json

# Inicializando o dicionário de produtos
produtos = {}

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
            icms = 0.18
            valor_com_icms = valor_prod + (valor_prod * icms)

            # Criando a estrutura do produto com subtópicos
            produtos[descricao_prod] = {
                'embalagem': tipo_embalagem,
                'valor_total': valor_com_icms
            }

            break  # Saindo do loop interno após o cadastro bem-sucedido
        except ValueError:
            print('Valor inválido! Por favor, insira um número válido para o valor do produto.')

    # Pergunta ao usuário se deseja cadastrar outro produto
    resposta = input('Deseja cadastrar mais algum produto? (sim ou não): ').strip().lower()

# Exibindo os produtos cadastrados
print("\nProdutos cadastrados:")
for descricao, info in produtos.items():
    print(f"Descrição: {descricao}, Embalagem: {info['embalagem']}, Valor Total (com ICMS): R$ {info['valor_total']:.2f}")

# Convertendo o dicionário de produtos para JSON e salvando em um arquivo
final = json.dumps(produtos, indent=4)

# Escrevendo o JSON em um arquivo
with open('C:\\projeto 1\\info_produtos', 'w') as info_prod:
    info_prod.write(final)

print("\nDados dos produtos salvos em 'C:\\projeto 1\\info_produtos'.")