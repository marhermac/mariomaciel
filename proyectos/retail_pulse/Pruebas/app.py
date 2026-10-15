import os
import glob
import pandas as pd
import streamlit as st
import plotly.express as px

# Configuración de la página
st.set_page_config(
    page_title="Retail Pulse - TikTok Intelligence",
    page_icon="📊",
    layout="wide"
)

# Título Principal
st.title("📊 Retail Pulse: Share of Engagement (TikTok Argentina)")
st.markdown("Monitoreo competitivo en tiempo real de las principales cadenas de supermercados en TikTok.")

@st.cache_data
def load_latest_data():
    """Busca y carga los CSVs más recientes generados por analyzer.py"""
    video_files = glob.glob("processed_videos_*.csv")
    summary_files = glob.glob("summary_share_of_engagement_*.csv")
    
    if not video_files or not summary_files:
        return None, None
        
    latest_videos = max(video_files, key=os.path.getmtime)
    latest_summary = max(summary_files, key=os.path.getmtime)
    
    df_videos = pd.read_csv(latest_videos)
    df_summary = pd.read_csv(latest_summary)
    
    return df_videos, df_summary

df_videos, df_summary = load_latest_data()

if df_videos is None or df_summary is None:
    st.warning("⚠️ No se encontraron datos procesados. Ejecutá primero `python analyzer.py` en tu terminal.")
else:
    # --- FILTROS LATERALES ---
    st.sidebar.header("🔍 Filtros del Dashboard")
    selected_brands = st.sidebar.multiselect(
        "Seleccioná Marcas:",
        options=df_summary["brand"].unique(),
        default=df_summary["brand"].unique()
    )

    # Filtrar data
    filtered_summary = df_summary[df_summary["brand"].isin(selected_brands)]
    filtered_videos = df_videos[df_videos["brand"].isin(selected_brands)]

    # --- MÉTRICAS SUPERIORES (KPIs) ---
    st.markdown("---")
    col1, col2, col3, col4 = st.columns(4)

    total_market_engagement = filtered_summary["total_engagement"].sum()
    total_market_videos = filtered_summary["total_videos"].sum()
    total_market_likes = filtered_summary["total_likes"].sum()
    total_market_comments = filtered_summary["total_comments"].sum()

    col1.metric("Engagement Total del Sector", f"{total_market_engagement:,.0f}")
    col2.metric("Videos Analizados", f"{total_market_videos:,}")
    col3.metric("Total de Likes", f"{total_market_likes:,.0f}")
    col4.metric("Total de Comentarios", f"{total_market_comments:,.0f}")
    st.markdown("---")

    # --- SECCIÓN DE GRÁFICOS ---
    col_chart1, col_chart2 = st.columns(2)

    with col_chart1:
        st.subheader("🥧 Share of Engagement (%)")
        fig_pie = px.pie(
            filtered_summary,
            names="brand",
            values="share_of_engagement_%",
            hole=0.4,
            color="brand",
            color_discrete_map={
                "Carrefour": "#00539F",
                "Coto": "#E31B23",
                "Día": "#FFCC00",
                "Jumbo_Vea": "#008751"
            }
        )
        fig_pie.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig_pie, use_container_width=True)

    with col_chart2:
        st.subheader("📊 Volumen Total de Engagement por Marca")
        fig_bar = px.bar(
            filtered_summary,
            x="brand",
            y="total_engagement",
            text="total_engagement",
            color="brand",
            color_discrete_map={
                "Carrefour": "#00539F",
                "Coto": "#E31B23",
                "Día": "#FFCC00",
                "Jumbo_Vea": "#008751"
            }
        )
        fig_bar.update_traces(texttemplate='%{text:,.0f}', textposition='outside')
        fig_bar.update_layout(showlegend=False, xaxis_title="Marca", yaxis_title="Engagement (Likes + Comentarios + Shares)")
        st.plotly_chart(fig_bar, use_container_width=True)

    # --- TABLA DE RANKING DE VIDEOS VIRALES ---
    st.markdown("### 🏆 Top Videos con Mayor Engagement del Sector")
    
    # Selector de métrica de orden
    sort_metric = st.selectbox("Ordenar ranking por:", ["total_engagement", "likes", "comments", "shares", "virality_ratio_%"])
    
    top_videos = filtered_videos.sort_values(by=sort_metric, ascending=False).head(15)

    st.dataframe(
        top_videos[["brand", "hashtag", "author", "likes", "comments", "shares", "total_engagement", "virality_ratio_%", "url"]],
        use_container_width=True,
        hide_index=True
    )