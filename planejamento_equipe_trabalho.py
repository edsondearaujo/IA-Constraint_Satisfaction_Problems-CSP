from constraint import Problem, AllDifferentConstraint

def solve_work_schedule(funcionarios, tarefas, restricoes):
    """
    Resolve o problema de planejamento de equipes de trabalho.
    
    Args:
        funcionarios (list): Lista de funcionários.
        tarefas (list): Lista de tarefas.
        restricoes (list): Lista de restrições adicionais.
        
    Returns:
        list: Lista de soluções do problema.
    """
    problem = Problem()
    
    # Variáveis do PSR: atribuição de tarefas para cada funcionário
    for funcionario in funcionarios:
        problem.addVariable(funcionario, tarefas)
    
    # Restrições: cada tarefa deve ser atribuída a um único funcionário
    problem.addConstraint(AllDifferentConstraint(), funcionarios)
    
    # Restrições personalizadas fornecidas pelo usuário
    for restricao in restricoes:
        constraint = restricao['constraint']
        variables = restricao['variables']
        problem.addConstraint(constraint, variables)
    
    # Solução do PSR
    solucao = problem.getSolutions()
    
    return solucao

def print_work_schedule(solucao):
    """
    Imprime a solução do problema de planejamento de equipes de trabalho.
    
    Args:
        solucao (list): Lista de soluções do problema.
    """
    print()
    print("Cronograma de trabalho")
    print()
    semanas = len(solucao)
    for semana in range(semanas):
        print(f"Semana {semana + 1}:")
        cronograma_semana = solucao[semana]
        for funcionario, tarefa in cronograma_semana.items():
            print(f"{funcionario} -> {tarefa}")
        print()

# Exemplo de uso

# Definição de funcionários e tarefas
funcionarios = ['Luiza', 'João Henrique', 'Solange']
tarefas = ['Definir backlog', 'Implementar funcionalidade', 'Apresentar trabalho']

# Definição de restrições adicionais
restricoes = [
    {'constraint': lambda f1, f2: f1 != f2, 'variables': ('Luiza', 'João Henrique')},
    {'constraint': lambda f1, f3: f1 != f3, 'variables': ('Luiza', 'Solange')}
]

# Resolução do problema de planejamento de cronograma
solucao = solve_work_schedule(funcionarios, tarefas, restricoes)

# Exibição da solução
print_work_schedule(solucao)