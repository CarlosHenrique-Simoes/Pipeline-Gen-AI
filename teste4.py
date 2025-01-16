import time

import streamlit as st
from streamlit import rerun

# Lista de usuários
users = {"priscila.e": None, "rodrigo.v": None, "edson.s": None}

port_code = [
    "CNSHA",
    "CNSZX",
    "CNTAO",
    "KRPUS",
    "THLCH",
    "VNSGN",
    "VNHPH",
]

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


def next_tab():
    st.session_state.current_tab += 1


def previous_tab():
    st.session_state.current_tab -= 1


def is_filled():
    return all(
        [
            st.session_state.get(field)
            for field in [
                "nome",
                "idade",
                "genero",
                "rua",
                "cidade",
                "cep",
                "email",
                "telefone",
            ]
        ]
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

    col1, col2 = st.columns(2)

    # Criando o formulário com vários tipos de entradas
    with tab1:
        st.subheader("Dados do Importador")

        with col1:
            # Campo de texto
            st.session_state.house_bl = st.text_input(
                "House BL",
                value=st.session_state.get("house_bl", ""),
            )

        with col2:
            st.session_state.master_bl = st.text_input(
                "Master BL",
                value=st.session_state.get("master_bl", ""),
            )

        with col1:
            st.session_state.shipper = st.text_input(
                "Shipper",
                value=st.session_state.get("shipper", ""),
            )

        with col2:
            st.session_state.consignee = st.radio(
                "Consignee",
                ["SEDA", "SDS"],
                index=st.session_state.get("consignee",),
            )
        with col1:
            st.session_state.notify = st.text_input(
                "Notify",
                value=st.session_state.get("notify", ""),
            )

        with col2:
            st.session_state.consignee = st.text_input(
                "Consignee",
                value=st.session_state.get("consignee", ""),
            )

        # with col1:
        #     # Campo dropdown (selectbox)
        #     port_of_loading = st.text_input(
        #         "Porto de Origem",
        #         value=st.session_state.get("port_of_loading", ""),
        #         max_chars=5,
        #     )

        #     st.session_state.port_of_loading = port_of_loading
        #     st.session_state.place_of_receipt = st.session_state.port_of_loading

        # with col2:
        #     st.session_state.port_of_discharge = st.text_input(
        #         "Porto de Destino",
        #         value=st.session_state.get("port_of_discharge", ""),
        #         max_chars=5,
        #     )

        # with col1:
        #     st.session_state.vessel_origin = st.text_input(
        #         "Navio de Origem",
        #         value=st.session_state.get("vessel_origin", ""),
        #     )

        # with col2:
        #     st.session_state.viagem = st.text_input(
        #         "Número da Viagem",
        #         value=st.session_state.get("viagem", ""),
        #     )


        # quantidade_de_embalagem = st.number_input(
        #     "Quantidade de Embalagem",
        #     min_value=0.0,
        #     format="%.1f",
        #     key="quantidade_de_embalagem",
        # )
        # tipo_de_embalagem = st.text_input(
        #     "Tipo de Embalagem",
        #     key="tipo_de_embalagem",
        # )
        # peso_bruto = st.number_input(
        #     "Informe o Peso Bruto",
        #     min_value=0.0,
        #     format="%.3f",
        #     key="peso_bruto",
        # )
        # cubagem = st.number_input(
        #     "Informe a Cubagem do House",
        #     min_value=0.0,
        #     format="%.3f",
        #     key="cubagem",
        # )
        # frete = st.text_input(
        #     "Informe o Frete",
        #     min_value=0.0,
        #     format="%.2f",
        #     key="frete",
        # )

        # # Campo de data
        # onboard_date = st.date_input(
        #     "Onboard date",
        #     key="onboard_date",
        # )
        # issue_date = st.date_input("Issue date", key="issue_date")

        # Botão para enviar o formulário
        # submit_button = st.form_submit_button("Enviar")

    # Ação após o envio do formulário
    # if submit_button:
    #     if (
    #         house_bl == ""
    #         or master_bl == ""
    #         or onboard_date == ""
    #         or issue_date == ""
    #         or place_of_receipt == ""
    #         or port_of_discharge == ""
    #         or vessel == ""
    #         or viagem == ""
    #         or quantidade_de_embalagem == ""
    #         or tipo_de_embalagem == ""
    #         or peso_bruto == ""
    #         or cubagem == ""
    #         or frete == ""
    #     ):
    #         st.error("Por favor, preencha todos os campos!")
    #     else:
    #         st.success(f"Dados enviados com sucesso.")
    #         st.write(f"Origem: {port_of_loading}")
    #         st.write(f"House BL: {house_bl}")
    #         st.write(f"Master BL: {master_bl}")
    #         st.write(f"Local de Recebimento: {place_of_receipt}")
    #         st.write(f"Porto de Destino: {port_of_discharge}")
    #         st.write(f"Navio de Origem: {vessel}")
    #         st.write(f"Viagem: {viagem}")
    #         st.write(f"Quantidade de Embalagem: {quantidade_de_embalagem}")
    #         st.write(f"Tipo de Embalagem: {tipo_de_embalagem}")
    #         st.write(f"Peso Bruto: {peso_bruto}")
    #         st.write(f"Cubagem: {cubagem}")
    #         st.write(f"Data de embarque: {onboard_date}")
    #         st.write(f"Data de emissão: {issue_date}")

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

    coluna1, coluna2, coluna3 = st.columns([1.5, 3.5, 1.2], gap="large")
    with coluna1:
        if st.button("Login", key="login_button"):
            if authenticate(username, password):
                st.session_state.user_id = username
                st.success(f"Bem-vindo, {username}! Login efetuado com sucesso.")
                time.sleep(0.8)
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
            time.sleep(0.8)
            st.session_state.page = "home"  # Redireciona para o login após o cadastro
            rerun()  # Faz o rerun para atualizar a página


# Inicialização do session_state para manter o controle do usuário e da página
if "user_id" not in st.session_state:
    st.session_state.user_id = None
if "page" not in st.session_state:
    st.session_state.page = "home"  # Página inicial padrão
if "current_tab" not in st.session_state:
    st.session_state.current_tab = 0

# Controle da página baseada no estado do usuário
if st.session_state.user_id is None:
    if st.session_state.page == "home":
        login_page()
    elif st.session_state.page == "register":
        register_page()

# Se o usuário estiver logado, mostrar a página principal
else:
    main_page()
