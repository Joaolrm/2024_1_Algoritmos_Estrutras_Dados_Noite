class Aluno():
    def __init__(self, codigo, nome, matricula):
        self.codigo = int(codigo)
        self.nome = str(nome)
        self.matricula = str(matricula)

    def __str__(self):
        return f"""
        Codigo: {self.codigo}
        Nome: {self.nome}
        Matrícula: {self.matricula}"""

    def imprimir(self):
        print (self)

class AlunoEnsinoMedio(Aluno):
    def __init__(self, codigo, nome, matricula, ano):
        super().__init__(codigo, nome, matricula)
        self.ano = int(ano)

    
    def __str__(self):
        return f"""
        {super().__str__()}
        Ano: {self.ano}
        """

class AlunoGraduacao(Aluno):
    def __init__(self, codigo, nome, matricula, semestre):
        super().__init__(codigo, nome, matricula)
        self.semestre = int(semestre)

    def __str__(self):
        return f"""
        {super().__str__()}
        Semestre: {self.semestre}"""

aluno = AlunoGraduacao(1, "João", 1, 1)
aluno.imprimir()
aluno1 = Aluno(1, "João", 1)
aluno1.imprimir()