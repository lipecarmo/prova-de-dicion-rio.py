# Criando um dicionário para armazenar informações do contato
contato = {}

# Pedindo ao usuário para inserir as informações do contato
contato['nome'] = input("Digite o nome do contato: ")
contato['telefone'] = input("Digite o número de telefone: ")
contato['email'] = input("Digite o endereço de email: ")

# Exibindo o conteúdo do dicionário
print("\nInformações do contato:")
for chave, valor in contato.items():
    print(f"{chave.capitalize()}: {valor}")
