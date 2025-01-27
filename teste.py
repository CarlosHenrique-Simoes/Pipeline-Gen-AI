



with tab1:
    col1, col2, col3 = st.columns(3)

    with col1:
        # Campo de texto
        house_bl = st.text_input(
            "House BL",
        ).upper()
        notify = st.selectbox(
            "Notify",
            ["SEDA", "SDS"],
        ).upper()
        port_of_loading = st.text_input(
            "Porto de Origem",
            max_chars=5,
        )
        viagem = st.text_input(
            "Número da Viagem",
            value=st.session_state.get("viagem", ""),
        )
        gross_weight = st.number_input(
            "Informe o Peso Bruto",
            min_value=0.0,
            format="%.3f",
        )
        onboard_date = st.date_input(
            "Onboard date",
        )

    with col2:
        master_bl = st.text_input(
            "Master BL",
        ).upper()
        consignee = st.selectbox(
            "Consignee",
            ["SEDA", "SDS"],
        ).upper()
        port_of_discharge = st.text_input(
            "Porto de Destino",
            max_chars=5,
        )
        quantidade_de_embalagem = st.number_input(
            "Quantidade de Embalagem",
            min_value=0.0,
            format="%.1f",
        )
        cubagem = st.number_input(
            "Informe a Cubagem do House",
            min_value=0.0,
            format="%.3f",
        )
        issue_date = st.date_input("Issue date", key="issue_date")

    with col3:
        shipper = st.text_area(
            label="Shipper",
            height=123,
        ).upper()
        vessel_origin = st.text_input(
            "Navio de Origem",
        )
        tipo_de_embalagem = st.text_input(
            "Tipo de Embalagem",
            max_chars=3,
        ).upper()
        freight = st.number_input(
            "Informe o Frete",
            min_value=0.0,
            format="%.2f",
        )