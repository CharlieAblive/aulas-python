import requests, json

with open("dados_funcionarios_atualizados.json", "r", encoding='utf-8') as arquivo:
    lista_funcionarios = json.load(arquivo)
    id_funcionario = 1

    for funcionario in lista_funcionarios:
        print(f'Tentativa: {id_funcionario}\n')
        novo_dicionario =    {
            "cargo": funcionario['cargo'],
            "cep": funcionario['cep'],
            "cidade": funcionario['cidade'],
            "estado": funcionario['estado'],
            "id": funcionario['id'],
            "nome": funcionario['nome'],
            "salario": funcionario['salario'],
            "tempoEmpresa": funcionario['tempoEmpresa'],
        }
        atualizacao = requests.put(f'http://192.168.205.100:8080/funcionarios/'
                                    +str(id_funcionario),
                                    json=novo_dicionario)
        id_funcionario += 1
        print(atualizacao) # PRECISAM SER 200 DE FORMA OBRIGATÓRIA

busca = requests.get(f'http://192.168.205.100:8080/funcionarios')
for funcionario in busca.json():
    print(funcionario)

# você deve atualizar todos os dados modificados no arquivo:
#           dados_funcionarios_atualizados.json
# na a API utilizada em sala com o metodo HTTP do tipo PUT
