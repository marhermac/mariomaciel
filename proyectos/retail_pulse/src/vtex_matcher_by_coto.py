import time
import requests
import pandas as pd
from datetime import datetime

# Configuración de los dominios VTEX en Argentina
RETAILERS = {
    "Carrefour": "www.carrefour.com.ar",
    "Día": "www.diaonline.supermercadosdia.com.ar",
    "Jumbo": "www.jumbo.com.ar"
}

def fetch_vtex_by_ean(retailer_name, domain, ean):
    """
    Consulta la API VTEX usando el parámetro correcto (alternateIds_Ean).
    """
    clean_ean = str(ean).strip()
    if not clean_ean or clean_ean == "SIN_EAN" or len(clean_ean) < 8:
        return None

    # Endpoint oficial con el filtro exacto de EAN en VTEX
    url = f"https://{domain}/api/catalog_system/pub/products/search?fq=alternateIds_Ean:{clean_ean}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept": "application/json",
        "REST-Range": "resources=0-2"
    }

    try:
        res = requests.get(url, headers=headers, timeout=8)
        if res.status_code in [200, 206]:
            products = res.json()
            if isinstance(products, list) and len(products) > 0:
                prod = products[0]
                brand = prod.get("brand", "")
                items = prod.get("items", [])
                
                if items:
                    item = items[0]
                    found_ean = item.get("ean", clean_ean)
                    found_name = prod.get("productName", "")
                    sellers = item.get("sellers", [])
                    
                    if sellers:
                        offer = sellers[0].get("commertialOffer", {})
                        list_price = offer.get("ListPrice", 0.0)
                        price = offer.get("Price", 0.0)
                        
                        if price > 0:
                            return {
                                "retailer": retailer_name,
                                "ean": str(found_ean),
                                "product_name": found_name,
                                "brand": brand,
                                "list_price": list_price,
                                "price": price,
                                "discount_%": round(((list_price - price) / list_price) * 100, 2) if list_price > price else 0.0,
                                "available": offer.get("IsAvailable", False)
                            }
    except Exception:
        pass

    return None

def main():
    # 📌 Asegurate de que coincida con tu archivo CSV actual de Coto
    coto_csv_filename = "coto_categoria_golosinas_20261012.csv" 
    
    print(f"🔄 [Retail Pulse] Cargando base de Coto desde: {coto_csv_filename}...\n")
    
    try:
        df_coto = pd.read_csv(coto_csv_filename)
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo '{coto_csv_filename}'.")
        return

    all_comparison_data = []

    # 1. Cargar los productos de Coto base al set de datos
    for _, row in df_coto.iterrows():
        price_val = float(row.get("price", 0))
        if price_val > 0:
            all_comparison_data.append({
                "retailer": "Coto",
                "ean": str(row.get("ean", "SIN_EAN")),
                "product_name": row.get("product_name", ""),
                "brand": row.get("brand", "Coto"),
                "list_price": float(row.get("list_price", price_val)),
                "price": price_val,
                "discount_%": 0.0,
                "available": row.get("available", True)
            })

    total_coto = len(df_coto)
    print(f"📦 Total de productos cargados de Coto: {total_coto}")
    print(f"🔍 Consultando Carrefour, Día y Jumbo por EAN exacto...\n")

    matches_found = 0
    valid_eans_count = 0

    # 2. Recorrer la lista y buscar en los 3 supermercados VTEX
    for idx, row in df_coto.iterrows():
        ean = str(row.get("ean", "SIN_EAN")).strip()
        p_name = str(row.get("product_name", ""))
        
        if ean == "SIN_EAN" or len(ean) < 8:
            continue
            
        valid_eans_count += 1
        print(f"[{idx+1}/{total_coto}] Buscando EAN: {ean} ({p_name[:30]}...)")
        
        for retailer_name, domain in RETAILERS.items():
            matched_item = fetch_vtex_by_ean(retailer_name, domain, ean)
            if matched_item:
                all_comparison_data.append(matched_item)
                matches_found += 1
                print(f"   🟢 Encontrado en {retailer_name}: ${matched_item['price']} ({matched_item['product_name'][:30]})")
            
        time.sleep(0.3)

    # 3. Guardar la matriz final consolidada
    if all_comparison_data:
        df_final = pd.DataFrame(all_comparison_data)
        today_str = datetime.now().strftime("%Y%m%d")
        output_filename = f"retail_pulse_comparison_matrix_{today_str}.csv"
        df_final.to_csv(output_filename, index=False, encoding="utf-8-sig")
        
        print(f"\n📊 === RESUMEN MATRIZ COMPARATIVA EXITOSA ===")
        print(f"• EANs válidos procesados: {valid_eans_count}")
        print(f"• Coincidencias exactas encontradas en VTEX: {matches_found}")
        print(f"• Archivo maestro guardado: {output_filename}")
    else:
        print("\n⚠️ No se pudieron generar datos.")

if __name__ == "__main__":
    main()