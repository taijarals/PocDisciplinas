import streamlit as st
import pandas as pd
from services.disciplina_service import DisciplinaService


class App:

    def __init__(self):
        self.service = DisciplinaService()

    def executar(self):

        st.title("Sistema de Disciplinas")

        st.divider()

        self.tela_cadastro()

        st.divider()

        self.tela_listagem()

        st.divider()

        self.tela_remover()

        st.divider()

        self.tela_atualizar()

    # ====================================
    # CADASTRO
    # ====================================

    def tela_cadastro(self):

        st.subheader("Cadastrar disciplina")

        nome = st.text_input("Nome da disciplina")
        curso = st.text_input("Curso")
        dia = st.text_input("Dia da aula")

        if st.button("Salvar disciplina"):

            self.service.criar_disciplina(nome, curso, dia)

            st.success("Disciplina salva")

    # ====================================
    # LISTAGEM
    # ====================================

    def tela_listagem(self):

        st.subheader("Disciplinas cadastradas")

        disciplinas = self.service.listar_disciplinas()

        df = pd.DataFrame(disciplinas)

        st.dataframe(df, use_container_width=True)

    # ====================================
    # REMOVER
    # ====================================

    def tela_remover(self):

        st.subheader("Remover disciplina")

        id_remover = st.number_input("ID da disciplina", step=1)

        if st.button("Remover"):

            self.service.remover_disciplina(id_remover)

            st.warning(f"Disciplina {id_remover} removida")

    # ====================================
    # ATUALIZAR
    # ====================================

    def tela_atualizar(self):

        st.subheader("Atualizar disciplina")

        id_editar = st.number_input("ID da disciplina", step=1)

        novo_nome = st.text_input("Novo nome")
        novo_curso = st.text_input("Novo curso")
        novo_dia = st.text_input("Novo dia")

        if st.button("Atualizar disciplina"):

            self.service.atualizar_disciplina(
                id_editar,
                novo_nome,
                novo_curso,
                novo_dia
            )

            st.info("Disciplina atualizada")


# ====================================
# EXECUÇÃO DA APLICAÇÃO
# ====================================

app = App()
app.executar()
