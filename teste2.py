import streamlit as st
from streamlit import rerun

# Inicialize o dicionário de credenciais
if "user_credentials" not in st.session_state:
    st.session_state.user_credentials = {}


# Função de autenticação
def authenticate(username, password):
    if (
        username in st.session_state.user_credentials
        and st.session_state.user_credentials[username] == password
    ):
        return True
    else:
        return False


# Função para registrar novo usuário
def register(username, password):
    if username in st.session_state.user_credentials:
        return False  # Usuário já existe
    else:
        st.session_state.user_credentials[username] = password
        return True


# Função para exibir a página principal após login
def main_page():
    st.title("Bem-vindo à página principal")
    st.write("Aqui estão as funcionalidades do seu app.")
    st.button("Sair", on_click=lambda: st.session_state.update({"user_id": None}))
    rerun()


# Função para exibir a página de login
def login_page():
    st.title("Sistema de Autenticação")
    st.subheader("Por favor, faça o login")

    username = st.text_input("Nome de usuário")
    password = st.text_input("Senha", type="password")

    if st.button("Login"):
        if authenticate(username, password):
            st.session_state.user_id = username
            st.success(f"Bem-vindo, {username}!")
            # st.session_state.page = "main"
            rerun()  # Força a mudança de tela após o login
        else:
            st.error("Nome de usuário ou senha incorretos.")


# Função para exibir a página de cadastro
def register_page():
    st.title("Cadastro de Novo Usuário")
    st.subheader("Crie um novo nome de usuário e senha")

    new_username = st.text_input("Novo nome de usuário")
    new_password = st.text_input("Nova senha", type="password")
    confirm_password = st.text_input("Confirme a senha", type="password")

    if st.button("Registrar"):
        if new_password != confirm_password:
            st.error("As senhas não coincidem.")
        elif len(new_username) == 0 or len(new_password) == 0:
            st.error("Nome de usuário e senha não podem estar vazios.")
        else:
            if register(new_username, new_password):
                st.success(
                    f"Usuário {new_username} registrado com sucesso! Agora você pode fazer login."
                )
                # Atualiza a página para o login após o cadastro
                st.session_state.page = "login"
                rerun()
            else:
                st.error("Nome de usuário já existe. Tente outro.")


# Inicialização do session_state
if "user_id" not in st.session_state:
    st.session_state.user_id = None

# Exibir a página inicial com os botões de login e cadastro
if st.session_state.user_id is None:
    st.title("Bem-vindo ao sistema")
    st.subheader("Escolha uma opção:")

    # Botões para selecionar entre Login e Cadastro
    col1, col2 = st.columns(2, gap="large")

    with col1:
        if st.button("Login", key="login_button"):
            st.session_state.page = "login"
            rerun()  # Forçar a atualização da página para mudar para o login

    with col2:
        if st.button("Cadastro", key="register_button"):
            st.session_state.page = "register"
            rerun()  # Forçar a atualização da página para a página cadastro

    # Carregar a página de acordo com a escolha do usuário
    if "page" in st.session_state:
        if st.session_state.page == "login":
            login_page()
        elif st.session_state.page == "register":
            register_page()
        elif st.session_state.page == "main":
            main_page()

# Se o usuário já estiver logado, mostrar a página principal
else:
    main_page()
