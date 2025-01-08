import streamlit as st

# Dicionário com credenciais de usuários (username: password)
user_credentials = {
    "user1": "password123",
    "user2": "mysecretpassword",
    "admin": "adminpass",
}


# Função de autenticação
def authenticate(username, password):
    if username in user_credentials and user_credentials[username] == password:
        return True
    else:
        return False


# Interface do Streamlit para login
st.title("Sistema de Autenticação")

if "user_id" not in st.session_state:
    st.session_state.user_id = None

if st.session_state.user_id is None:
    st.subheader("Por favor, faça o login")

    username = st.text_input("Nome de usuário")
    password = st.text_input("Senha", type="password")

    if st.button("Login"):
        if authenticate(username, password):
            st.session_state.user_id = username
            st.success(f"Bem-vindo, {username}!")
        else:
            st.error("Nome de usuário ou senha incorretos.")
else:
    st.success(f"Você está logado como: {st.session_state.user_id}")
    st.button("Sair", on_click=lambda: st.session_state.update({"user_id": None}))

# Aqui, você pode prosseguir com outras funcionalidades do app
if st.session_state.user_id:
    st.write("Funcionalidades do app acessíveis após o login.")
    # Adicione aqui as funcionalidades que dependem do login do usuário
