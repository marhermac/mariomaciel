import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

from app.config import DB_FILE

from app.gestor_db import (
    obtener_clientes,
    agregar_cliente,
    eliminar_cliente,
    importar_clientes_csv
)

from app.investigacion.gestor_investigacion import (
    crear_investigacion,
    guardar_wms,
    guardar_tms,
    obtener_wms,
    obtener_tms,
    guardar_entrevista,
    obtener_entrevistas
)


# =====================================
# CONFIGURACION PAGINA
# =====================================

st.set_page_config(
    page_title="Radar Reclamos Logísticos",
    layout="wide"
)

# =====================================
# CARGA DATOS SQLITE
# =====================================



conexion = sqlite3.connect(
    DB_FILE
)

df = pd.read_sql_query(
    """
    SELECT *
    FROM reclamos
    """,
    conexion
)

conexion.close()

# =====================================
# MENU
# =====================================

pagina = st.sidebar.radio(
    "Menú",
    [
        "Dashboard",
        "Reclamos",
        "Clientes",
        "Administración",
        "Investigación"
    ]
)

# =====================================
# PAGINA CLIENTES
# =====================================

if pagina == "Clientes":

    st.title("👥 Clientes")

    clientes = obtener_clientes()

    clientes_df = pd.DataFrame(
        clientes,
        columns=[
            "ID",
            "Cliente",
            "Email"
        ]
    )

    st.dataframe(
        clientes_df,
        use_container_width=True
    )

    st.subheader(
        "Agregar Cliente"
    )

    nuevo_cliente = st.text_input(
        "Nombre Cliente"
    )

    nuevo_email = st.text_input(
        "Email"
    )

    if st.button(
        "Guardar Cliente"
    ):

        agregar_cliente(
            nuevo_cliente,
            nuevo_email
        )

        st.success(
            "Cliente agregado correctamente"
        )

        st.rerun()

    st.stop()

# =====================================
# PAGINA RECLAMOS
# =====================================

if pagina == "Reclamos":

    st.title(
        "📧 Reclamos"
    )

    if not df.empty:

        st.dataframe(
            df.sort_values(
                by="fecha_registro",
                ascending=False
            ),
            use_container_width=True
        )

    else:

        st.warning(
            "No hay reclamos cargados."
        )

    st.stop()

# =====================================
# PAGINA ADMINISTRACION
# =====================================

if pagina == "Administración":

    st.header("⚙ Administración")

    st.subheader(
        "Importar Clientes CSV"
    )

    archivo = st.file_uploader(
        "Seleccionar archivo CSV",
        type="csv"
    )

    if archivo:

        clientes_importados = (
            importar_clientes_csv(
                archivo
            )
        )

        st.success(
            f"{clientes_importados} clientes importados."
        )

    st.divider()

    st.subheader(
        "Formato esperado"
    )



    st.code(
"""
cliente_logistica,email
Quefrio,mario.maciel5@gmail.com
Arrocera Villaguay,mhm639@hotmail.com
Clavelina Plantas,claudia.clavelina@gmail.com
Tech,mario.maciel.tech@outlook.es
"""
    )

    st.stop()

# =====================================
# PAGINA INVESTIGACION
# =====================================

if pagina == "Investigación":

    st.title(
        "🔎 Investigación de Reclamos"
    )
          
    # ==========================
    # CLIENTE MAS CRITICO
    # ==========================

    cliente_critico = (
        df["cliente_logistica"]
        .value_counts()
        .idxmax()
    )

    cantidad_cliente = (
        df["cliente_logistica"]
        .value_counts()
        .max()
    )

    st.error(
        f"Cliente más crítico: {cliente_critico} ({cantidad_cliente} reclamos)"
    )

    # ==========================
    # CATEGORIA MAS CRITICA
    # ==========================

    categoria_critica = (
        df["categoria"]
        .value_counts()
        .idxmax()
    )

    cantidad_categoria = (
        df["categoria"]
        .value_counts()
        .max()
    )

    st.warning(
        f"Categoría más crítica: {categoria_critica} ({cantidad_categoria} reclamos)"
    )

    # ==========================
    # PEDIDOS DEL CLIENTE CRITICO
    # ==========================

    st.subheader(
              "📦 Reclamos del Cliente Crítico"
       )

    pedidos_cliente = df[
         df["cliente_logistica"]
          == cliente_critico
    ][
    [
        "id",
        "pedido",
        "cliente_logistica",
        "categoria"
    ]
    ]

    st.dataframe(
       pedidos_cliente,
       use_container_width=True
    )

    pedido_seleccionado = st.selectbox(
         "Seleccionar pedido para investigar",
         pedidos_cliente["pedido"].tolist()
        )

   

    reclamo_id = pedidos_cliente[
        pedidos_cliente["pedido"]
        == pedido_seleccionado
    ]["id"].iloc[0]

    if st.button(
    "🚀 Iniciar Investigación"
    ):

        investigacion_id = crear_investigacion(
            reclamo_id=reclamo_id,
            responsable="Mario"
        )

        st.session_state[
            "investigacion_id"
        ] = investigacion_id

        st.success(
            f"Investigación #{investigacion_id} creada correctamente."
        )

        investigacion_id = st.session_state.get(
            "investigacion_id"
        )
    investigacion_id = st.session_state.get(
        "investigacion_id"
    )

    st.subheader(
        "📋 Estado de la Investigación"
        )

    if investigacion_id:

        st.success(
            "☑ Investigación iniciada"
        )

    else:

        st.warning(
            "☐ Investigación no iniciada"
        )
    if df.empty:

        st.warning(
            "No existen reclamos para analizar."
        )

        st.stop()

    st.divider()

    st.subheader(
            "🏭 Paso 1 - Warehouse"
        )

    turno = st.text_input(
            "Turno"
        )

    operador = st.text_input(
            "Operador"
        )

    supervisor = st.text_input(
            "Supervisor"
        )

    pedido_preparado = st.radio(
        "Pedido preparado",
        ["Sí", "No"],
        horizontal=True
    )

    pedido_completo = st.radio(
        "Pedido completo",
        ["Sí", "No"],
        horizontal=True
    )

    stock_correcto = st.radio(
        "Stock correcto",
        ["Sí", "No"],
        horizontal=True
    )

    embalaje_correcto = st.radio(
        "Embalaje correcto",
        ["Sí", "No"],
        horizontal=True
    )
        
    observaciones = st.text_area(
            "Observaciones"
        )

    st.divider()

    st.subheader(
        "🎤 Entrevistas Warehouse"
        )
        # =====================================
        # OPERADOR WMS
        # =====================================

    st.markdown(
            "### 👷 Operador WMS"
        )

    nombre_operador = st.text_input(
            "Nombre Operador"
        )

    comentario_operador = st.text_area(
            "¿Qué ocurrió durante la preparación?"
        )

    accion_operador = st.text_area(
            "Acciones realizadas"
        )

     
    if investigacion_id:

        wms = obtener_wms(
            investigacion_id
        )

    else:

        st.info(
            "☐ Warehouse pendiente"
        )




    if st.button(
        "💾 Guardar WMS"
    ):

        investigacion_id = st.session_state.get(
            "investigacion_id"
        )

        if investigacion_id is None:

            st.error(
                "Primero debe iniciar una investigación."
            )

        else:

            guardar_wms(
                investigacion_id,
                1 if pedido_preparado == "Sí" else 0,
                1 if pedido_completo == "Sí" else 0,
                1 if stock_correcto == "Sí" else 0,
                1 if embalaje_correcto == "Sí" else 0,
                0,  # sin_incidencias se calculará automáticamente
                turno,
                operador,
                supervisor,
                observaciones
            )

            st.success(
                "☑ Paso 1 WMS completado"
            )

           
            st.info(
                    "Continuar análisis en Tráfico."
                )


    st.info(
        "➡ Próximo paso: Investigación TMS"
    )

    st.subheader(
        "🚚 Paso 2 - Tráfico"
    )

    viaje = st.text_input(
        "Número de viaje"
    )

    transportista = st.text_input(
        "Transportista"
    )

    ruta = st.text_input(
        "Ruta"
    )

    salida_horario = st.radio(
        "Salida en horario",
        ["Sí", "No"],
        horizontal=True
    )

    sin_reprogramacion = st.radio(
        "Sin reprogramación",
        ["Sí", "No"],
        horizontal=True
    )

    sin_rechazo = st.radio(
        "Sin rechazo",
        ["Sí", "No"],
        horizontal=True
    )

    entrega_fuera_ventana = st.radio(
        "Entrega fuera de ventana",
        ["Sí", "No"],
        horizontal=True
    )

    observaciones_tms = st.text_area(
        "Observaciones TMS"
    )

    st.subheader(
        "🎤 Entrevistas Trafico"
        )
    
    # =====================================
    # CHOFER
    # =====================================

    st.markdown(
        "### 🛻 Chofer"
    )

    nombre_chofer = st.text_input(
        "Nombre Chofer"
    )

    comentario_chofer = st.text_area(
        "Comentarios del chofer"
    )

    accion_chofer = st.text_area(
        "Acciones tomadas"
    )


    if st.button(
        "💾 Guardar Trafico"
    ):

        guardar_tms(
            investigacion_id,
            viaje,
            transportista,
            ruta,
            1 if salida_horario == "Sí" else 0,
            1 if sin_reprogramacion == "Sí" else 0,
            1 if sin_rechazo == "Sí" else 0,
            1 if entrega_fuera_ventana == "Sí" else 0,
            observaciones_tms           
        )

        st.success(
            "☑ Paso 2 Tráfico completado"
        )

    

    investigacion_id = st.session_state.get(
    "investigacion_id"
)

    if investigacion_id is None:

        st.warning(
            "Primero debe iniciar una investigación."
        )

    else:

        if st.button(
            "💾 Guardar Entrevistas"
        ):


            guardar_entrevista(
                investigacion_id,
                "OPERADOR_WMS",
                nombre_operador,
                comentario_operador,
                accion_operador
            )

            
            guardar_entrevista(
                investigacion_id,
                "CHOFER",
                nombre_chofer,
                comentario_chofer,
                accion_chofer
            )

            st.success(
                "☑ Paso 3 Entrevistas completado"
            )

    # ==========================
    # ANALISIS WMS
    # ==========================

    warehouse_ok = (
        pedido_preparado == "Sí"
        and pedido_completo == "Sí"
        and stock_correcto == "Sí"
        and embalaje_correcto == "Sí"
    )

    if not warehouse_ok:

        st.warning(
            "⚠ Se detectaron incidencias en Warehouse."
        )

        st.info(
            "La investigación puede resolverse en este sector."
        )

    else:

        st.success(
            "✓ Warehouse sin desvíos detectados."
        )

        st.info(
            "➡ Continuar investigación en Tráfico."
        )
        
        # ==========================
        # ANALISIS TMS
        # ==========================

        if salida_horario == "No":

            st.warning(
                "⚠ Posible desvío en transporte: salida fuera de horario"
            )

        else:

            st.success(
                "✓ Salida en horario"
        )

    # ==========================
    # CONCLUSION
    # ==========================

    if salida_horario == "No":

        st.error(
            "🎯 Conclusión preliminar: posible causa en Transporte"
        )

    elif not warehouse_ok:

        st.error(
            "🎯 Conclusión preliminar: posible causa en WMS"
        )

    else:

        st.success(
            "🎯 No se detectan desvíos evidentes"
        )

    st.info(
        "➡ Próximo paso: Hallazgos"
        )

    st.divider()

    st.subheader(
        "📌 Hallazgos del Investigador"
    )

    hallazgo_1 = st.text_input(
        "Problema Inicial"
    )

    hallazgo_2 = st.text_input(
        "Dato clave para el analisis"
    )

   
    if st.button(
        "💾 Guardar Hallazgos"
    ):

        st.success(
            "☑ Hallazgos registrados"
        )

    # =====================================
    # GENERADOR DE PROMPT 5 WHY
    # =====================================

    st.divider()

    st.subheader(
        "🤖 Generador de Prompt 5 Why"
    )

    if st.button(
        "🚀 Generar Prompt 5 Why"
    ):

        prompt_5why = f"""
        Utilicemos la metodología 5 Why para analizar el siguiente reclamo logístico.

        PROBLEMA INICIAL:
        {hallazgo_1}

        DATO CLAVE PARA EL ANÁLISIS:
        {hallazgo_2}

        Objetivos:

        1. Identificar la causa raíz utilizando la técnica 5 Why.

        2. Determinar si el origen del problema se encuentra en:
        - Warehouse
        - Transporte
        - Planificación
        - Cliente
        - Proceso

        3. Proponer acciones correctivas inmediatas.

        4. Proponer acciones preventivas para evitar recurrencia.

        5. Generar una conclusión final para el investigador.

        Desarrollar el análisis completo paso a paso.
        """

        st.text_area(
            "Prompt generado",
            value=prompt_5why,
            height=300
        )



        st.info(
            "➡ Próximo paso: Análisis 5 Why"
        )

        st.divider()

    st.subheader(
    "🤖 Análisis de Causa Raíz"
    )

    causa_raiz = st.text_area(
        "Causa Raíz"
    )

    origen_problema = st.selectbox(
        "Origen del Problema",
        [
            "Warehouse",
            "Transporte",
            "Planificación",
            "Cliente",
            "Proceso"
        ]
    )

    accion_correctiva = st.text_area(
        "Acción Correctiva"
    )

    accion_preventiva = st.text_area(
        "Acción Preventiva"
    )

    conclusion_final = st.text_area(
        "Conclusión Final"
)

    st.subheader(
    "🤖 Análisis de Causa Raíz"
    )

    with st.expander(
        "🔍 Ver análisis completo"
        ):
            st.subheader(
                "🔍 Análisis 5 Why"
            )

            problema = st.text_input(
                "Problema a analizar"
            )

            why1 = st.text_input(
                "Why 1"
            )

            why2 = st.text_input(
                "Why 2"
            )

            why3 = st.text_input(
                "Why 3"
            )

            why4 = st.text_input(
                "Why 4"
            )

            why5 = st.text_input(
                "Why 5"
            )

            causa_raiz = st.text_area(
                "🎯 Causa raíz identificada"
            )

    if st.button(
    "💾 Guardar Análisis"
    ):

        guardar_analisis_causa_raiz(
            investigacion_id,
            causa_raiz,
            origen_problema,
            accion_correctiva,
            accion_preventiva,
            conclusion_final,
            problema_analizar,
            "", "", "", "", ""
        )

    st.success(
        "☑ Análisis guardado correctamente"
    )


    st.subheader(
        "✅ Cierre de Investigación"
    )

    estado_final = st.selectbox(
        "Resultado",
        [
            "Resuelto",
            "Resuelto con Acción Preventiva",
            "Pendiente",
            "Escalar a Gerencia"
        ]
    )

    responsable_accion = st.text_input(
        "Responsable de la acción"
    )

    fecha_compromiso = st.date_input(
        "Fecha compromiso"
    )
    
    if st.button(
    "✅ Cerrar Investigación"
    ):

        st.success(
        "Investigación finalizada."
     )

    # ==========================
    # GUIA DE INVESTIGACION
    # ==========================

    st.subheader(
        "🧭 Guía de Investigación"
    )

    st.markdown(
        f"""
        ### Paso 1
        Identificar los pedidos afectados por **{categoria_critica}**

        ### Paso 2
        Buscar esos pedidos en el WMS

        ### Paso 3
        Identificar el viaje correspondiente en el TMS

        ### Paso 4
        Verificar si otros pedidos del mismo viaje tuvieron reclamos

        ### Paso 5
        Buscar patrones comunes

        - mismo transportista
        - misma ruta
        - mismo depósito
        - mismo turno
        - mismo operador

        ### Paso 6
        Documentar hallazgos

        ### Paso 7
        Iniciar análisis de causa raíz (5 Why)
        """
        )

    st.stop()

   
 
# =====================================
# DASHBOARD
# =====================================

st.title(
    "📦 Radar Reclamos Logísticos"
)

if df.empty:

    st.warning(
        "No existen reclamos cargados."
    )

    st.stop()


st.divider()

# =====================================
# FECHAS
# =====================================

df["fecha_registro"] = pd.to_datetime(
    df["fecha_registro"]
)

# =====================================
# FILTROS
# =====================================

st.sidebar.header(
    "Filtros"
)

cliente = st.sidebar.selectbox(
    "Cliente",
    ["Todos"]
    + sorted(
        df["cliente_logistica"]
        .unique()
        .tolist()
    )
)

categoria = st.sidebar.selectbox(
    "Categoría",
    ["Todas"]
    + sorted(
        df["categoria"]
        .unique()
        .tolist()
    )
)



df_filtrado = df.copy()



if cliente != "Todos":

    df_filtrado = df_filtrado[
        df_filtrado[
            "cliente_logistica"
        ] == cliente
    ]

if categoria != "Todas":

    df_filtrado = df_filtrado[
        df_filtrado[
            "categoria"
        ] == categoria
    ]

ranking_clientes = (
    df_filtrado
    .groupby("cliente_logistica")
    .size()
    .reset_index(name="Reclamos")
)

ranking_clientes.columns = [
    "Cliente",
    "Reclamos"
]

ranking_clientes = (
    ranking_clientes
    .sort_values(
        by="Reclamos",
        ascending=False
    )
)

# =====================================
# Alerta CLIENTES
# =====================================

st.subheader(
    "🚦Alerta Operativa"
)

for _, fila in ranking_clientes.iterrows():

    cliente_actual = fila["Cliente"]
    reclamos = fila["Reclamos"]

    if reclamos >= 5:

        st.error(
            f"🔴 {cliente_actual}: {reclamos} reclamos"
        )

    elif reclamos >= 3:

        st.warning(
            f"🟡 {cliente_actual}: {reclamos} reclamos"
        )

    else:

        st.success(
            f"🟢 {cliente_actual}: {reclamos} reclamos"
        )


# =====================================
# KPIS
# =====================================

total_reclamos = len(
    df_filtrado
)

total_clientes = (
    df_filtrado[
        "cliente_logistica"
    ].nunique()
)

faltantes = len(
    df_filtrado[
        df_filtrado[
            "categoria"
        ] == "FALTANTE"
    ]
)

roturas = len(
    df_filtrado[
        df_filtrado[
            "categoria"
        ] == "ROTURA"
    ]
)

demoras = len(
    df_filtrado[
        df_filtrado[
            "categoria"
        ] == "DEMORA"
    ]
)

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "Reclamos",
    total_reclamos
)

col2.metric(
    "Clientes",
    total_clientes
)

col3.metric(
    "Faltantes",
    faltantes
)

col4.metric(
    "Roturas",
    roturas
)

col5.metric(
    "Demoras",
    demoras
)

st.divider()

# =====================================
# RANKING CLIENTES
# =====================================

st.subheader(
    "🏆 Ranking de Clientes"
)

ranking_clientes = (
    df_filtrado["cliente_logistica"]
    .value_counts()
    .reset_index()
)

ranking_clientes.columns = [
    "Cliente",
    "Reclamos"
]

st.dataframe(
    ranking_clientes,
    use_container_width=True
)



# =====================================
# PARETO
# =====================================

st.subheader(
    "📊 Pareto de Reclamos"
)

pareto_df = ranking_clientes.copy()

pareto_df["Acumulado"] = (
    pareto_df["Reclamos"]
    .cumsum()
)

total = pareto_df["Reclamos"].sum()

pareto_df["% Acumulado"] = (
    pareto_df["Acumulado"]
    / total
    * 100
)

st.dataframe(
    pareto_df,
    use_container_width=True
)




# =====================================
# GRAFICO CATEGORIAS
# =====================================

cat_df = (
    df_filtrado["categoria"]
    .value_counts()
    .reset_index()
)

cat_df.columns = [
    "categoria",
    "cantidad"
]

fig_cat = px.bar(
    cat_df,
    x="categoria",
    y="cantidad",
    title="Reclamos por Categoría"
)

st.plotly_chart(
    fig_cat,
    use_container_width=True
)

# =====================================
# GRAFICO CLIENTES
# =====================================

cli_df = (
    df_filtrado[
        "cliente_logistica"
    ]
    .value_counts()
    .reset_index()
)

cli_df.columns = [
    "cliente",
    "cantidad"
]

fig_cli = px.bar(
    cli_df,
    x="cliente",
    y="cantidad",
    title="Reclamos por Cliente"
)

st.plotly_chart(
    fig_cli,
    use_container_width=True
)

# =====================================
# ULTIMOS RECLAMOS
# =====================================

st.subheader(
    "📋 Últimos Reclamos"
)

st.dataframe(
    df_filtrado.sort_values(
        by="fecha_registro",
        ascending=False
    ),
    use_container_width=True
)