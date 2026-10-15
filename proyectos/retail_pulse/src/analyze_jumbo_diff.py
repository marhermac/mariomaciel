import pandas as pd
from datetime import datetime

def analyze_jumbo_highest_prices(csv_filename):
    print(f"📊 [Retail Pulse Analyzer - Jumbo] Leyendo matriz desde: {csv_filename}...\n")
    
    try:
        df = pd.read_csv("retail_pulse_comparison_matrix_20261013.csv")
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo '{csv_filename}'.")
        return

    # Limpiar precios y EAN
    df_valid = df[df["price"] > 0].copy()
    df_valid["ean"] = df_valid["ean"].astype(str).str.strip()

    # 1. Conservar un nombre de producto representativo por EAN
    product_names = df_valid.groupby("ean")["product_name"].first().to_dict()

    # 2. Pivotear únicamente por EAN
    pivot_df = df_valid.pivot_table(
        index="ean", 
        columns="retailer", 
        values="price", 
        aggfunc="min"
    ).reset_index()

    # Reasignar el nombre del producto
    pivot_df["product_name"] = pivot_df["ean"].map(product_names)

    if "Jumbo" not in pivot_df.columns:
        print("⚠️ No se encontraron registros de Jumbo en el archivo.")
        return

    # Competidores de Jumbo presentes en el CSV
    competitor_cols = [col for col in pivot_df.columns if col not in ["ean", "product_name", "Jumbo"]]

    print(f"🔍 Competidores detectados para comparar contra Jumbo: {', '.join(competitor_cols)}")

    # Filtrar productos que estén en Jumbo Y en al menos un competidor
    pivot_df = pivot_df.dropna(subset=["Jumbo"])
    pivot_df["max_competitor_price"] = pivot_df[competitor_cols].max(axis=1)
    
    pivot_df = pivot_df.dropna(subset=["max_competitor_price"])

    # Calcular diferencia en pesos y porcentaje respecto al competidor más alto
    pivot_df["diff_abs"] = pivot_df["Jumbo"] - pivot_df["max_competitor_price"]
    pivot_df["diff_pct"] = (pivot_df["diff_abs"] / pivot_df["max_competitor_price"]) * 100

    # Filtrar solo donde Jumbo es MÁS CARO
    jumbo_expensive = pivot_df[pivot_df["diff_abs"] > 0].copy()

    if jumbo_expensive.empty:
        print("\n✅ ¡Buenas noticias para Jumbo! No se encontraron productos donde sea más caro que la competencia.")
        return

    jumbo_expensive = jumbo_expensive.sort_values(by="diff_pct", ascending=False)

    print(f"\n🚨 === RANKING: EANs CON MAYOR PRECIO EN JUMBO ({len(jumbo_expensive)} ítems) ===")
    
    display_cols = ["ean", "product_name", "Jumbo"] + competitor_cols + ["diff_abs", "diff_pct"]
    
    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", 1000)
    
    print(jumbo_expensive[display_cols].to_string(index=False))

    today_str = datetime.now().strftime("%Y%m%d")
    output_report = f"jumbo_reporte_precios_altos_{today_str}.csv"
    jumbo_expensive[display_cols].to_csv(output_report, index=False, encoding="utf-8-sig")
    
    print(f"\n📁 Reporte de sobreprecios exportado exitosamente: {output_report}")

if __name__ == "__main__":
    csv_file_path = "retail_pulse_comparison_matrix_20261013.csv"
    analyze_jumbo_highest_prices(csv_file_path)