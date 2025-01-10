import time

import streamlit as st
from streamlit import rerun

# Lista de usuários
users = {"priscila.e": None, "rodrigo.v": None, "edson.s": None}

# Inicialize o dicionário de credenciais no estado da sessão
if "user_credentials" not in st.session_state:
    st.session_state.user_credentials = users


# Função de autenticação
def authenticate(username: str, password: str) -> bool:
    """Verifica se o usuário e senha informados correspondem às credenciais no estado da sessão.

    Args:
        username (str): Nome de usuário.
        password (str): Senha.

    Returns:
        bool: True caso as credenciais sejam válidas, False caso contrário.

    """  # noqa: E501
    return bool(
        username in st.session_state.user_credentials
        and st.session_state.user_credentials[username] == password,
    )


# Função para registrar novo usuário
def register(username, password):
    if username in st.session_state.user_credentials:
        if st.session_state.user_credentials[username] is None:
            st.session_state.user_credentials[username] = password
            return True  # Usuário registrado com sucesso
        else:
            return False  # Usuário já registrado
    else:
        # Se o usuário ainda não estiver registrado, adicione-o ao dicionário
        st.session_state.user_credentials[username] = password
        return True  # Novo usuário registrado com sucesso


def main_page():
    st.title("Cadastro de Embarque Marítimo")
    st.subheader("Preencha o formulário abaixo")

    # Criando o formulário com vários tipos de entradas
    with st.form("my_form"):
        # Campo dropdown (selectbox)
        pol = st.selectbox(
            "Selecione a Origem",
            ["", "CNSHA", "CNSZX", "CNTAO", "KRPUS", "THLCH", "VNSGN", "VNHPH"],
            key="pol",
        )
        # Campo de texto
        house_bl = st.text_input("Informe o House BL", key="house_bl")
        master_bl = st.text_input("Informe o Master BL", key="master_bl")

        # Campo de data
        onboard_date = st.date_input("Onboard date", key="onboard_date")
        issue_date = st.date_input("Issue date", key="issue_date")

        # Caixa de seleção (checkbox)
        accept_terms = st.checkbox(
            "Eu aceito os termos e condições", key="accept_terms"
        )

        # Botão para enviar o formulário
        submit_button = st.form_submit_button("Enviar")

    # Ação após o envio do formulário
    if submit_button:
        if house_bl == "" or master_bl == "" or onboard_date == "" or issue_date == "":
            st.error("Por favor, preencha todos os campos!")
        elif not accept_terms:
            st.error("Por favor, aceite os termos e condições.")
        else:
            st.success(f"Obrigado, {name}! Seus dados foram enviados com sucesso.")
            st.write(f"Data de Nascimento: {birthdate}")
            st.write(f"Cor Favorita: {favorite_color}")

    # Botão para sair
    if st.button("Sair", key="logout"):
        st.session_state.user_id = None
        st.session_state.page = "home"  # Volta para a página inicial
        rerun()


# Função para exibir a página de login
def login_page():
    st.title("Sistema de Cadastro de Embarques Marítimos")
    st.subheader("Por favor, faça o login")

    username = st.text_input("Nome de usuário", key="login_username")
    password = st.text_input("Senha", type="password", key="login_password")

    coluna1, coluna2, coluna3 = st.columns([1, 3.5, 1], gap="large")
    with coluna1:
        if st.button("Login", key="login_button"):
            if authenticate(username, password):
                st.session_state.user_id = username
                st.success(f"Bem-vindo, {username}! Login efetuado com sucesso.")
                time.sleep(1.6)
                st.session_state.page = "main"  # Muda para a página principal
                rerun()  # Faz o rerun para atualizar a página
            elif username not in st.session_state.user_credentials:
                st.error("Usuário não registrado.")
            else:
                st.error("Nome de usuário ou senha incorretos.")

    with coluna3:
        if st.button("Registrar", key="register_button"):
            st.session_state.page = "register"  # Muda para a página de cadastro
            rerun()


# Função para exibir a página de cadastro
def register_page():
    st.title("Cadastro de Novo Usuário")
    st.subheader("Crie um usuário e senha")

    new_username = st.text_input("Novo nome de usuário", key="register_username")
    new_password = st.text_input("Nova senha", type="password", key="register_password")
    confirm_password = st.text_input(
        "Confirme a senha", type="password", key="confirm_password"
    )

    if st.button("Registrar", key="register_button"):
        if new_password != confirm_password:
            st.error("As senhas não coincidem.")
        elif new_username in st.session_state.user_credentials:
            st.error("Nome de usuário já registrado. Tente outro.")
        elif len(new_username) == 0 or len(new_password) == 0:
            st.error("Nome de usuário e senha não podem estar vazios.")
        elif register(new_username, new_password):
            st.success(
                f"Usuário {new_username} registrado com sucesso! Redirecionando para o login..."
            )
            time.sleep(1.6)
            st.session_state.page = (
                "home"  # Redireciona para o login após o cadastro
            )
            rerun()  # Faz o rerun para atualizar a página


# Inicialização do session_state para manter o controle do usuário e da página
if "user_id" not in st.session_state:
    st.session_state.user_id = None
if "page" not in st.session_state:
    st.session_state.page = "home"  # Página inicial padrão

# Controle da página baseada no estado do usuário
if st.session_state.user_id is None:
    if st.session_state.page == "home":
        login_page()
    elif st.session_state.page == "register":
        register_page()

# Se o usuário estiver logado, mostrar a página principal
else:
    main_page()
