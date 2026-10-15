import os
import glob
import json
import pandas as pd
from datetime import datetime

# Mapeo de palabras clave/tags a la marca corporativa
BRAND_MAP = {
    "Carrefour": ["carrefour", "carrefourargentina", "ofertascarrefour"],
    "Coto": ["coto", "ofertascoto", "cotoyotenozco"],
    "Día": ["dia", "diaargentina", "supermercadosdia"],
    "Jumbo_Vea": ["jumbo", "jumboargentina", "vea", "veasupermercados"]
}

def detect_brand(tag_str):
    """Asigna la marca principal analizando el tag o término de búsqueda."""
    tag_clean = str(tag_str).lower().replace(" ", "").replace("#", "")
    for brand, keywords in BRAND_MAP.items():
        if any(kw in tag_clean for kw in keywords):
            return brand
    return "Otros"

def load_and_process_json_files():
    """Lee todos los JSONs raw_tiktok_*.json y los consolida en un DataFrame."""
    json_files = glob.glob("raw_tiktok_*.json")
    
    if not json_files:
        print("⚠️ No se encontraron archivos 'raw_tiktok_*.json' en la carpeta.")
        return None

    all_records = []

    for file_path in json_files:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                
                # Extraer el tag del nombre del archivo si no está adentro
                # Nombre típico: raw_tiktok_carrefourargentina_20261006.json
                file_tag = file_path.split("raw_tiktok_")[-1].split("_")[0]

                for item in data:
                    hashtag = item.get("hashtag", file_tag)
                    brand = item.get("brand", detect_brand(hashtag))
                    if brand == "Otros":
                        brand = detect_brand(file_tag)

                    all_records.append({
                        "video_id": str(item.get("video_id", "")),
                        "brand": brand,
                        "hashtag": hashtag,
                        "author": item.get("author", "desconocido"),
                        "url": item.get("url", ""),
                        "likes": int(item.get("likes", 0)),
                        "comments": int(item.get("comments", 0)),
                        "shares": int(item.get("shares", 0)),
                        "views": int(item.get("views", 0)),
                        "scraped_at": item.get("scraped_at", datetime.now().isoformat())
                    })
        except Exception as e:
            print(f"❌ Error leyendo el archivo {file_path}: {e}")

    df = pd.DataFrame(all_records)

    if df.empty:
        print("⚠️ Los archivos JSON leídos no contenían registros válidos.")
        return None

    # 1. Deduplicación por video_id (mantiene la captura con métricas más altas)
    df = df.sort_values(by=["likes", "comments", "views"], ascending=False)
    df = df.drop_duplicates(subset=["video_id"], keep="first")

    # 2. Métricas Calculadas
    df["total_engagement"] = df["likes"] + df["comments"] + df["shares"]
    
    # Ratio de viralidad (Engagement / Vistas si hay vistas > 0)
    df["virality_ratio_%"] = df.apply(
        lambda row: round((row["total_engagement"] / row["views"]) * 100, 2) if row["views"] > 0 else 0.0,
        axis=1
    )

    return df

def generate_market_insights(df):
    """Genera resumen ejecutivo consolidado por marca."""
    # Agrupación por Marca
    summary = df.groupby("brand").agg(
        total_videos=("video_id", "count"),
        total_likes=("likes", "sum"),
        total_comments=("comments", "sum"),
        total_shares=("shares", "sum"),
        total_views=("views", "sum"),
        total_engagement=("total_engagement", "sum")
    ).reset_index()

    # Calcular Share of Engagement (SOE)
    market_engagement = summary["total_engagement"].sum()
    if market_engagement > 0:
        summary["share_of_engagement_%"] = ((summary["total_engagement"] / market_engagement) * 100).round(2)
    else:
        summary["share_of_engagement_%"] = 0.0

    # Ordenar por Share of Engagement descendente
    summary = summary.sort_values(by="share_of_engagement_%", ascending=False)

    return summary

def main():
    print("🔄 [Retail Pulse] Procesando archivos JSON descargados...")
    df_videos = load_and_process_json_files()

    if df_videos is not None:
        # Guardar dataset procesado a nivel video
        today_str = datetime.now().strftime("%Y%m%d")
        csv_videos = f"processed_videos_{today_str}.csv"
        df_videos.to_csv(csv_videos, index=False, encoding="utf-8-sig")

        # Generar y guardar consolidado ejecutivo por marca
        summary_df = generate_market_insights(df_videos)
        csv_summary = f"summary_share_of_engagement_{today_str}.csv"
        summary_df.to_csv(csv_summary, index=False, encoding="utf-8-sig")

        print("\n📊 === RESUMEN EJECUTIVO: SHARE OF ENGAGEMENT ===")
        print(summary_df[["brand", "total_videos", "total_engagement", "share_of_engagement_%"]].to_string(index=False))
        print(f"\n✅ Archivo detallado guardado: {csv_videos}")
        print(f"✅ Archivo consolidado guardado: {csv_summary}")

if __name__ == "__main__":
    main()