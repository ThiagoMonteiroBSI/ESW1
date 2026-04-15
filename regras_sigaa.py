class AvaliadorSigaa:
    def __init__(self, carga_horaria_total: int):
        self.carga_horaria_total = carga_horaria_total
        self.LIMITE_FALTAS = 0.25  
        self.MEDIA_APROVACAO = 7.0
        self.MEDIA_MINIMA_EXAME = 3.0
        self.MEDIA_FINAL_APOS_EXAME = 5.0

    def processar_status(self, notas: list[float], faltas_em_horas: int) -> dict:
        media = sum(notas) / len(notas) if notas else 0.0
        percentual_faltas = faltas_em_horas / self.carga_horaria_total
        
        if percentual_faltas > self.LIMITE_FALTAS:
            return {
                "status": "Reprovado por Frequência", 
                "media": round(media, 2),
                "detalhes": f"{percentual_faltas*100:.1f}% de faltas"
            }

        if media >= self.MEDIA_APROVACAO:
            return {"status": "Aprovado", "media": round(media, 2)}
        
        elif media >= self.MEDIA_MINIMA_EXAME:
            nota_necessaria = (self.MEDIA_FINAL_APOS_EXAME * 2) - media
            return {
                "status": "Exame", 
                "media": round(media, 2),
                "precisa_tirar": round(max(nota_necessaria, 3.0), 2)
            }
        
        else:
            return {"status": "Reprovado por Nota", "media": round(media, 2)}