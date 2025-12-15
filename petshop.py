from pixqrcode import PixQrCode
import qrcode

users = []
produtos = []
servicos = []

def gerar_qrcode(valor):
    pix = PixQrCode("PETSHOP", "(83) 98139-8823", "CAJAZEIRAS", str(valor))

    qr = qrcode.QRCode(border=4)
    qr.add_data(pix.generate_code())
    qr.make(fit=True)

    qr.print_ascii(invert=False)

def add_usuario(user):
    with open('usuarios.txt', 'a', encoding='utf-8') as f:
        f.write(f"\n{user['user']}/{user['password']}/{user['role']}")
def load_usuarios():
    with open('usuarios.txt', 'r', encoding='utf-8') as f:
        for linha in f:
            user = linha.strip().split('/')
            add_user = {'user': user[0], 'password': user[1], 'role': user[2]}
            users.append(add_user)
            
def add_produto(produto):
    with open('produtos.txt', 'a', encoding='utf-8') as f:
        f.write(f"\n{produto['nome']}/{produto['desc']}/{produto['valor']}")
def load_produtos():
    with open('produtos.txt', 'r', encoding='utf-8') as f:
        for linha in f:
            produto = linha.strip().split('/')
            add_produto = {'nome': produto[0], 'desc': produto[1], 'valor': int(produto[2])}
            produtos.append(add_produto)        
def refresh_produtos():
    with open('produtos.txt', 'w', encoding='utf-8') as f:
        for p in produtos:
            f.write(f"{p['nome']}/{p['desc']}/{p['valor']}\n")

    
def add_servico(servico):
    with open('servicos.txt', 'a', encoding='utf-8') as f:
        f.write(f"\n{servico['nome']}/{servico['desc']}/{servico['valor']}")
def load_servicos():
    with open('servicos.txt', 'r', encoding='utf-8') as f:
        for linha in f:
            servico = linha.strip().split('/')
            add_servico = {'nome': servico[0], 'desc': servico[1], 'valor': int(servico[2])}
            servicos.append(add_servico)
def refresh_servicos():
    with open('servicos.txt', 'w', encoding='utf-8') as f:
        for s in servicos:
            f.write(f"{s['nome']}/{s['desc']}/{s['valor']}\n")
            
def checkAdmin(user):
    for u in users:
        userLogin = u['user']
        userRole = u['role']
        if user == userLogin:
            if userRole == "admin":
                return True
            else:
                return False
            
    return False

def logar(user, password):
    for u in users:
        userLogin = u['user']
        userPassword = u['password']
        if userLogin == user and userPassword == password:
            return True
    return False

def menu_adm():
    inADMMenu = True
    while inADMMenu:
        print("=== Menu de Admnistração ===\n")
        print("0 - Voltar")
        print("1 - Gerenciar produtos")
        print("2 - Gerenciar serviços")

        options = [0, 1, 2]
        option = int(input())
        while option not in options:
            print("Digite uma opção válida! ")
            option = int(input(""))

        if option == 1:
            print("\n" * 100)
            print("=== Gerenciamento de produtos ===\n")
            print("0 - Voltar")
            print("1 - Cadastrar produtos")
            print("2 - Listar produtos")
            print("3 - Remover produtos")
            print("4 - Atualizar produtos")

            options = [0, 1, 2, 3, 4]
            option = int(input())
            while option not in options:
                print("Digite uma opção válida! ")
                option = int(input(""))

            if option == 1:
                print("\n" * 100)
                nomeProduto = input("Digite o nome do produto: ")
                descricaoProduto = input("Digite a descricao do produto: ")
                valorProduto = int(input("Digite o valor do produto: "))
                novo_produto = {'nome': nomeProduto, 'desc': descricaoProduto, 'valor': valorProduto}
                produtos.append(novo_produto)
                print("Produto cadastrado moral! \n")
                add_produto(novo_produto)
                option = -1

            if option == 2:
                print("\n" * 100)
                print("Lista de todos os produtos com seus indices: ")
                for i in range(0, len(produtos)):
                    produto = produtos[i]
                    print(f"[{i}] Nome: {produto['nome'] }")
                    print(f"    Descricação: {produto['desc']}")
                    print(f"    Valor: {produto['valor']}")
                    print("\n")
                option = 1
                input("Digite ENTER para voltar")
                print("\n" * 100)

            if option == 3:
                print("\n" * 100)
                print("Antes de remover qualquer produto, consulte todos na função Listar Produtos")
                praRemover = int(input("Digite o indice do produto pra ser removido ou -1 para cancelar: "))
                if praRemover != -1:
                    produtoRemovido = produtos.pop(praRemover)
                    print(f"Produto {produtoRemovido['nome']} Removido!")
                    refresh_produtos()
                option = -1
                print("\n" * 100)

            if option == 4:
                print("\n" * 100)
                print("Antes de editar qualquer produto, consulte todos na função Listar Produtos")
                praAtualizar = int(input("Digite o indice do produto pra ser editado ou -1 para cancelar: "))
                if praAtualizar != -1:
                    produto = produtos[praAtualizar]
                    produto['nome'] = input("Digite o novo nome: ")
                    produto['desc'] = input("Digite a nova descrição: ")
                    produto['valor'] = input("Digite o novo valor: ")
                    print(f"Produto {produto['nome']} Atualizado!")
                    refresh_produtos()
                print("\n" * 100)
                option = -1

            if option == 0:
                print("\n" * 100)
                option = -1

        if option == 2:
            print("\n" * 100)
            print("=== Gerenciamento de Serviços ===\n")
            print("0 - Voltar")
            print("1 - Cadastrar serviços")
            print("2 - Listar serviços")
            print("3 - Remover serviços")
            print("4 - Atualizar serviços")

            options = [0, 1, 2, 3, 4]
            option = int(input())
            while option not in options:
                print("Digite uma opção válida! ")
                option = int(input(""))

            if option == 1:
                print("\n" * 100)
                nomeServico = input("Digite o nome do serviços: ")
                descricaoServico = input("Digite a descricao do serviços: ")
                valorServico = int(input("Digite o valor do serviços: "))
                novo_servico = {'nome': nomeServico, 'desc': descricaoServico, 'valor': valorServico}
                servicos.append(novo_servico)
                add_servico(novo_servico)
                print("Servico cadastrado moral! \n")
                option = -1

            if option == 2:
                print("\n" * 100)
                print("Lista de todos os serviços com seus indices: ")
                for i in range(0, len(servicos)):
                    servico = servicos[i]
                    print(f"[{i}] Nome: {servico['nome'] }")
                    print(f"    Descricação: {servico['desc']}")
                    print(f"    Valor: {servico['valor']}")
                    print("\n")
                print()
                input("Digite ENTER para voltar")
                print("\n" * 100)
                option = -1

            if option == 3:
                print("\n" * 100)
                print("Antes de remover qualquer servicos, consulte todos na função Listar serviços")
                praRemover = int(input("Digite o indice do servicos pra ser removido ou -1 para cancelar: "))
                if praRemover != -1:
                    servicosRemovido = servicos.pop(praRemover)
                    refresh_servicos()
                    print(f"Servico {servicosRemovido['nome']} Removido!")
                print("\n" * 100)
                
                option = -1

            if option == 4:
                print("\n" * 100)
                print("Antes de editar qualquer servicos, consulte todos na função Listar serviços")
                praAtualizar = int(input("Digite o indice do serviço pra ser editado ou -1 para cancelar: "))
                if praAtualizar != -1:
                    servico = servicos[praAtualizar]
                    servico['nome'] = input("Digite o novo nome: ")
                    servico['desc'] = input("Digite a nova descrição: ")
                    servico['valor'] = input("Digite o novo valor: ")
                    refresh_servicos()
                print("\n" * 100)
                option = -1

        if option == 0:
            inADMMenu = False
            print("\n" * 100)

def menu_customer():
    inCustomerMenu = True
    while inCustomerMenu:
        print("\n" * 100)
        print("Seja bem vindo cliente! \n")
        print("0 - Voltar")
        print("1 - Agendar serviços")
        print("2 - Comprar produtos")

        options = [0, 1, 2]
        option = int(input())
        while option not in options:
            print("Digite uma opção válida! ")
            option = int(input(""))

        if option == 1:
            print("=== Digite o indice do serviço que deseja === \n")
            for i in range(0, len(servicos)):
                serv = servicos[i]
                print(f"[{i}] {serv['nome']} - {serv['desc']} - R${serv['valor']}")

            servInput = int(input())
            selectedServ = servicos[servInput]
            print(f"Voce selecionou o serviço {selectedServ['nome']}")
            print(
                f"Efetue o pagamento do pix no QR CODE ABAIXO"
            )
            gerar_qrcode(selectedServ['valor'])
            print(
                f'Em seguida envie o comprovante para o numero "(83) 9 8139-8823" juntamente com o serviço selecionado para prosseguirmos com o agendamento!'
            )
            input("Digite ENTER para retornar")
        if option == 2:
            print("=== Digite o indice do produto que deseja === \n")
            for i in range(0, len(produtos)):
                prod = produtos[i]
                print(f"[{i}] {prod['nome']} - {prod['desc']} - R${prod['valor']}")

            prodInput = int(input())
            selectedProd = produtos[prodInput]
            print(f"Voce selecionou o produto {selectedProd['nome']}")
            print(
                f"Efetue o pagamento do pix no QR CODE ABAIXO"
            )
            gerar_qrcode(selectedProd['valor'])
            print(
                f'Em seguida envie o comprovante para o numero "(83) 9 8139-8823" juntamente com o serviço selecionado para prosseguirmos com a compra!'
            )
            input("Digite ENTER para retornar")

        if option == 0:
            option = -1
            inCustomerMenu = False

def menu_login():
    print("\n" * 100)
    print("Digite o usuario:")
    user = input("")
    print("Digite a senha:")
    password = input("")
    login = logar(user, password)

    if login:
        isAdmin = checkAdmin(user)
        print("[!] Login feito com sucesso!")
        if isAdmin:
            print("\n" * 100)
            menu_adm()
        else:
            menu_customer()
        
    else:
        print("Login ou senha incorreto")

def menu_registro():
    print("\n" * 100)
    print("Digite o usuario a ser cadastrado:")
    user = input("")
    print("Digite a senha a ser cadastrada")
    password = input("")
    user_add = {'user': user, 'password': password, 'role': 'user'}
    users.append(user_add)
    add_usuario(user_add)
    print("\n" * 100)
    print("[!] Usuario cadastrado!")

def menu_principal():
    print("=== Petshop ===")
    print("1 - Login")
    print("2 - Cadastro")
    print()

    option = int(input(""))
    options = [0, 1, 2]
    while option not in options:
        print("Digite uma opção válida! ")
        option = int(input(""))
    if option == 1:
        menu_login()
    if option == 2:
        menu_registro()

isAdmin = False
option = -1
running = True

load_produtos()
load_usuarios()
load_servicos()
while running:
    menu_principal()