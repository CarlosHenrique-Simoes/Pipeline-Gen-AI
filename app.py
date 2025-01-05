from datetime import datetime, time

import numpy as np
import pandas as pd
import streamlit as st
from pydantic import ValidationError

from contrato import Vendas


def main():

    st.title("Sistema de CRM e Vendas ZapFlow")
    email = st.text_input("Email do Vendedor:")
    data = st.date_input("Data da Compra:", datetime.now())
    hora = st.time_input("Hora da Compra:", value=time(9, 0))
    valor = st.number_input("Valor da Venda:", min_value=0.0, format="%.2f")
    quantidade = st.number_input(
        "Quantidade de Produtos:",
        min_value=1,
        step=1)
    produto = st.selectbox("Produto:", options=[
        "ZapFlow com Gemini", "ZapFlow com ChatGPT", "ZapFlow com Llama 3.0"])

    if st.button("Salvar"):
        try:
            data_hora = datetime.combine(data, hora)
            venda = Vendas(
                email=email,
                data=data_hora,
                valor=valor,
                quantidade=quantidade,
                produto=produto,
            )

            st.write(venda)
        except ValidationError as e:
            st.error(f"Deu erro: {e}")


if __name__ == "__main__":
    main()
