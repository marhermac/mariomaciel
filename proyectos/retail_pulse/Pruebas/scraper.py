import os
import time
import json
from datetime import datetime
from playwright.sync_api import sync_playwright

HASHTAGS = {
    "Carrefour": ["carrefourargentina", "ofertascarrefour"],
    "Coto": ["coto", "ofertascoto"],
    "Día": ["diaargentina", "supermercadosdia"],
    "Jumbo_Vea": ["jumboargentina", "veasupermercados"]
}

def parse_number(text: str) -> int:
    if not text:
        return 0
    text = str(text).upper().strip().replace(',', '.')
    try:
        if 'K' in text:
            return int(float(text.replace('K', '')) * 1_000)
        if 'M' in text:
            return int(float(text.replace('M', '')) * 1_000_000)
        return int(float(text))
    except ValueError:
        return 0

def fetch_details_from_video(page, video_url):
    metrics = {"likes": 0, "comments": 0}
    try:
        page.goto(video_url, wait_until="domcontentloaded", timeout=15000)
        time.sleep(2)

        page.keyboard.press("Escape")

        like_selectors = [
            'strong[data-e2e="like-count"]',
            'span[data-e2e="like-count"]',
            'button[data-e2e="like-icon"] + strong'
        ]
        for sel in like_selectors:
            try:
                elem = page.query_selector(sel)
                if elem:
                    txt = elem.inner_text().strip()
                    val = parse_number(txt)
                    if val > 0 or metrics["likes"] == 0:
                        metrics["likes"] = val
                        if val > 0:
                            break
            except Exception:
                continue

        comment_selectors = [
            'strong[data-e2e="comment-count"]',
            'span[data-e2e="comment-count"]',
            'button[data-e2e="comment-icon"] + strong'
        ]
        for sel in comment_selectors:
            try:
                elem = page.query_selector(sel)
                if elem:
                    txt = elem.inner_text().strip()
                    val = parse_number(txt)
                    if val > 0 or metrics["comments"] == 0:
                        metrics["comments"] = val
                        if val > 0:
                            break
            except Exception:
                continue

    except Exception as e:
        print(f"      ⚠️ Error leyendo {video_url}: {e}")
    
    return metrics

def run_scraper():
    print(f"[{datetime.now().strftime('%H:%M:%S')}] 🚀 Iniciando Google Chrome real con Playwright...")
    
    user_data_dir = os.path.join(os.getcwd(), "playwright_session")
    raw_results = []

    with sync_playwright() as p:
        # channel="chrome" especifica que use Google Chrome instalado en tu sistema
        context = p.chromium.launch_persistent_context(
            user_data_dir=user_data_dir,
            headless=False,
            channel="chrome",  # <--- Usa el Google Chrome del sistema
            viewport={"width": 1280, "height": 800},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            ignore_default_args=["--enable-automation"],
            args=[
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox",
                "--disable-infobars"
            ]
        )
        
        page = context.pages[0] if context.pages else context.new_page()

        # Ocultar indicador navigator.webdriver
        page.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            });
        """)
        
        print("\n" + "="*60)
        print("  🌐 Cargando TikTok en Google Chrome...")
        page.goto("https://www.tiktok.com", wait_until="domcontentloaded")
        
        print("\n  👉 ATENCIÓN: Revisa la ventana del navegador.")
        print("     1. Si aparece la página principal de TikTok normalmente, todo está listo.")
        print("     2. Si aparece un Captcha, resuélvelo manualmente esta vez.")
        print("="*60 + "\n")

        input("📌 Presioná ENTER en la terminal cuando la página haya cargado correctamente... ")
        print("\n🚀 ¡Iniciando extracción de videos!")

        for brand, tags in HASHTAGS.items():
            processed_urls_for_brand = set()
            
            for tag in tags:
                tag_url = f"https://www.tiktok.com/tag/{tag}"
                print(f"  🔍 Analizando hashtag: #{tag} ({brand})...")
                
                try:
                    page.goto(tag_url, wait_until="domcontentloaded", timeout=15000)
                    time.sleep(3)
                    
                    page.evaluate("window.scrollTo(0, 1000)")
                    time.sleep(2)

                    hrefs = page.eval_on_selector_all(
                        'a[href*="/video/"]', 
                        'elements => elements.map(e => e.href)'
                    )

                    links_found = []
                    for link in hrefs:
                        if "/video/" in link and link not in processed_urls_for_brand:
                            links_found.append(link)
                            processed_urls_for_brand.add(link)

                    print(f"     🔗 Detectados {len(links_found)} videos nuevos para #{tag}. Procesando los 3 primeros...")

                    for link in links_found[:3]:
                        details = fetch_details_from_video(page, link)
                        print(f"        └─ Video: {details['likes']} ❤️ | {details['comments']} 💬")
                        
                        raw_results.append({
                            "brand": brand,
                            "hashtag": tag,
                            "url": link,
                            "likes": details["likes"],
                            "comments": details["comments"],
                            "scraped_at": datetime.now().isoformat()
                        })
                        time.sleep(1)

                except Exception as e:
                    print(f"     ❌ Error procesando #{tag}: {e}")

        context.close()

    today_str = datetime.now().strftime("%Y%m%d")
    output_filename = f"raw_tiktok_{today_str}.json"
    
    with open(output_filename, "w", encoding="utf-8") as f:
        json.dump(raw_results, f, ensure_ascii=False, indent=4)
        
    print(f"[{datetime.now().strftime('%H:%M:%S')}] 💾 Guardado exitoso en {output_filename} ({len(raw_results)} registros)")

if __name__ == "__main__":
    run_scraper()