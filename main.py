import streamlit as st
import pandas as pd

st.title("Sistema de Disciplinas")

st.divider()

# ====================================
# FORMULÁRIO DE CADASTRO
# ====================================

st.subheader("Cadastrar disciplina")

nome = st.text_input("Nome da disciplina")
curso = st.text_input("Curso")
dia = st.text_input("Dia da aula")

if st.button("Salvar disciplina"):

    # AQUI OS ALUNOS DEVEM CHAMAR O SERVICE
    # service.criar_disciplina(nome, curso, dia)

    st.success("Disciplina salva (simulação)")

st.divider()

# ====================================
# LISTAGEM DE DISCIPLINAS
# ====================================

st.subheader("Disciplinas cadastradas")

# AQUI OS ALUNOS DEVEM BUSCAR DO SERVICE
# disciplinas = service.listar_disciplinas()

# DADOS MOCK PARA UI FUNCIONAR
disciplinas = [
    {"id": 1, "nome": "Algoritmos", "curso": "Computação", "dia": "Segunda"},
    {"id": 2, "nome": "Banco de Dados", "curso": "Computação", "dia": "Quarta"},
]

df = pd.DataFrame(disciplinas)

st.dataframe(df, use_container_width=True)

st.divider()

# ====================================
# REMOVER DISCIPLINA
# ====================================

st.subheader("Remover disciplina")

id_remover = st.number_input("ID da disciplina", step=1)

if st.button("Remover"):

    # AQUI OS ALUNOS DEVEM CHAMAR O SERVICE
    # service.remover_disciplina(id_remover)

    st.warning(f"Disciplina {id_remover} removida (simulação)")

st.divider()

# ====================================
# ATUALIZAR DISCIPLINA
# ====================================

st.subheader("Atualizar disciplina")

id_editar = st.number_input("ID da disciplina para editar", step=1)

novo_nome = st.text_input("Novo nome")
novo_curso = st.text_input("Novo curso")
novo_dia = st.text_input("Novo dia")

if st.button("Atualizar disciplina"):

    # AQUI OS ALUNOS DEVEM CHAMAR O SERVICE
    # service.atualizar_disciplina(id_editar, novo_nome, novo_curso, novo_dia)

    st.info("Disciplina atualizada (simulação)")
