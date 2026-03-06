Repository ##########

Métodos esperados:

listar_disciplinas()
criar_disciplina()
remover_disciplina()
atualizar_disciplina()

Integração com Frontend ##########

Eles devem substituir:

# service.criar_disciplina(...)

Estrutura de projeto ##########

projeto/

app.py

services/
   disciplina_service.py

repositories/
   disciplina_repository.py

database/
   connection.py

Estrutura da tabela no Supabase ################

Tabela:

disciplinas

Campos:

id (int, primary key)
nome (text)
curso (text)
dia (text)
