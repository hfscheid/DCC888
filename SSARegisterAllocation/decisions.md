- O exercício consiste em implementar as funções principais apresentadas no artigo
- Necessária uma estrutura intermediária para o grafo de interseções: IntersectionGraph
- Reaproveita Liveness Analysis
- Necessário adaptar instruções para aceitar valores numéricos, reduzindo o
  número de variáveis e tornando a análise mais intuitiva e fácil de se verficar
- Registradores só são atribuídos a variáveis presentes na liveness analysis.
  Assim, variáveis inutilizadas são invisíveis aos registradores
