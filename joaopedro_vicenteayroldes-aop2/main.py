# Inicializando contadores
aprovados = 0
recuperacao = 0
reprovados = 0
reprovados_direto = 0

# Número total de alunos
total_alunos = 100

for i in range(1, total_alunos + 1):
    print(f"\nAluno {i}:")
    
    # Lendo as notas das atividades e prova regular
    aop1 = float(input("Nota [0 - 1] na AOP1: "))
    aop2 = float(input("Nota [0 - 2] na AOP2: "))
    aop3 = float(input("Nota [0 - 1] na AOP3: "))
    prova_regular = float(input("Nota [0 - 6] da PROVA REGULAR: "))
    
    # Calculando a soma do módulo (SM)
    soma_modulo = aop1 + aop2 + aop3 + prova_regular
    
    # Verificando a necessidade da prova de recuperação
    if soma_modulo >= 7:
        media_modulo = soma_modulo  # Média é igual à soma, pois não fez prova de recuperação
        status = "Aprovado"
        aprovados += 1
    else:
        # Se não passou, fazer prova de recuperação
        prova_recuperacao = float(input("Nota [0 - 10] da PROVA DE RECUPERAÇÃO: "))
        media_modulo = (soma_modulo + prova_recuperacao) / 2
        
        # Determinando o status do aluno
        if media_modulo >= 5:
            status = "Aprovado após recuperação"
            aprovados += 1
        elif 3 <= media_modulo < 5:
            status = "Reprovado"
            reprovados += 1
        else:
            status = "Reprovado Direto"
            reprovados_direto += 1
    
    # Exibindo os resultados
    print(f"Soma do Módulo (SM): {soma_modulo}")
    print(f"Média do Módulo (MM): {media_modulo}")
    print(f"Status do Aluno: {status}")

# Calculando porcentagens
porcentagem_aprovados = (aprovados / total_alunos) * 100
porcentagem_reprovados = ((reprovados + reprovados_direto) / total_alunos) * 100

# Exibindo o resumo final
print("\nResumo Final:")
print(f"Total de Alunos Aprovados: {aprovados} ({porcentagem_aprovados:.2f}%)")
print(f"Total de Alunos Reprovados: {reprovados + reprovados_direto} ({porcentagem_reprovados:.2f}%)")
