from operacoes import calcularMedia, mostrarAlunosReprovados, verificarAprovacao

dadosAlunos = {
    'matriculas': {
        26: 'Maria',
        101: 'Ana',
        13: 'João',
        37: 'Ágatha',
        72: 'Joaquim',
        5: 'Félix',
    },
    'notas': {
        26: [8, 7, 5, 9],
        101: [9, 9, 8, 9],
        13: [6, 5, 5, 5],
        37: [8, 6, 7.5, 9],
        72: [6, 5.5, 5, 7],
        5: [10, 8, 8, 8],
    }
}

alunosReprovados = [];

for matricula, notas in dadosAlunos.get('notas').items():
    mediaFinal = calcularMedia(notas)
    estaAprovado = verificarAprovacao(mediaFinal);

    if (not estaAprovado): alunosReprovados.append(matricula)

mostrarAlunosReprovados(dadosAlunos, alunosReprovados)