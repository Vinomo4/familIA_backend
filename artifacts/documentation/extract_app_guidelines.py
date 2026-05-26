import os
import sys
import time
import sqlite3
from typing import Set, List
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
from curl_cffi import requests
from google import genai
from google.genai import types


class BBVADeepMarkdownCompilerEN:
    def __init__(
        self, db_path: str = "artifacts/documentation/cache_scraped_pages_en.db"
    ):
        self.base_domain = "https://www.bbva.es"
        self.index_urls = [
            "https://www.bbva.es/en/finanzas-vistazo/tu-guia-bbva.html",
            "https://www.bbva.es/en/finanzas-vistazo/tu-guia-bbva.pag-2.html",
            "https://www.bbva.es/en/finanzas-vistazo/tu-guia-bbva.pag-3.html",
            "https://www.bbva.es/en/finanzas-vistazo/tu-guia-bbva.pag-4.html",
            "https://www.bbva.es/en/finanzas-vistazo/tu-guia-bbva.pag-5.html",
        ]
        self.db_path = db_path
        self.session = requests.Session()
        self.article_links: Set[str] = set()

        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS cache_guides_en (
                    url TEXT PRIMARY KEY,
                    title TEXT NOT NULL,
                    clean_text TEXT NOT NULL,
                    scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()

    def _get_cached_content(self, url: str) -> str:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT title, clean_text FROM cache_guides_en WHERE url = ?", (url,)
            )
            row = cursor.fetchone()
            if row:
                title, clean_text = row
                return f"\n\n=== DEEP ENGLISH ARTICLE (CACHED): {title} ===\nURL: {url}\n{clean_text}"
        return None

    def _save_to_cache(self, url: str, title: str, clean_text: str):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT OR REPLACE INTO cache_guides_en (url, title, clean_text)
                VALUES (?, ?, ?)
            """,
                (url, title, clean_text),
            )
            conn.commit()

    def harvest_all_article_links(self) -> List[str]:
        print("[*] STAGE 1: Starting Deep English Article Link Harvesting...")
        for index_url in self.index_urls:
            print(f"[*] Extracting anchors from English directory index: {index_url}")
            try:
                response = self.session.get(index_url, impersonate="chrome", timeout=15)
                response.raise_for_status()
                soup = BeautifulSoup(response.text, "html.parser")

                for anchor in soup.find_all("a", href=True):
                    href = anchor["href"].split("#")[0].split("?")[0]
                    absolute_url = urljoin(self.base_domain, href)

                    if "www.bbva.es/en/" in absolute_url:
                        if any(
                            folder in absolute_url
                            for folder in [
                                "/finanzas-vistazo/",
                                "/cuentas/",
                                "/tarjetas/",
                                "/transferencias/",
                                "/oficina/",
                            ]
                        ):
                            if not any(
                                bad_pattern in absolute_url
                                for bad_pattern in [".pag-", "tu-guia-bbva.html"]
                            ):
                                self.article_links.add(absolute_url)

            except Exception as e:
                print(
                    f"[-] Warning: Failed to parse index list {index_url}: {e}",
                    file=sys.stderr,
                )

        print(
            f"[+] Stage 1 Complete. Isolated {len(self.article_links)} unique English tutorial guides."
        )
        return sorted(list(self.article_links))

    def scrape_deep_body_content(self, url: str) -> str:
        cached_data = self._get_cached_content(url)
        if cached_data:
            print(f"[->] Cache Hit (English Local Storage): {url.split('/')[-1]}")
            return cached_data

        try:
            time.sleep(1.2)
            response = self.session.get(url, impersonate="chrome", timeout=10)
            if response.status_code != 200:
                return ""

            soup = BeautifulSoup(response.text, "html.parser")

            page_title = "Unknown English Article"
            if soup.title:
                page_title = soup.title.get_text().split("|")[0].strip()
            elif url.split("/")[-1]:
                page_title = (
                    url.split("/")[-1].replace(".html", "").replace("-", " ").title()
                )

            for boilerplate in soup(
                [
                    "script",
                    "style",
                    "nav",
                    "footer",
                    "header",
                    "noscript",
                    "iframe",
                    "aside",
                ]
            ):
                boilerplate.decompose()

            body_text = soup.get_text(separator="\n")
            lines = [line.strip() for line in body_text.splitlines() if line.strip()]
            clean_text_payload = "\n".join(lines)

            self._save_to_cache(url, page_title, clean_text_payload)
            print(f"[+] Network Fetch & Cached English Deep Body: {page_title}")

            return f"\n\n=== DEEP ENGLISH ARTICLE CONTENT: {page_title} ===\nURL: {url}\n{clean_text_payload}"

        except Exception as e:
            print(
                f"[-] Skipping processing for target {url} due to failure: {e}",
                file=sys.stderr,
            )
            return ""

    def compile_full_context_stack(self) -> str:
        child_urls = self.harvest_all_article_links()

        print("[*] Ingesting root layout context data...")
        consolidated_context = (
            self.scrape_guide_content(self.seed_url)
            if hasattr(self, "seed_url")
            else ""
        )

        for index, target_url in enumerate(child_urls, start=1):
            print(f"[*] Processing detailed article path {index}/{len(child_urls)}")
            page_data = (
                self.scrape_guide_content(target_url)
                if hasattr(self, "scrape_guide_content")
                else self.scrape_deep_body_content(target_url)
            )
            if page_data:
                consolidated_context += page_data

        return consolidated_context


def execute_context_cleaning(raw_context_path: str, clean_output_path: str):
    """
    LLM CALL 1: Parses raw text dump, strips out non-utility boilerplate elements,
    structures the operational guides, and structures the content into an expanded markdown artifact.
    """
    print("[*] LLM CALL 1: Initializing text content optimization pipeline...")
    if not os.environ.get("GEMINI_API_KEY"):
        raise ValueError(
            "Missing critical environment payload: GEMINI_API_KEY must be exported."
        )

    with open(raw_context_path, "r", encoding="utf-8") as f:
        raw_text = f.read()

    client = genai.Client()

    system_prompt = (
        "You are an expert Technical Documentation Clean-up Engine. Your goal is to transform a noisy, web-scraped dump of "
        "retail banking tutorials into a highly detailed, clean, structured technical Markdown manual (.md).\n\n"
        "Strict Content Rules:\n"
        "1. Maximize Operational Utility: Keep all operational definitions, step-by-step procedures, capability listings, tutorial steps, "
        "and detailed Question & Answer (Q&A) pairs.\n"
        "2. Ruthless Noise Filtering: Completely discard cookie warnings, legal statements, footer links, privacy policies, UI marketing taglines, "
        "and layout navigation text fragments that offer no capability information.\n"
        "3. Preserve Complete Detail: Do not synthesize or summarize. Extract descriptions in full depth. If an article details a multi-step troubleshooting path "
        "or edge-case scenario, extract every single condition and step.\n"
        "4. Output Format: Emit purely valid Markdown code. Do not wrap your response in conversational preambles, introductory meta-commentary, or markdown blocks."
    )

    user_content = (
        "Process and optimize the raw text block enclosed in the XML tags below. Clean, structure, and output it as a comprehensive markdown documentation file.\n\n"
        "<raw_scraped_text>\n"
        f"{raw_text}\n"
        "</raw_scraped_text>"
    )

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=[user_content],
        config=types.GenerateContentConfig(
            system_instruction=system_prompt, temperature=0.1, top_p=0.95
        ),
    )

    with open(clean_output_path, "w", encoding="utf-8") as f:
        f.write(response.text)
    print(
        f"[+] LLM CALL 1 Complete. Structured context output saved to: {clean_output_path}"
    )


def execute_gemini_compilation(
    pdf_path: str, clean_markdown_path: str, final_output_path: str
):
    """
    LLM CALL 2: Cross-references the visual application screens from the PDF with the
    completely cleaned, highly detailed text tutorials to generate an extensive, unconstrained master guide.
    """
    print("[*] LLM CALL 2: Initializing master cross-modal manual synthesis...")
    client = genai.Client()

    print("[*] Uploading visual UX reference mapping PDF via GenAI Files API...")
    uploaded_file = client.files.upload(file=pdf_path)
    print(
        f"[+] File instantiation successful. Handle tracking locator URI: {uploaded_file.uri}"
    )

    with open(clean_markdown_path, "r", encoding="utf-8") as f:
        clean_web_context = f.read()

    system_prompt = (
        "You are a Senior Systems Documentation Architect. Your task is to combine an application screen layout blueprint (PDF file) "
        "with a thoroughly cleaned text database of step-by-step app tutorials to produce an extensively detailed, comprehensive Master UI Guide.\n\n"
        "Strict Synthesis Mandates:\n"
        "1. Length and Depth Maximization: You are explicitly forbidden from truncating, summarizing, or condensing the material. "
        "The final guideline document must be exhaustive and trace every possible user pathway, condition, layout anchor, and exception rule found in the text.\n"
        "2. Layout-to-Action Interpolation: For every application screen identified in the PDF blueprint, systematically extract and link "
        "every corresponding step-by-step tutorial, FAQ pair, and troubleshooting guideline from the clean web context under a '### Detailed Operation & Edge Cases' section.\n"
        "3. Explicit Technical Anchoring: Every target visual element must maintain strict literal bracket syntax references (e.g., buttons must be written exactly as [Continue], [Accept] or [Next]).\n"
        "4. Absolute Clarity: Translate layout topology into precise physical instructions (e.g., 'the button with three lines at the top left corner' or 'the input field located in the center wrapper').\n"
        "5. Output Integrity: Emit purely valid Markdown. Do not include introductory text, meta-commentary, or wrap the file in trailing conversational phrases."
    )

    user_content = (
        "Execute the deep document compilation task by combining the uploaded PDF layout blueprint file with the optimized website documentation context enclosed below.\n\n"
        "<cleaned_webpage_context>\n"
        f"{clean_web_context}\n"
        "</cleaned_webpage_context>\n\n"
        "Provide an uncompromisingly complete manual layout according to the system rules."
    )

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=[uploaded_file, user_content],
            config=types.GenerateContentConfig(
                system_instruction=system_prompt, temperature=0.1, top_p=0.95
            ),
        )

        with open(final_output_path, "w", encoding="utf-8") as f:
            f.write(response.text)
        print(
            f"[+] LLM CALL 2 Complete. Master guideline output saved to: {final_output_path}"
        )

    finally:
        print(
            "[*] Post-execution pipeline cleanup: Purging visual binary asset record from remote engine..."
        )
        client.files.delete(name=uploaded_file.name)


if __name__ == "__main__":
    # Normalized deployment paths
    INPUT_PDF = "artifacts/documentation/bbva.pdf"
    RAW_TEXT_OUT = "artifacts/documentation/bbva_scraped_raw_en.txt"
    CLEAN_MD_OUT = "artifacts/documentation/bbva_web_clean_en.md"
    OUTPUT_MD = "artifacts/documentation/bbva_manual_en.md"

    # 1. Extraction Crawler Phase
    deep_compiler = BBVADeepMarkdownCompilerEN()
    target_articles = deep_compiler.harvest_all_article_links()

    print("\n[*] STAGE 2: Launching Deep English Content Body Extraction Sweep...")
    consolidated_rich_text = ""
    for idx, article_url in enumerate(target_articles, start=1):
        print(f"[*] Processing detailed article path {idx}/{len(target_articles)}")
        article_body = deep_compiler.scrape_deep_body_content(article_url)
        if article_body:
            consolidated_rich_text += article_body

    print(f"\n[*] Exporting unified English rich text corpus file to: {RAW_TEXT_OUT}")
    with open(RAW_TEXT_OUT, "w", encoding="utf-8") as f:
        f.write(consolidated_rich_text)
    print("[+] Raw deep English text data stack safely preserved.")

    # 2. LLM Call 1: Clean and optimize the crawled text blocks
    execute_context_cleaning(RAW_TEXT_OUT, CLEAN_MD_OUT)

    # 3. LLM Call 2: Perform the final exhaustive master-guide compilation
    execute_gemini_compilation(INPUT_PDF, CLEAN_MD_OUT, OUTPUT_MD)
