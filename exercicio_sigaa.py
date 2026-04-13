import unittest

from regras_sigaa import AvaliadorSigaa

class TestRelatorioNotasSIGAA(unittest.TestCase):
    
    def setUp(self):
        
        self.avaliador = AvaliadorSigaa(carga_horaria_total=60) # Disciplina de Engenharia para 60h

    def test_aluno_Thiago_Aprovado(self):
        status = self.avaliador.processar_status(notas=[8.5, 9.0], faltas_em_horas=2)
        print(f"\nVerificando Thiago: Status esperado 'Aprovado' -> Obtido: '{status}'")
        self.assertEqual(status, "Aprovado")

    def test_aluno_Mirella_Exame(self):
        status = self.avaliador.processar_status(notas=[5.0, 6.0], faltas_em_horas=5)
        print(f"Verificando Mirella: Status esperado 'Exame' -> Obtido: '{status}'")
        self.assertEqual(status, "Exame")

    def test_aluno_Kelvin_Reprovado_Falta(self):
        status = self.avaliador.processar_status(notas=[10.0, 10.0], faltas_em_horas=20)
        print(f"Verificando Kelvin: Status esperado 'Reprovado por Frequência' -> Obtido: '{status}'")
        self.assertEqual(status, "Reprovado por Frequência")

    def test_aluno_Guilherme_Reprovado_Nota(self):
        status = self.avaliador.processar_status(notas=[2.0, 1.5], faltas_em_horas=0)
        print(f"Verificando Guilherme: Status esperado 'Reprovado por Nota' -> Obtido: '{status}'")
        self.assertEqual(status, "Reprovado por Nota")

if __name__ == '__main__':
    unittest.main()

