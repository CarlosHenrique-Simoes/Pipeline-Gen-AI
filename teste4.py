import time

import streamlit as st
from streamlit import rerun

import pandas as pd

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

ncms = ["7318", "8415", "8501", "4518", "4517", "4516", "4523", "4815"]
containers = []


# Inicialização do session_state para manter o controle do usuário e da página
if "user_id" not in st.session_state:
    st.session_state["user_id"] = None
if "page" not in st.session_state:
    st.session_state["page"] = "home"  # Página inicial padrão
if "current_tab" not in st.session_state:
    st.session_state["current_tab"] = 0

if "user_credentials" not in st.session_state:
    st.session_state["user_credentials"] = users

if "num_containers" not in st.session_state:
    st.session_state["num_containers"] = 0

if "house_bl" not in st.session_state:
    st.session_state["house_bl"] = None

if "master_bl" not in st.session_state:
    st.session_state["master_bl"] = None

if "shipper" not in st.session_state:
    st.session_state["shipper"] = None

if "consignee" not in st.session_state:
    st.session_state["consignee"] = None

if "notify" not in st.session_state:
    st.session_state["notify"] = None

if "port_of_loading" not in st.session_state:
    st.session_state["port_of_loading"] = None

if "port_of_discharge" not in st.session_state:
    st.session_state["port_of_discharge"] = None

if "vessel_origin" not in st.session_state:
    st.session_state["vessel_origin"] = None

if "vessel_voyage" not in st.session_state:
    st.session_state["vessel_voyage"] = None

if "gross_weight" not in st.session_state:
    st.session_state["gross_weight"] = None

if "cbm" not in st.session_state:
    st.session_state["cbm"] = None

if "package_quantity" not in st.session_state:
    st.session_state["package_quantity"] = None

if "package_type" not in st.session_state:
    st.session_state["package_type"] = None

if "onboard_date" not in st.session_state:
    st.session_state["onboard_date"] = None

if "issue_date" not in st.session_state:
    st.session_state["issue_date"] = None

if "freight" not in st.session_state:
    st.session_state["freight"] = None

if "freight_currency" not in st.session_state:
    st.session_state["freight_currency"] = None

if "terminal_handling" not in st.session_state:
    st.session_state["terminal_handling"] = None

if "terminal_handling_currency" not in st.session_state:
    st.session_state["terminal_handling_currency"] = None

if "documentation_fee" not in st.session_state:
    st.session_state["documentation_fee"] = None

if "documentation_fee_currency" not in st.session_state:
    st.session_state["documentation_fee_currency"] = None

if "fourth_fee" not in st.session_state:
    st.session_state["fourth_fee"] = None

if "fourth_fee_currency" not in st.session_state:
    st.session_state["fourth_fee_currency"] = None

if "fifth_fee" not in st.session_state:
    st.session_state["fifth_fee"] = None

if "fifth_fee_currency" not in st.session_state:
    st.session_state["fifth_fee_currency"] = None

if "sixth_fee" not in st.session_state:
    st.session_state["sixth_fee"] = None

if "sixth_fee_currency" not in st.session_state:
    st.session_state["sixth_fee_currency"] = None

if "seventh_fee" not in st.session_state:
    st.session_state["seventh_fee"] = None

if "seventh_fee_currency" not in st.session_state:
    st.session_state["seventh_fee_currency"] = None

if "eighth_fee" not in st.session_state:
    st.session_state["eighth_fee"] = None

if "eighth_fee_currency" not in st.session_state:
    st.session_state["eighth_fee_currency"] = None

if "ninth_fee" not in st.session_state:
    st.session_state["ninth_fee"] = None

if "ninth_fee_currency" not in st.session_state:
    st.session_state["ninth_fee_currency"] = None

if "tenth_fee" not in st.session_state:
    st.session_state["tenth_fee"] = None

if "tenth_fee_currency" not in st.session_state:
    st.session_state["tenth_fee_currency"] = None

if "eleventh_fee" not in st.session_state:
    st.session_state["eleventh_fee"] = None

if "eleventh_fee_currency" not in st.session_state:
    st.session_state["eleventh_fee_currency"] = None

if "twelfth_fee" not in st.session_state:
    st.session_state["twelfth_fee"] = None

if "twelfth_fee_currency" not in st.session_state:
    st.session_state["twelfth_fee_currency"] = None

if "thirteenth_fee" not in st.session_state:
    st.session_state["thirteenth_fee"] = None

if "thirteenth_fee_currency" not in st.session_state:
    st.session_state["thirteenth_fee_currency"] = None

if "fourteenth_fee" not in st.session_state:
    st.session_state["fourteenth_fee"] = None

if "fourteenth_fee_currency" not in st.session_state:
    st.session_state["fourteenth_fee_currency"] = None

if "fifteenth_fee" not in st.session_state:
    st.session_state["fifteenth_fee"] = None

if "fifteenth_fee_currency" not in st.session_state:
    st.session_state["fifteenth_fee_currency"] = None

if "hbl_freight" not in st.session_state:
    st.session_state["hbl_freight"] = None

if "hbl_container" not in st.session_state:
    st.session_state["hbl_container"] = None


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
    st.session_state["current_tab"] += 1


def previous_tab():
    st.session_state["current_tab"] -= 1


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
    st.set_page_config(
        layout="wide",
        page_title="Ocean Inbound",
        page_icon="🚢",
    )

    col1, col2 = st.columns(2)
    with col2:
        st.image("samsung sds.png", width=480)
    with col1:
        st.title("Cadastro de Embarque Marítimo")

    # Criando o formulário com vários tipos de entradas
    with st.form("dados_do_importador"):  # Dados do Importador
        tab1, tab2, tab3 = st.tabs(
            [
                "Dados do Importador ⚓",
                "Frete 💰",
                "Container 📦",
            ],
        )

        with tab1:
            col1, col2, col3 = st.columns(3)

            with col1:
                # Campo de texto
                house_bl = st.text_input(
                    "House BL",
                ).upper()
                master_bl = st.text_input(
                    "Master BL",
                ).upper()
                consignee = st.selectbox(
                    "Consignee",
                    ["SEDA", "SDS"],
                    index=0,
                )
                notify = st.selectbox(
                    "Notify",
                    ["SEDA", "SDS"],
                    index=0,
                )
                port_of_loading = st.selectbox(
                    "Porto de Origem",
                    port_code,
                )

            with col2:
                port_of_discharge = st.selectbox(
                    "Porto de Destino",
                    ["BRMAO", "BRSSZ", "BRRIO"],
                )
                vessel_origin = st.text_input(
                    "Navio de Origem",
                ).upper()
                vessel_voyage = st.text_input(
                    "Número da Viagem",
                ).upper()
                package_type = st.text_input(
                    "Tipo de Embalagem",
                    max_chars=3,
                ).upper()

                package_quantity = st.number_input(
                    "Quantidade de Embalagem",
                    min_value=0.0,
                    format="%.1f",
                )

            with col3:
                shipper = st.text_area(
                    label="Shipper",
                    height=123,
                )
                gross_weight = st.number_input(
                    "Informe o Peso Bruto",
                    min_value=0.0,
                    format="%.3f",
                )
                cbm = st.number_input(
                    "Informe a Cubagem do House",
                    min_value=0.0,
                    format="%.3f",
                )
                onboard_date = st.date_input(
                    "Onboard date",
                )
                # issue_date = st.date_input(
                #     "Issue date",
                # )


        with tab3:
            col1, col2, col3 = st.columns(3)

            with col1:
                hbl_container = st.text_input(
                    "HBL",
                ).upper()
                container_weight = st.number_input(
                    "Gross Weight",
                    min_value=0.0,
                    format="%.3f",
                )

            with col2:
                container = st.text_input(
                    "Container",
                ).upper()
                container_tare = st.number_input(
                    "Container Tare",
                    min_value=0.0,
                    format="%.3f",
                )

            with col3:
                container_type = st.selectbox(
                    "Container Type",
                    ["22GP", "45GP"],
                    index=0,
                )
                ncm = st.multiselect(
                    "NCMs",
                    ncms,
                    default=None,
                )
            if st.form_submit_button("Adicionar contêiner"):
                container_data = {
                    "hbl_container": hbl_container,
                    "container": container,
                    "container_weight": container_weight,
                    "container_tare": container_tare,
                    "container_type": container_type,
                    "ncm": ncm,
                }
                containers.append(container_data)
                st.success(
                    f"Contêiner {container} adicionado com sucesso.",
                )

                df_container = pd.DataFrame(containers)

                df_container = df_container[
                    [
                        "hbl_container",
                        "container",
                        "container_type",
                    ]
                ]

                st.write(df_container)

        with tab2:
            col1, col2 = st.columns(2)

            with col2:
                hbl_freight = st.text_input(
                    "House BL Frete",
                )

            with col1:
                escolha_de_taxa = st.radio(
                    "Escolha A Quantidade de Taxas",
                    [3, 5, 11, 15],
                    horizontal=True,
                    index=None,
                )

            if st.form_submit_button("Abrir Quantidade de taxas"):

                if escolha_de_taxa is None:
                    st.warning(
                        "Por favor, escolha a quantidade de taxas.",
                    )
                else:
                    col1, col2 = st.columns(2)

                    with col1:
                        if escolha_de_taxa >= 3:
                            freight = st.number_input(
                                "Informe o Frete",
                                min_value=0.0,
                                format="%.2f",
                            )
                            terminal_handling = st.number_input(
                                "Capatazia",
                                min_value=0.0,
                                format="%.2f",
                            )
                            documentation_fee = st.number_input(
                                "Doc Fee",
                                min_value=0.0,
                                format="%.2f",
                            )
                        if escolha_de_taxa >= 5:
                            fourth_fee = st.number_input(
                                "4ª Taxa",
                                min_value=0.0,
                                format="%.2f",
                            )
                            fifth_fee = st.number_input(
                                "5ª Taxa",
                                min_value=0.0,
                                format="%.2f",
                            )
                        if escolha_de_taxa >= 11:
                            sixth_fee = st.number_input(
                                "6ª Taxa",
                                min_value=0.0,
                                format="%.2f",
                            )
                            seventh_fee = st.number_input(
                                "7ª Taxa",
                                min_value=0.0,
                                format="%.2f",
                            )
                            eighth_fee = st.number_input(
                                "8ª Taxa",
                                min_value=0.0,
                                format="%.2f",
                            )
                            ninth_fee = st.number_input(
                                "9ª Taxa",
                                min_value=0.0,
                                format="%.2f",
                            )
                            tenth_fee = st.number_input(
                                "10ª Taxa",
                                min_value=0.0,
                                format="%.2f",
                            )
                            eleventh_fee = st.number_input(
                                "11ª Taxa",
                                min_value=0.0,
                                format="%.2f",
                            )
                        if escolha_de_taxa >= 15:
                            twelfth_fee = st.number_input(
                                "12ª Taxa",
                                min_value=0.0,
                                format="%.2f",
                            )
                            thirtheenth_fee = st.number_input(
                                "13ª Taxa",
                                min_value=0.0,
                                format="%.2f",
                            )
                            fourteenth_fee = st.number_input(
                                "14ª Taxa",
                                min_value=0.0,
                                format="%.2f",
                            )
                            fifteenth_fee = st.number_input(
                                "15ª Taxa",
                                min_value=0.0,
                                format="%.2f",
                            )
                    with col2:
                        if escolha_de_taxa >= 3:
                            freight_currency = st.selectbox(
                                "Moeda do Frete",
                                ["USD", "BRL"],
                                index=0,
                            )
                            terminal_handling_currency = st.selectbox(
                                "Moeda da Capatazia",
                                ["USD", "BRL"],
                                index=0,
                            )
                            documentation_fee_currency = st.selectbox(
                                "Moeda do Doc Fee",
                                ["USD", "BRL"],
                                index=0
                            )
                        if escolha_de_taxa >= 5:
                            fourth_fee_currency = st.selectbox(
                                "Moeda da 4ª Taxa",
                                ["USD", "BRL"],
                                index=0,
                            )
                            fifth_fee_currency = st.selectbox(
                                "Moeda da 5ª Taxa",
                                ["USD", "BRL"],
                                index=0,
                            )
                        if escolha_de_taxa >= 11:
                            sixth_fee_currency = st.selectbox(
                                "Moeda da 6ª Taxa",
                                ["USD", "BRL"],
                                index=0,
                            )
                            seventh_fee_currency = st.selectbox(
                                "Moeda da 7ª Taxa",
                                ["USD", "BRL"],
                                index=0,
                            )
                            eighth_fee_currency = st.selectbox(
                                "Moeda da 8ª Taxa",
                                ["USD", "BRL"],
                                index=0,
                            )
                            ninth_fee_currency = st.selectbox(
                                "Moeda da 9ª Taxa",
                                ["USD", "BRL"],
                                index=0,
                            )
                            tenth_fee_currency = st.selectbox(
                                "Moeda da 10ª Taxa",
                                ["USD", "BRL"],
                                index=0,
                            )
                            eleventh_fee_currency = st.selectbox(
                                "Moeda da 11ª Taxa",
                                ["USD", "BRL"],
                                index=0,
                            )
                        if escolha_de_taxa >= 15:
                            twelfth_fee_currency = st.selectbox(
                                "Moeda da 12ª Taxa",
                                ["USD", "BRL"],
                                index=0,
                            )
                            thirtheenth_fee_currency = st.selectbox(
                                "Moeda da 13ª Taxa",
                                ["USD", "BRL"],
                                index=0,
                            )
                            fourteenth_fee_currency = st.selectbox(
                                "Moeda da 14ª Taxa",
                                ["USD", "BRL"],
                                index=0,
                            )
                            fifteenth_fee_currency = st.selectbox(
                                "Moeda da 15ª Taxa",
                                ["USD", "BRL"],
                                index=0,
                            )

        if st.form_submit_button("Enviar"):

            if house_bl == "":
                st.error("O House BL da Aba Dados do Importador deve ser informado!")
            elif (
                hbl_freight == ""
                or hbl_freight != st.session_state["house_bl"]
            ):
                st.error(
                    "O House BL da Aba Frete deve ser informado e ser igual ao House da Aba Dados do Importador!",
                )
            elif (
                hbl_container == ""
                or hbl_container != st.session_state["house_bl"]
            ):
                st.error(
                    "O House BL da Aba Container deve ser informadoe ser igual ao House da Aba Dados do Importador!",
                )
            elif (
                st.session_state.house_bl == ""
                or st.session_state.master_bl == ""
                or st.session_state.shipper == ""
                or st.session_state.consignee == ""
                or st.session_state.notify == ""
                or st.session_state.port_of_loading == ""
                or st.session_state.onboard_date is None
                or st.session_state.issue_date is None
                or st.session_state.vessel_origin == ""
                or st.session_state.vessel_voyage == ""
                or st.session_state.package_quantity == 0
                or st.session_state.package_type == ""
                or st.session_state.gross_weight == 0
                or st.session_state.cbm == 0
            ):
                st.error("Por favor, preencha todos os campos!")
            else:
                st.success(f"Dados enviados com sucesso.")

                if st.session_state.notify == "SEDA":
                    st.session_state.notify = "Samsung Electronics"
                elif st.session_state.notify == "SDS":
                    st.session_state.notify = "Samsung SDS"

                if st.session_state.consignee == "SEDA":
                    st.session_state.consignee = "Samsung Electronics"
                elif st.session_state.consignee == "SDS":
                    st.session_state.consignee = "Samsung SDS"

                json_data = {
                    "house_bl": st.session_state.house_bl,
                    "master_bl": st.session_state.master_bl,
                    "shipper": st.session_state.shipper,
                    "consignee": st.session_state.consignee,
                    "notify": st.session_state.notify,
                    "port_of_loading": st.session_state.port_of_loading,
                    "place_of_receipt": st.session_state.port_of_loading,
                    "port_of_discharge": st.session_state.port_of_discharge,
                    "vessel_origin": st.session_state.vessel_origin,
                    "vessel_voayge": st.session_state.vessel_voyage,
                    "package_quantity": st.session_state.package_quantity,
                    "package_type": st.session_state.package_type,
                    "gross_weight": st.session_state.gross_weight,
                    "cbm": st.session_state.cbm,
                    "ncm": st.session_state.ncm,
                    "un": st.session_state.un,
                    "freight": st.session_state.freight,
                    "freight_currency": st.session_state.freight_currency,
                    "terminal_handling": st.session_state.terminal_handling,
                    "terminal_handling_currency": st.session_state.terminal_handling_currency,
                    "documentation_fee": st.session_state.documentation_fee,
                    "documentation_fee_currency": st.session_state.documentation_fee_currency,
                    "fourth_fee": st.session_state.fourth_fee,
                    "fourth_fee_currency": st.session_state.fourth_fee_currency,
                    "fifth_fee": st.session_state.fifth_fee,
                    "fifth_fee_currency": st.session_state.fifth_fee_currency,
                    "sixth_fee": st.session_state.sixth_fee,
                    "sixth_fee_currency": st.session_state.sixth_fee_currency,
                    "seventh_fee": st.session_state.seventh_fee,
                    "seventh_fee_currency": st.session_state.seventh_fee_currency,
                    "eighth_fee": st.session_state.eighth_fee,
                    "eighth_fee_currency": st.session_state.eighth_fee_currency,
                    "ninth_fee": st.session_state.ninth_fee,
                    "ninth_fee_currency": st.session_state.ninth_fee_currency,
                    "tenth_fee": st.session_state.tenth_fee,
                    "tenth_fee_currency": st.session_state.tenth_fee_currency,
                    "eleventh_fee": st.session_state.eleventh_fee,
                    "eleventh_fee_currency": st.session_state.eleventh_fee_currency,
                    "twelfth_fee": st.session_state.twelfth_fee,
                    "twelfth_fee_currency": st.session_state.twelfth_fee_currency,
                    "thirteenth_fee": st.session_state.thirteenth_fee,
                    "thirteenth_fee_currency": st.session_state.thirteenth_fee_currency,
                    "fourteenth_fee": st.session_state.fourteenth_fee,
                    "fourteenth_fee_currency": st.session_state.fourteenth_fee_currency,
                    "fifteenth_fee": st.session_state.fifteenth_fee,
                    "fifteenth_fee_currency": st.session_state.fifteenth_fee_currency,
                }

                df_json = pd.DataFrame([json_data])

                df_json = df_json[
                    [
                        "house_bl",
                        "master_bl",
                        "shipper",
                        "port_of_loading",
                        "port_of_discharge",
                    ]
                ]

                st.write(df_json.to_html(index=False), unsafe_allow_html=True)
                time.sleep(4)
                st.rerun()

    # if submit_button:

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

# Controle da página baseada no estado do usuário
if st.session_state.user_id is None:
    if st.session_state.page == "home":
        # login_page()
        main_page()
    elif st.session_state.page == "register":
        register_page()

# Se o usuário estiver logado, mostrar a página principal
else:
    main_page()
