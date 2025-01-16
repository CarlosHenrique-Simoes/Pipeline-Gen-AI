import time
import streamlit as st
from streamlit import rerun

# Lista de usuários
users = {"priscila.e": None, "rodrigo.v": None, "edson.s": None}

port_code = ["CNSHA", "CNSZX", "CNTAO", "KRPUS", "THLCH", "VNSGN", "VNHPH"]

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
    """
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

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        [
            "Dados do Importador",
            "Peso e Cubagem",
            "Dados do Embarque",
            "Dados do Frete",
            "Container",
        ],
    )

    # Formulário para Dados do Importador na Aba 1
    with tab1:
        st.subheader("Dados do Importador")
        with st.form(key="importador_form"):
            col1, col2 = st.columns(2)

            with col1:
                st.session_state.house_bl = st.text_input(
                    "House BL", value=st.session_state.get("house_bl", "")
                )

            with col2:
                st.session_state.master_bl = st.text_input(
                    "Master BL", value=st.session_state.get("master_bl", "")
                )

            with col1:
                st.session_state.shipper = st.text_input(
                    "Shipper", value=st.session_state.get("shipper", "")
                )

            with col2:
                st.session_state.consignee = st.radio(
                    "Consignee",
                    ["SEDA", "SDS"],
                    index=st.session_state.get("consignee", 0),
                )

            with col1:
                st.session_state.notify = st.text_input(
                    "Notify", value=st.session_state.get("notify", "")
                )

            with col2:
                st.session_state.consignee_text = st.text_input(
                    "Consignee (Texto)",
                    value=st.session_state.get("consignee_text", ""),
                )

            submit_button = st.form_submit_button("Enviar")

            if submit_button:
                st.success("Formulário de Importador enviado com sucesso!")

    # Formulário para Peso e Cubagem na Aba 2
    with tab2:
        st.subheader("Peso e Cubagem")
        with st.form(key="peso_form"):
            col1, col2 = st.columns(2)

            with col1:
                st.session_state.quantidade_de_embalagem = st.number_input(
                    "Quantidade de Embalagem", min_value=0.0, format="%.1f"
                )

            with col2:
                st.session_state.tipo_de_embalagem = st.text_input(
                    "Tipo de Embalagem",
                    value=st.session_state.get("tipo_de_embalagem", ""),
                )

            with col1:
                st.session_state.peso_bruto = st.number_input(
                    "Peso Bruto", min_value=0.0, format="%.3f"
                )

            with col2:
                st.session_state.cubagem = st.number_input(
                    "Cubagem", min_value=0.0, format="%.3f"
                )

            submit_button = st.form_submit_button("Enviar Peso e Cubagem")

            if submit_button:
                st.success("Dados de Peso e Cubagem enviados com sucesso!")

    # Formulário para Dados do Embarque na Aba 3
    with tab3:
        st.subheader("Dados do Embarque")
        with st.form(key="embarque_form"):
            col1, col2 = st.columns(2)

            with col1:
                st.session_state.port_of_loading = st.text_input(
                    "Porto de Origem",
                    value=st.session_state.get("port_of_loading", ""),
                    max_chars=5,
                )

            with col2:
                st.session_state.port_of_discharge = st.text_input(
                    "Porto de Destino",
                    value=st.session_state.get("port_of_discharge", ""),
                    max_chars=5,
                )

            with col1:
                st.session_state.vessel_origin = st.text_input(
                    "Navio de Origem", value=st.session_state.get("vessel_origin", "")
                )

            with col2:
                st.session_state.viagem = st.text_input(
                    "Número da Viagem", value=st.session_state.get("viagem", "")
                )

            submit_button = st.form_submit_button("Enviar Dados do Embarque")

            if submit_button:
                st.success("Dados do Embarque enviados com sucesso!")

    # Exemplo de outros formulários nas demais abas
    # Dados do Frete na Aba 4 e Container na Aba 5 podem seguir a mesma estrutura

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

    col1, col2, col3 = st.columns([1.5, 3.5, 1.5], gap="large")
    with col1:
        if st.button("Login", key="login_button"):
            if authenticate(username, password):
                st.session_state.user_id = username
                st.success(f"Bem-vindo, {username}! Login efetuado com sucesso.")
                time.sleep(0.8)
                st.session_state.page = "main"  # Muda para a página principal
                rerun()
            elif username not in st.session_state.user_credentials:
                st.error("Usuário não registrado.")
            else:
                st.error("Nome de usuário ou senha incorretos.")

    with col3:
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
            st.error("Nome de usuário já registrado.")
        elif len(new_username) == 0 or len(new_password) == 0:
            st.error("Nome de usuário e senha não podem estar vazios.")
        elif register(new_username, new_password):
            st.success(f"Usuário {new_username} registrado com sucesso!")
            time.sleep(0.8)
            st.session_state.page = "home"  # Redireciona para o login após o cadastro
            rerun()


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
