class AvaliadorSigaa:
  
    def __init__(self, carga_horaria_total: int):
        self.carga_horaria_total = carga_horaria_total
        self.LIMITE_FALTAS = 0.25  
        self.MEDIA_APROVACAO = 7.0
        self.MEDIA_MINIMA_EXAME = 3.0

    def processar_status(self, notas: list[float], faltas_em_horas: int) -> str:
        if (faltas_em_horas / self.carga_horaria_total) > self.LIMITE_FALTAS:
            return "Reprovado por Frequência"

        if not notas:
            raise ValueError("O aluno deve ter ao menos uma nota cadastrada.")
            
        media_final = sum(notas) / len(notas)

        if media_final >= self.MEDIA_APROVACAO:
            return "Aprovado"
        elif media_final >= self.MEDIA_MINIMA_EXAME:
            return "Exame"
        else:
            return "Reprovado por Nota"

if __name__ == '__main__':
    unittest.main(verbosity=2)