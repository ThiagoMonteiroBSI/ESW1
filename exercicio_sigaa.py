import unittest
from regras_sigaa import AvaliadorSigaa


GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"

class TestRelatorioNotasSIGAA(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print(f"\n{BOLD}{'='*75}")
        print(f"{'SISTEMA INTEGRADO DE GESTÃO DE ATIVIDADES ACADÊMICAS - IFC':^75}")
        print(f"{'='*75}{RESET}")
        print(f"{BOLD}{'ALUNO':<15} | {'MÉDIA':<6} | {'STATUS':<25} | {'OBSERVAÇÃO'}{RESET}")
        print("-" * 75)

    def setUp(self):
        self.avaliador = AvaliadorSigaa(carga_horaria_total=60)

    def imprimir_linha(self, nome, resultado):
        cor = GREEN if resultado["status"] == "Aprovado" else YELLOW
        if "Reprovado" in resultado["status"]: cor = RED
        
        status = resultado["status"]
        media = resultado.get("media", 0.0)
        obs = f"Precisa de {resultado['precisa_tirar']} no exame" if "precisa_tirar" in resultado else "-"
        
        print(f"{nome:<15} | {media:<6.2f} | {cor}{status:<25}{RESET} | {obs}")

    def test_aluno_Thiago(self):
        res = self.avaliador.processar_status(notas=[8.5, 9.0], faltas_em_horas=2)
        self.imprimir_linha("Thiago", res)
        self.assertEqual(res["status"], "Aprovado")

    def test_aluno_Mirella(self):
        res = self.avaliador.processar_status(notas=[5.0, 6.0], faltas_em_horas=5)
        self.imprimir_linha("Mirella", res)
        self.assertEqual(res["status"], "Exame")

    def test_aluno_Kelvin(self):
        res = self.avaliador.processar_status(notas=[10.0, 10.0], faltas_em_horas=20)
        self.imprimir_linha("Kelvin", res)
        self.assertEqual(res["status"], "Reprovado por Frequência")

    def test_aluno_Guilherme(self):
        res = self.avaliador.processar_status(notas=[2.0, 1.5], faltas_em_horas=0)
        self.imprimir_linha("Guilherme", res)
        self.assertEqual(res["status"], "Reprovado por Nota")

if __name__ == '__main__':
    unittest.main(verbosity=2)