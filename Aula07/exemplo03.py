estudante = {
    "João": {
        "idade": 18,
        "cidade":"São Paulo",
        "notas":[7.5, 8.0, 9.0]
    },
    "Maria": {
        "idade": 20,
        "cidade":"Rio de Janeiro",
        "notas":[6.5, 7.0, 8.5]
    },
    "Pedro": {
        "idade": 19,
        "cidade":"Belo Horizonte",
        "notas":[8.0, 8.5, 9.5]
    }    
}

aluno = "João"
print(f"A idade de {aluno} é:")
print(estudante[aluno]['idade'])

aluno = "Maria"
print(f"As notas de {aluno} são:")
estudante[aluno]['notas'].append(9.0)
print(estudante[aluno]['notas'])

for lAluno, info in estudante.items():
    print(lAluno, ":")
    print("Idade: ", info['idade'])
    print("Cidade: ", info['cidade'])
    print("Notas: ", info['notas']) 
    print("Media: ", sum(info['notas'])/len(info['notas']))
    print("=" * 20)       