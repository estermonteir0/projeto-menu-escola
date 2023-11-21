

import json

lista_estudantes = []
lista_professores = []
lista_disciplinas = []
lista_turmas = []
lista_matriculas = []


def salvar(lista, arquivo):
    # Função para salvar os dados do dicionário e lista em JSON

    with open(arquivo, 'w') as file:
        json.dump(lista, file)
        file.close()


def carregar(arquivo):
    # Função para carregar os dados salvos nos arquivos JSON

    try:
        with open(arquivo, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# Função para exibir o menu principal
def menu():

    print('[     MENU PRINCIPAL     ]\n'
          '[1] Gerenciar estudantes\n'
          '[2] Gerenciar professores\n'
          '[3] Gerenciar disciplinas\n'
          '[4] Gerenciar turmas\n'
          '[5] Gerenciar matrículas\n'
          '[9] Sair\n')

    while True:
        try:
            op = int(input('Digite a opção desejada: '))
            break
        except ValueError:
            print('Erro. Tente novamente com um número inteiro.\n')

    if op == 9:
        finalizar()
    elif op == 1:
        menu_estudante()
    elif op == 2:
        menu_professor()
    elif op == 3:
        menu_disciplina()
    elif op == 4:
        menu_turma()
    elif op == 5:
        menu_matricula()
    else:
        print('Opção inválida.')



# Função para gerenciar estudantes
def menu_estudante():

    while True:
        print('\n[      ESTUDANTES      ]\n'
              '[1] Criar novo registro\n'
              '[2] Atualizar um registro\n'
              '[3] Excluir um registro\n'
              '[4] Listar registros\n'
              '[5] Buscar registro\n'
              '[9] Voltar menu\n')

        while True:
            try:
                op2 = int(input('Digite a opção desejada: '))
                break
            except ValueError:
                print('Erro. Tente novamente com um número inteiro.\n')

        if op2 == 1:
            criar_estudante()
        elif op2 == 2:
            atualizar_estudante()
        elif op2 == 3:
            excluir_estudante()
        elif op2 == 4:
            listar_estudante()
        elif op2 == 5:
            buscar_estudante()
        elif op2 == 9:
            menu()
        else:
            print('Opção inválida.\n')
            menu()


# Função para gerenciar professores
def menu_professor():

    while True:
        print('\n[      PROFESSORES     ]\n'
              '[1] Criar novo registro\n'
              '[2] Atualizar um registro\n'
              '[3] Excluir um registro\n'
              '[4] Listar registros\n'
              '[5] Buscar registro\n'
              '[9] Voltar menu\n')

        while True:
            try:
                op2 = int(input('Digite a opção desejada: '))
                break
            except ValueError:
                print('Erro. Tente novamente com um número inteiro.\n')

        if op2 == 1:
            criar_professor()
        elif op2 == 2:
            atualizar_professor()
        elif op2 == 3:
            excluir_professor()
        elif op2 == 4:
            listar_professor()
        elif op2 == 5:
            buscar_professor()
        elif op2 == 9:
            menu()
        else:
            print('Opção inválida.\n')
            menu()


# Função para gerenciar disciplinas
def menu_disciplina():

    while True:
        print('\n[      DISCIPLINAS      ]\n'
              '[1] Criar novo registro\n'
              '[2] Atualizar um registro\n'
              '[3] Excluir um registro\n'
              '[4] Listar registros\n'
              '[5] Buscar registro\n'
              '[9] Voltar menu\n')

        while True:
            try:
                op2 = int(input('Digite a opção desejada: '))
                break
            except ValueError:
                print('Erro. Tente novamente com um número inteiro.\n')

        if op2 == 1:
            criar_disciplina()
        elif op2 == 2:
            atualizar_disciplina()
        elif op2 == 3:
            excluir_disciplina()
        elif op2 == 4:
            listar_disciplina()
        elif op2 == 5:
            buscar_disciplina()
        elif op2 == 9:
            menu()
        else:
            print('Opção inválida.\n')
            menu()

# Função para gerenciar turmas
def menu_turma():

    while True:
        print('\n[       TURMAS       ]\n'
              '[1] Criar novo registro\n'
              '[2] Atualizar um registro\n'
              '[3] Excluir um registro\n'
              '[4] Listar registros\n'
              '[5] Buscar registro\n'
              '[9] Voltar menu\n')

        while True:
            try:
                op2 = int(input('Digite a opção desejada: '))
                break
            except ValueError:
                print('Erro. Tente novamente com um número inteiro.\n')

        if op2 == 1:
            criar_turma()
        elif op2 == 2:
            atualizar_turma()
        elif op2 == 3:
            excluir_turma()
        elif op2 == 4:
            listar_turma()
        elif op2 == 5:
            buscar_turma()
        elif op2 == 9:
            menu()
        else:
            print('Opção inválida.\n')
            menu()

# Função para gerenciar matrículas
def menu_matricula():

    while True:
        print('\n[      MATRÍCULAS      ]\n'
              '[1] Criar novo registro\n'
              '[2] Atualizar um registro\n'
              '[3] Excluir um registro\n'
              '[4] Listar registros\n'
              '[5] Buscar registro\n'
              '[9] Voltar menu\n')

        while True:
            try:
                op2 = int(input('Digite a opção desejada: '))
                break
            except ValueError:
                print('Erro. Tente novamente com um número inteiro.\n')

        if op2 == 1:
            criar_matricula()
        elif op2 == 2:
            atualizar_matricula()
        elif op2 == 3:
            excluir_matricula()
        elif op2 == 4:
            listar_matricula()
        elif op2 == 5:
            buscar_matricula()
        elif op2 == 9:
            menu()
        else:
            print('Opção inválida.\n')
            menu()




# Função para criar um registro de professor
def criar_professor():

    lista_professores = carregar('professores.json')

    while True:
        try:
            nome = (input('Digite o nome do novo usuário: '))
            codigo = int(input('Digite o código do novo usuário: '))
            cpf = (input('Digite o cpf do novo usuário: '))
            break
        except ValueError:
            print('Erro. Tente novamente com valores válidos.\n')

    for registro in lista_professores:
        if registro['codigo'] == codigo:
            print('Erro. Código já cadastrado.\n')
            finalizar()

        elif registro['cpf'] == cpf:
            print('Erro. CPF já cadastrado.\n')
            finalizar()

    registro = {'nome': nome, 'codigo': codigo, 'cpf': cpf}
    lista_professores.append(registro)

    salvar(lista_professores, 'professores.json')

    print('Usuário registrado!')


# Função para atualizar um registro de professor
def atualizar_professor():

    lista_professores = carregar('professores.json')

    if len(lista_professores) == 0:
        print('Não há registros.')

    else:
        cod = int(input('Digite o código do usuário que deseja atualizar: '))

        for registro in lista_professores:
            if registro['codigo'] == cod:

                print(
                    f"Nome: {registro['nome']}, Código: {registro['codigo']}, CPF: {registro['cpf']}")
                print()

                index = lista_professores.index(registro)
                novo_nome = (input("Novo nome: "))
                novo_codigo = int(input("Novo código: "))
                novo_cpf = input("Novo CPF: ")

                lista_professores[index] = {'nome': novo_nome,
                                            'codigo': novo_codigo,
                                            'cpf': novo_cpf}

                salvar('professores.json')
                print('Atualização concluída.')

                return

        print('Registro não encontrado.')


# Função para excluir um registro de professor
def excluir_professor():

    lista_professores = carregar('professores.json')

    if len(lista_professores) == 0:
        print('Não há registros.')

    else:
        cod = int(input('Digite o código do usuário que deseja remover: '))

        for registro in lista_professores:
            if registro['codigo'] == cod:
                resp = input('Confirmar exclusão? (S/N)').upper()

                if resp == 'S':
                    lista_professores.remove(registro)
                    salvar('professores.json')

                    print('Registro removido com sucesso!')

                    return

                else:
                    print('Ok')

            elif registro['codigo'] != cod:
                print('Registro não encontrado.')


# Função para listar registros de professor
def listar_professor():

    lista_professores = carregar('professores.json')

    if len(lista_professores) == 0:
        print('Não há registros.')

    else:
        for registro in lista_professores:
            print(f"Nome: {registro['nome']}, Código: {registro['codigo']}, CPF: {registro['cpf']}")
            print()


# Função para buscar um registro de professor
def buscar_professor():

    lista_professores = carregar('professores.json')

    if len(lista_professores) == 0:
        print('Não há registros.')

    else:
        cod = int(input('Digite o código do usuário que deseja consultar: '))

        for registro in lista_professores:
            if registro['codigo'] == cod:

                print(f"Nome: {registro['nome']}, Código: {registro['codigo']}, CPF: {registro['cpf']}")
                print()

                return

        print('Registro não encontrado.')




# Função para criar um registro de estudante
def criar_estudante():

    lista_estudantes = carregar('estudantes.json')

    while True:
        try:
            nome = (input('Digite o nome do novo usuário: '))
            codigo = int(input('Digite o código do novo usuário: '))
            cpf = (input('Digite o cpf do novo usuário: '))
            break
        except ValueError:
            print('Erro. Tente novamente com valores válidos.\n')

    for registro in lista_estudantes:
        if registro['codigo'] == codigo:
            print('Erro. Código já cadastrado.')
            finalizar()
        elif registro['cpf'] == cpf:
            print('Erro. CPF já cadastrado.')
            finalizar()

    registro = {'nome': nome, 'codigo': codigo, 'cpf': cpf}
    lista_estudantes.append(registro)

    salvar(lista_estudantes, 'estudantes.json')

    print('Usuário registrado!')


# Função para atualizar um registro de estudante
def atualizar_estudante():

    lista_estudantes = carregar('estudantes.json')

    if len(lista_estudantes) == 0:
        print('Não há registros.')

    else:
        cod = int(input('Digite o código do usuário que deseja atualizar: '))

        for registro in lista_estudantes:
            if registro['codigo'] == cod:

                print(f"Nome: {registro['nome']}, Código: {registro['codigo']}, CPF: {registro['cpf']}")
                print()

                index = lista_estudantes.index(registro)
                novo_nome = input("Novo nome: ")
                novo_codigo = int(input("Novo código: "))
                novo_cpf = input("Novo CPF: ")

                lista_estudantes[index] = {'nome': novo_nome,
                                       'codigo': novo_codigo,
                                       'cpf': novo_cpf}

                salvar(lista_estudantes, 'estudantes.json')
                print('Atualização concluída.')

                return

        print('Registro não encontrado.')


# Função para excluir um registro de estudante
def excluir_estudante():

    lista_estudantes = carregar('estudantes.json')

    cod = int(input('Digite o código do usuário que deseja remover: '))
    encontrado = False

    for registro in lista_estudantes:
        if registro['codigo'] == cod:
            encontrado = True

    if encontrado:
        resp = input('Confirmar exclusão? (S/N)').upper()

        if resp == 'S':
            lista_estudantes.remove(registro)
            salvar(lista_estudantes, 'estudantes.json')
            print('Registro removido com sucesso!')

        else:
            print('Operação cancelada.')

            return

    else:
        print('Registro não encontrado.')


# Função para listar registros de estudante
def listar_estudante():

    lista_estudantes = carregar('estudantes.json')

    if not lista_estudantes:
        print('Não há registros.')

    for registro in lista_estudantes:
        print(
            f"Nome: {registro['nome']}, Código: {registro['codigo']}, CPF: {registro['cpf']}")
        print()


# Função para buscar um registro de estudante
def buscar_estudante():

    lista_estudantes = carregar('estudantes.json')

    if len(lista_estudantes) == 0:
        print('Não há registros.')

    else:
        cod = int(input('Digite o código do usuário que deseja consultar: '))

        for registro in lista_estudantes:
            if registro['codigo'] == cod:

                print(
                    f"Nome: {registro['nome']}, Código: {registro['codigo']}, CPF: {registro['cpf']}")
                print()

                return

        print('Registro não encontrado.')




# Função para criar um registro de disciplina
def criar_disciplina():

    lista_disciplinas = carregar('disciplinas.json')

    while True:
        try:
            nome = input('Digite o nome da nova disciplina: ')
            codigo = int(input('Digite o código da nova disciplina: '))
            break
        except ValueError:
            print('Erro. Tente novamente com valores válidos.\n')

    for registro in lista_disciplinas:
        if registro['codigo'] == codigo:
            print('Erro. Código já cadastrado.')
            finalizar()
        elif registro['nome'] == nome:
            print('Erro. Disciplina já cadastrada.')
            finalizar()

    registro = {'nome': nome, 'codigo': codigo}
    lista_disciplinas.append(registro)

    salvar(lista_disciplinas, 'disciplinas.json')

    print('Disciplina registrada!')


# Função para atualizar um registro de disciplina
def atualizar_disciplina():

    lista_disciplinas = carregar('disciplinas.json')

    if len(lista_disciplinas) == 0:
        print('Não há registros.')

    else:
        cod = int(input('Digite o código da disciplina que deseja atualizar: '))

        for registro in lista_disciplinas:
            if registro['codigo'] == cod:

                print(
                    f"Nome: {registro['nome']}, Código: {registro['codigo']}")
                print()

                index = lista_disciplinas.index(registro)
                novo_nome = input("Novo nome: ")
                novo_codigo = int(input("Novo código: "))

                lista_disciplinas[index] = {'nome': novo_nome,
                                            'codigo': novo_codigo}

                salvar('disciplinas.json')
                print('Atualização concluída.')

                return

        print('Registro não encontrado.')


# Função para excluir um registro de disciplina
def excluir_disciplina():

    lista_disciplinas = carregar('disciplinas.json')

    if len(lista_disciplinas) == 0:
        print('Não há registros.')

    else:
        cod = int(input('Digite o código da disciplina que deseja remover: '))

        for registro in lista_disciplinas:
            if registro['codigo'] == cod:
                resp = input('Confirmar exclusão? (S/N)').upper()

                if resp == 'S':
                    lista_disciplinas.remove(registro)
                    salvar('disciplinas.json')

                    print('Registro removido com sucesso!')

                    return

                else:
                    print('Ok')

            elif registro['codigo'] != cod:
                print('Registro não encontrado.')


# Função para listar registros de disciplina
def listar_disciplina():

    lista_disciplinas = carregar('disciplinas.json')

    if len(lista_disciplinas) == 0:
        print('Não há registros.')

    else:
        for registro in lista_disciplinas:
            print(f"Disciplina: {registro['nome']}, Código: {registro['codigo']}")
            print()


# Função para buscar um registro de disciplina
def buscar_disciplina():

    lista_disciplinas = carregar('disciplinas.json')

    if len(lista_disciplinas) == 0:
        print('Não há registros.')

    else:
        cod = int(input('Digite o código da disciplina que deseja consultar: '))

        for registro in lista_disciplinas:
            if registro['codigo'] == cod:

                print(f"Disciplina: {registro['nome']}, Código: {registro['codigo']}")
                print()

                return

        print('Registro não encontrado.')




# Função para criar um registro de turma
def criar_turma():

    lista_turmas = carregar('turmas.json')
    lista_professores = carregar('professores.json')
    lista_disciplinas = carregar('disciplinas.json')

    while True:
        try:
            codigo_turma = int(input('Digite o código da nova turma: '))
            codigo_professor = int(input('Digite o código do professor: '))
            codigo_disciplina = int(input('Digite o código da disciplina: '))
            break
        except ValueError:
            print('Erro. Tente novamente com valores válidos.\n')

    for registro in lista_turmas:
        if registro['codigo_turma'] == codigo_turma:
            print('Erro. Turma já cadastrada.')
            finalizar()

    for registro in lista_professores:
        if registro['codigo'] != codigo_professor:
            print('Erro. Professor não cadastrado.')
            finalizar()

    for registro in lista_disciplinas:
        if registro['codigo'] != codigo_disciplina:
            print('Erro. Disciplina não cadastrada.')
            finalizar()


    registro = {'codigo_turma': codigo_turma, 'codigo_professor': codigo_professor,
                'codigo_disciplina': codigo_disciplina}

    lista_turmas.append(registro)

    salvar(lista_turmas, 'turmas.json')

    print('Turma registrada!')


# Função para atualizar um registro de turma
def atualizar_turma():

    lista_turmas = carregar('turmas.json')

    if len(lista_turmas) == 0:
        print('Não há registros.')

    else:
        cod = int(input('Digite o código da turma que deseja atualizar: '))

        for registro in lista_turmas:
            if registro['codigo_turma'] == cod:

                print(
                    f"Código da turma: {registro['codigo_turma']}, "
                    f"Código do professor: {registro['codigo_professor']}, "
                    f"Código da disciplina: {registro['codigo_disciplina']}")
                print()

                index = lista_turmas.index(registro)
                novo_codigo_turma = int(input("Novo código da turma: "))
                novo_codigo_professor = int(input("Novo código do professor: "))
                novo_codigo_disciplina = int(input("Novo código da disciplina: "))

                lista_turmas[index] = {'codigo_turma': novo_codigo_turma,
                                       'codigo_professor': novo_codigo_professor,
                                       'codigo_disciplina': novo_codigo_disciplina}

                salvar('turmas.json')
                print('Atualização concluída.')

                return

        print('Registro não encontrado.')


# Função para excluir um registro de turma
def excluir_turma():

    lista_turmas = carregar('turmas.json')

    if len(lista_turmas) == 0:
        print('Não há registros.')

    else:
        cod = int(input('Digite o código da turma que deseja remover: '))

        for registro in lista_turmas:
            if registro['codigo_turma'] == cod:
                resp = input('Confirmar exclusão? (S/N)').upper()

                if resp == 'S':
                    lista_turmas.remove(registro)
                    salvar('turmas.json')

                    print('Registro removido com sucesso!')

                    return

                else:
                    print('Ok')

            elif registro['codigo_turma'] != cod:
                print('Registro não encontrado.')


# Função para listar registros de turma
def listar_turma():

    lista_turmas = carregar('turmas.json')

    if len(lista_turmas) == 0:
        print('Não há registros.')

    else:
        for registro in lista_turmas:
            print(f"Turma: {registro['codigo_turma']}, "
                  f"Código do professor: {registro['codigo_professor']}, "
                  f"Código da disciplina: {registro['codigo_disciplina']}")
            print()


# Função para buscar um registro de turma
def buscar_turma():

    lista_turmas = carregar('turmas.json')

    if len(lista_turmas) == 0:
        print('Não há registros.')

    else:
        cod = int(input('Digite o código da turma que deseja consultar: '))

        for registro in lista_turmas:
            if registro['codigo_turma'] == cod:

                print(f"Código da turma: {registro['codigo_turma']},"
                      f" Código do professor: {registro['codigo_professor']},"
                      f" Código da disciplina: {registro['codigo_disciplina']}")
                print()

                return

        print('Registro não encontrado.')




# Função para criar um registro de matrícula
def criar_matricula():

    lista_matriculas = carregar('matriculas.json')
    lista_estudantes = carregar('estudantes.json')
    lista_turmas = carregar('turmas.json')

    while True:
        try:
            codigo_turma = int(input('Digite o código da turma: '))
            codigo_estudante = int(input('Digite o código do estudante: '))
            break
        except ValueError:
            print('Erro. Tente novamente com números inteiros.\n')

    for registro in lista_matriculas:
        if registro['codigo_turma'] == codigo_turma and registro['codigo_estudante'] == codigo_estudante:
            print('Erro. Matrícula já cadastrada.')
            finalizar()

    for registro in lista_turmas:
        if registro['codigo_turma'] != codigo_turma:
            print('Erro. Turma não cadastrada.')
            finalizar()

    for registro in lista_estudantes:
        if registro['codigo'] != codigo_estudante:
            print('Erro. Estudante não cadastrado.')
            finalizar()

    registro = {'codigo_turma': codigo_turma, 'codigo_estudante': codigo_estudante}
    lista_matriculas.append(registro)

    salvar(lista_matriculas, 'matriculas.json')

    print('Matrícula registrada!')


# Função para atualizar um registro de matrícula
def atualizar_matricula():

    lista_matriculas = carregar('matriculas.json')

    if len(lista_matriculas) == 0:
        print('Não há registros.')

    else:
        cod = int(input('Digite o código do estudante que deseja atualizar: '))

        for registro in lista_matriculas:
            if registro['codigo_estudante'] == cod:

                print(
                    f"Código da turma: {registro['codigo_turma']}, "
                    f"Código do estudante: {registro['codigo_estudante']}")
                print()

                index = lista_matriculas.index(registro)
                novo_codigo_turma = input("Novo código da turma: ")
                novo_codigo_estudante = input('Novo código do estudante: ')


                lista_matriculas[index] = {'codigo_turma': novo_codigo_turma},{'codigo_estudante': novo_codigo_estudante}

                salvar('matriculas.json')
                print('Atualização concluída.')

                return

        print('Registro não encontrado.')


# Função para excluir um registro de matrícula
def excluir_matricula():

    lista_matriculas = carregar('matriculas.json')

    if len(lista_matriculas) == 0:
        print('Não há registros.')

    else:
        cod = int(input('Digite o código do estudante que deseja remover: '))

        for registro in lista_matriculas:
            if registro['codigo_estudante'] == cod:
                resp = input('Confirmar exclusão? (S/N)').upper()

                if resp == 'S':
                    lista_matriculas.remove(registro)
                    salvar('matriculas.json')

                    print('Registro removido com sucesso!')

                    return

                else:
                    print('Ok')

            elif registro['codigo_estudante'] != cod:
                print('Registro não encontrado.')


# Função para listar registros de matricula
def listar_matricula():

    lista_matriculas = carregar('matriculas.json')

    if len(lista_matriculas) == 0:
        print('Não há registros.')

    else:
        for registro in lista_matriculas:
            print(f"MATRÍCULA\n"
                  f"Código do estudante: {registro['codigo_estudante']}, "
                  f"Código da turma: {registro['codigo_turma']}")
            print()


# Função para buscar um registro de matricula
def buscar_matricula():

    lista_matriculas = carregar('matriculas.json')

    if len(lista_matriculas) == 0:
        print('Não há registros.')

    else:
        cod = int(input('Digite o código do estudante que deseja consultar: '))

        for registro in lista_matriculas:
            if registro['codigo_estudante'] == cod:

                print(f"MATRÍCULA"
                      f"Código do estudante: {registro['codigo_estudante']}, "
                      f"Código da turma: {registro['codigo_turma']}")
                print()

                return

        print('Registro não encontrado.')



# Função para finalizar o programa
def finalizar():

    print('Finalizando...')
    exit(0)


# Chamada da função do menu principal
menu()
