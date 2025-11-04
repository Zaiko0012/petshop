users = [
    'marcospaulo/123123/admin', 
    'william/123/admin', 
    'noca/321/user'
    ]
produtos = [
    'Shampoo pra pulguento/Um shampoo para tirar pulga/16',
    'Osso de borracha/Perfeito para cachorros hiperativos/9',
    'Gravatinha/Deixe seu pet estiloso/44'
]
servicos = [
    'Banho simples/Um banho simples/50',
    'Tosa Completa/Tosa no seu pet/25',
    'Banho + Tosa/Serviço completo/70'
]

running = True
isAdmin = False
option = -1

while running:
    if option == -1:
        print('=== Petshop ===')
        print('0 - Fechar')
        print('1 - Login')
        print('2 - Cadastro')
        print()
        
        option = int(input(''))
        options = [0, 1, 2]
        while option not in options:
            print('Digite uma opção válida! ')
            option = int(input(''))
    
    if option == 1:
        print("\n"*100)
        print('Digite o usuario:')
        login = input('')
        print('Digite a senha:')
        password = input('')
        sucess = False
        for user in users:
            split = user.split('/')
            
            userLogin = split[0]
            userPassword = split[1]
            userRole = split[2]
            if userLogin == login and userPassword == password:
                sucess = True
                if userRole == 'admin': 
                    isAdmin = True
                else:
                    isAdmin = False
        if not sucess:
            input('Usuario ou senha incorreto, digite ENTER e tente novamente!')
                
        if sucess:
            print('[!] Login feito com sucesso!')
            if isAdmin:
                inADMMenu = True
                print("\n"*100)
                while inADMMenu:
                    print('=== Menu de Admnistração ===\n')
                    print('0 - Voltar')
                    print('1 - Gerenciar produtos')
                    print('2 - Gerenciar serviços')
                    
                    options = [0, 1, 2]
                    option = int(input())
                    while option not in options:
                        print('Digite uma opção válida! ')
                        option = int(input(''))
                    
                    if option == 1:
                        print("\n"*100)
                        print('=== Gerenciamento de produtos ===\n')
                        print('0 - Voltar')
                        print('1 - Cadastrar produtos')
                        print('2 - Listar produtos')
                        print('3 - Remover produtos')
                        print('4 - Atualizar produtos')
                        
                        options = [0, 1, 2, 3 ,4]
                        option = int(input())
                        while option not in options:
                            print('Digite uma opção válida! ')
                            option = int(input(''))
                            
                        if option == 1:
                            print("\n"*100)
                            nomeProduto = input('Digite o nome do produto: ')
                            descricaoProduto = input('Digite a descricao do produto: ')
                            valorProduto = int(input('Digite o valor do produto: '))
                            produtos.append(f'{nomeProduto}/{descricaoProduto}/{valorProduto}')
                            print('Produto cadastrado moral! \n')
                            option = -1
                        if option == 2:
                            print("\n"*100)
                            print('Lista de todos os produtos com seus indices: ')
                            for i in range(0, len(produtos)):
                                produto = produtos[i].split('/')
                                print(f'[{i}] Nome: {produto[0] }')
                                print(f'    Descricação: {produto[1]}')
                                print(f'    Valor: {produto[2]}')
                                print('\n')
                            option = -1
                            input('Digite ENTER para voltar')
                            print("\n"*100)
                        if option == 3:
                            print("\n"*100)
                            print('Antes de remover qualquer produto, consulte todos na função Listar Produtos')
                            praRemover = int(input('Digite o indice do produto pra ser removido ou -1 para cancelar: '))
                            if praRemover != -1:
                                produtoRemovido = produtos.pop(praRemover)
                                produtoFormatado = produtoRemovido.split('/')
                                print(f'Produto {produtoFormatado[0]} Removido!')
                            option = -1
                            print("\n"*100)
                        if option == 4: 
                            print("\n"*100)
                            print('Antes de editar qualquer produto, consulte todos na função Listar Produtos')
                            praAtualizar = int(input('Digite o indice do produto pra ser editado ou -1 para cancelar: '))
                            if praAtualizar != -1:
                                novoNome = input('Digite o novo nome: ')
                                novaDesc = input('Digite a nova descrição: ')
                                novoPreco = input('Digite o novo valor: ')
                                novoProduto = novoNome + '/' + novaDesc + '/' + novoPreco
                                produtos[praAtualizar] = novoProduto
                                print(f'Produto {novoNome} Atualizado!')
                            print("\n"*100)
                            option = -1
                        if option == 0:
                            print("\n"*100)
                            option = -1
                            
                    
                    if option == 2:
                        print("\n"*100)
                        print('=== Gerenciamento de Serviços ===\n')
                        print('0 - Voltar')
                        print('1 - Cadastrar serviços')
                        print('2 - Listar serviços')
                        print('3 - Remover serviços')
                        print('4 - Atualizar serviços')
                        
                        options = [0, 1, 2, 3 ,4]
                        option = int(input())
                        while option not in options:
                            print('Digite uma opção válida! ')
                            option = int(input(''))
                            
                        if option == 1:
                            print("\n"*100)
                            nomeServico = input('Digite o nome do serviços: ')
                            descricaoServico = input('Digite a descricao do serviços: ')
                            valorServico = int(input('Digite o valor do serviços: '))
                            servicos.append(f'{nomeServico}/{descricaoServico}/{valorServico}')
                            print('Servico cadastrado moral! \n')
                            option = -1
                        if option == 2:
                            print("\n"*100)
                            print('Lista de todos os serviços com seus indices: ')
                            for i in range(0, len(servicos)):
                                servico = servicos[i].split('/')
                                print(f'[{i}] Nome: {servico[0] }')
                                print(f'    Descricação: {servico[1]}')
                                print(f'    Valor: {servico[2]}')
                                print('\n')
                            print()
                            input('Digite ENTER para voltar')
                            print("\n"*100)
                            option = -1
                        if option == 3:
                            print("\n"*100)
                            print('Antes de remover qualquer servicos, consulte todos na função Listar serviços')
                            praRemover = int(input('Digite o indice do servicos pra ser removido ou -1 para cancelar: '))
                            if praRemover != -1:
                                servicosRemovido = servicos.pop(praRemover)
                                servicosFormatado = servicosRemovido.split('/')
                                print(f'Servico {servicosFormatado[0]} Removido!')
                            print("\n"*100)
                            option = -1
                        if option == 4:
                            print("\n"*100) 
                            print('Antes de editar qualquer servicos, consulte todos na função Listar serviços')
                            praAtualizar = int(input('Digite o indice do serviço pra ser editado ou -1 para cancelar: '))
                            if praAtualizar != -1:
                                novoNome = input('Digite o novo nome: ')
                                novaDesc = input('Digite a nova descrição: ')
                                novoPreco = input('Digite o novo valor: ')
                                novoServico = novoNome + '/' + novaDesc + '/' + novoPreco
                                servicos[praAtualizar] = novoServico
                                print(f'Servico {novoNome} Atualizado!')
                            print("\n"*100)
                            option = -1
                    if option == 0:
                        option = -1
                        inADMMenu = False
                        print("\n"*100)
            else:
                inCustomerMenu = True
                while inCustomerMenu:
                    print("\n"*100)
                    print('Seja bem vindo cliente! \n')
                    print('0 - Voltar')
                    print('1 - Agendar serviços')
                    print('2 - Comprar produtos')      
                    
                    options = [0, 1, 2]
                    option = int(input())
                    while option not in options:
                        print('Digite uma opção válida! ')
                        option = int(input(''))
                    
                    if option == 1:
                        print('=== Digite o indice do serviço que deseja === \n')
                        for i in range(0, len(servicos)):
                            serv = servicos[i].split('/')
                            print(f'[{i}] {serv[0]} - {serv[1]} - R${serv[2]}')
                            
                        selectedServ = int(input())
                        selectedServ = servicos[selectedServ].split('/')
                        
                        print(f'Voce selecionou o serviço "{selectedServ[0]}"')
                        print(f'Faça um PIX de R${selectedServ[2]} para a chave: josewilliam2007.0012@gmail.com')
                        print(f'Em seguida envie o comprovante para o numero "(83) 9 8139-8823" juntamente com o serviço selecionado para prosseguirmos com o agendamento!')
                        input('Digite ENTER para retornar')
                    if option == 2:
                        print('=== Digite o indice do produto que deseja === \n')
                        for i in range(0, len(produtos)):
                            prod = produtos[i].split('/')
                            print(f'[{i}] {prod[0]} - {prod[1]} - R${prod[2]}')
                            
                        selectedProd = int(input())
                        selectedProd = produtos[selectedProd].split('/')
                        
                        print(f'Voce selecionou o produto "{selectedProd[0]}"')
                        print(f'Faça um PIX de R${selectedProd[2]} para a chave: josewilliam2007.0012@gmail.com')
                        print(f'Em seguida envie o comprovante para o numero "(83) 9 8139-8823" juntamente com o serviço selecionado para prosseguirmos com a compra!')
                        input('Digite ENTER para retornar')

                    if option == 0:
                        option = -1
                        inCustomerMenu = False
            
        else:
            print('Login ou senha incorreto')
    if option == 2:
        print("\n"*100)
        print('Digite o usuario a ser cadastrado:')
        user = input('')
        print('Digite a senha a ser cadastrada')
        password = input('')
        users.append(f'{user}/{password}/user')
        print("\n"*100)
        print('[!] Usuario cadastrado!')
        option = -1

    if option == 0:
        running = False