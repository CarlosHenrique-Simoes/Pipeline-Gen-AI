import streamlit as st
from streamlit import rerun
# Inicialize o dicionário de credenciais no estado da sessão
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
# def main_page():
#     st.title("Bem-vindo à página principal")
#     st.write("Aqui estão as funcionalidades do seu app.")
#     if st.button("Sair", key="logout"):
#         st.session_state.user_id = None
#         st.session_state.page = "home"  # Volta para a página inicial
#         rerun()


def main_page():
    st.title("Bem-vindo à página principal")
    st.write("Aqui estão as funcionalidades do seu app.")

    # Criando o formulário com vários tipos de entradas
    with st.form("my_form"):
        # Campo de texto
        house_bl = st.text_input("Digite seu House BL", key="house_bl")
        master_bl = st.text_input("Digite seu Master BL", key="master_bl")

        # Campo de data
        onboard_date = st.date_input(
            "Onboard date", key="onboard_date"
        )
        issue_date = st.date_input("Issue date", key="issue_date")

        # Caixa de seleção (checkbox)
        accept_terms = st.checkbox(
            "Eu aceito os termos e condições", key="accept_terms"
        )

        # Campo dropdown (selectbox)
        favorite_color = st.selectbox(
            "Selecione sua cor favorita",
            ["Azul", "Verde", "Vermelho", "Amarelo", "Preto", "Branco"],
            key="favorite_color",
        )

        # Botão para enviar o formulário
        submit_button = st.form_submit_button("Enviar")

    # Ação após o envio do formulário
    if submit_button:
        if not accept_terms:
            st.error("Você deve aceitar os termos e condições para continuar.")
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
    st.title("Sistema de Autenticação de Usuário")
    st.subheader("Por favor, faça o login")

    username = st.text_input("Nome de usuário", key="login_username")
    password = st.text_input("Senha", type="password", key="login_password")

    if st.button("Login", key="login_button"):
        if authenticate(username, password):
            st.session_state.user_id = username
            st.success(f"Bem-vindo, {username}!")
            st.session_state.page = "main"  # Muda para a página principal
            rerun()  # Faz o rerun para atualizar a página
        else:
            st.error("Nome de usuário ou senha incorretos.")


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
        elif len(new_username) == 0 or len(new_password) == 0:
            st.error("Nome de usuário e senha não podem estar vazios.")
        else:
            if register(new_username, new_password):
                st.success(
                    f"Usuário {new_username} registrado com sucesso! Redirecionando para o login..."
                )
                st.session_state.page = (
                    "login"  # Redireciona para o login após o cadastro
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
        st.title("Bem-vindo ao sistema de cadastro de embarques marítimos")
        st.subheader("Escolha uma opção:")

        col1, col2 = st.columns(2)

        with col1:
            if st.button("Login", key="login_select_button"):
                st.session_state.page = "login"
                rerun()

        with col2:
            if st.button("Cadastro", key="register_select_button"):
                st.session_state.page = "register"
                rerun()

    # Carregar a página de acordo com a escolha do usuário
    elif st.session_state.page == "login":
        login_page()
    elif st.session_state.page == "register":
        register_page()

# Se o usuário estiver logado, mostrar a página principal
else:
    main_page()
