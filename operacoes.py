def calcularMedia(notas):
    media = 0

    for nota in notas:
        media += nota / len(notas)

    return media

def verificarAprovacao(media):
    return media >= 6

def mostrarAlunosReprovados(dadosAlunos, matriculasReprovados):
    for matricula in matriculasReprovados:
        nomeAluno = dadosAlunos.get('matriculas').get(matricula)
        mediaFinal = calcularMedia(dadosAlunos.get('notas').get(matricula))
        print(f'Aluno Reprovado: {str.upper(nomeAluno)} - Matrícula: {matricula} - Média Final: {mediaFinal}')