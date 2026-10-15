import pandas as pd
from datetime import datetime

def analyze_coto_highest_prices(csv_filename):
    print(f"📊 [Retail Pulse Analyzer - Coto] Leyendo matriz desde: {csv_filename}...\n")

    try:
        df = pd.read_csv("retail_pulse_comparison_matrix_20261013.csv")
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo '{csv_filename}'.")
        return

    # Limpiar precios y EAN
    df_valid = df[df["price"] > 0].copy()
    df_valid["ean"] = df_valid["ean"].astype(str).str.strip()

    # Conservar un nombre de producto representativo por EAN
    product_names = df_valid.groupby("ean")["product_name"].first().to_dict()

    # Pivotear únicamente por EAN
    pivot_df = df_valid.pivot_table(
        index="ean", 
        columns="retailer", 
        values="price", 
        aggfunc="min"
    ).reset_index()

    # Reasignar el nombre del producto
    pivot_df["product_name"] = pivot_df["ean"].map(product_names)

    if "Coto" not in pivot_df.columns:
        print("⚠️ No se encontraron registros de Coto en el archivo.")
        return

    # Competidores de Coto presentes
    competitor_cols = [col for col in pivot_df.columns if col not in ["ean", "product_name", "Coto"]]

    print(f"🔍 Competidores detectados para comparar contra Coto: {', '.join(competitor_cols)}")

    # Filtrar productos que estén en Coto Y en al menos un competidor
    pivot_df = pivot_df.dropna(subset=["Coto"])
    pivot_df["max_competitor_price"] = pivot_df[competitor_cols].max(axis=1)
    pivot_df = pivot_df.dropna(subset=["max_competitor_price"])

    # Calcular diferencia en pesos y porcentaje respecto al competidor más alto
    pivot_df["diff_abs"] = pivot_df["Coto"] - pivot_df["max_competitor_price"]
    pivot_df["diff_pct"] = (pivot_df["diff_abs"] / pivot_df["max_competitor_price"]) * 100

    # Filtrar solo donde Coto es MÁS CARO
    coto_expensive = pivot_df[pivot_df["diff_abs"] > 0].copy()

    if coto_expensive.empty:
        print("\n✅ ¡Buenas noticias para Coto! No se encontraron productos donde sea más caro que la competencia.")
        return

    coto_expensive = coto_expensive.sort_values(by="diff_pct", ascending=False)

    print(f"\n🚨 === RANKING: EANs CON MAYOR PRECIO EN COTO ({len(coto_expensive)} ítems) ===")

    display_cols = ["ean", "product_name", "Coto"] + competitor_cols + ["diff_abs", "diff_pct"]

    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", 1000)

    print(coto_expensive[display_cols].to_string(index=False))

    today_str = datetime.now().strftime("%Y%m%d")
    output_report = f"coto_reporte_precios_altos_{today_str}.csv"
    coto_expensive[display_cols].to_csv(output_report, index=False, encoding="utf-8-sig")

    print(f"\n📁 Reporte de sobreprecios exportado exitosamente: {output_report}")

if __name__ == "__main__":
    # 📌 Asegurate de que este sea el nombre exacto de tu matriz consolidada
    csv_file_path = "retail_pulse_comparison_matrix_20261013.csv"
    analyze_coto_highest_prices(csv_file_path)