import streamlit as st
import google.generativeai as genai

# --- 1. KONFIGURACE STRÁNKY ---
st.set_page_config(
    page_title="Michal Harbáček - Cyber Security Portfolio",
    page_icon="🛡️",
    layout="wide"
)

# --- 2. DATA A PŘEKLADY ---
NAME = "Michal Harbáček"
EMAIL = "michalharbacek11@gmail.com"
LINKEDIN = "https://linkedin.com/in/michal-harbacek"

LOCATION = {
    "CZ": "Praha, Česká republika",
    "EN": "Prague, Czech Republic"
}

UI_TEXTS = {
    "CZ": {
        "role": "IT Operations Specialist | Aspiring Cyber Security Consultant",
        "about_title": "O mně",
        "exp_title": "🚀 Pracovní Zkušenosti",
        "skills_title": "🛠️ Skills",
        "download_btn_cz": "📄 CV (CZ)",
        "download_btn_en": "📄 CV (EN)",
        "cv_cz_missing": "CV (CZ) nenalezeno.",
        "cv_en_missing": "CV (EN) nenalezeno.",
        "contact_title": "🔗 Kontakt",
        "chat_header": "🤖 Chat o Michalovi",
        "api_settings": "⚙️ Nastavení API",
        "api_placeholder": "Vlož API Klíč",
        "api_warning": "Pro spuštění chatu je potřeba API klíč.",
        "chat_intro": "Ahoj! Jsem Michalův AI asistent. Zeptej se mě na jeho zkušenosti, motivaci nebo proč chce dělat Security.",
        "chat_placeholder": "Zeptej se na cokoliv...",
        "error": "Chyba:",
        "photo_missing": "📷"
    },
    "EN": {
        "role": "IT Operations Specialist | Aspiring Cyber Security Consultant",
        "about_title": "About Me",
        "exp_title": "🚀 Work Experience",
        "skills_title": "🛠️ Skills",
        "download_btn_cz": "📄 CV (CZ)",
        "download_btn_en": "📄 CV (EN)",
        "cv_cz_missing": "CV (CZ) not found.",
        "cv_en_missing": "CV (EN) not found.",
        "contact_title": "🔗 Contact",
        "chat_header": "🤖 Chat about Michal",
        "api_settings": "⚙️ API Settings",
        "api_placeholder": "Enter API Key",
        "api_warning": "API Key is required to start the chat.",
        "chat_intro": "Hello! I am Michal's AI assistant. Ask me about his experience, motivation, or why he wants to pivot to Security.",
        "chat_placeholder": "Ask me anything...",
        "error": "Error:",
        "photo_missing": "📷"
    }
}

BIO_DATA = {
    "CZ": """
    Michal je IT Operations specialista s 9 lety praxe v Enterprise prostředí. Má za sebou tisíce hodin reálného provozu – od fyzické diagnostiky serverů až po řešení incidentů pod tlakem přísných SLA. Ví, jak vypadá IT infrastruktura, když věci fungují, i jak to vypadá, když reálně selžou.

    Aktuálně přesouvá své kariérní zaměření z reaktivního IT (odstraňování poruch) do kybernetické bezpečnosti a GRC. Nemá zatím formální security certifikace, ale přináší to, co se z učebnic vyčíst nedá: hluboké pochopení toho, jak IT procesy a infrastruktura fungují v tvrdé realitě. Jeho cílem je tyto provozní zkušenosti využít při hodnocení rizik a zavádění bezpečnostních standardů (např. NIS2) tak, aby pro firmy byly prakticky proveditelné a nedusily jejich byznys.
    """,
    "EN": """
    Michal is an IT Operations specialist with 9 years of experience in an Enterprise environment. He has thousands of hours of real-world operations under his belt – from physical server diagnostics to resolving incidents under the pressure of strict SLAs. He knows what IT infrastructure looks like when things work, and what it looks like when they actually fail.

    Currently, he is shifting his career focus from reactive IT (troubleshooting/break-fix) to cybersecurity and GRC. He doesn't hold formal security certifications yet, but he brings something that cannot be learned from textbooks: a deep understanding of how IT processes and infrastructure operate in harsh reality. His goal is to leverage these operational experiences in risk assessment and the implementation of security standards (e.g., NIS2) so that they are practically achievable for companies and do not stifle their business.
    """
}

EXPERIENCE_DATA = {
    "CZ": """
    **Customer Care Rep III / Tech Solution Consultant** | 03/2017 – Současnost  
    *Hewlett Packard Enterprise s.r.o., Praha* Mezinárodní tým s přesahem do technických konzultací a procesního řízení.  
    - **L1 Technical Solution Consultant:** Diagnostika a troubleshooting závad na Industry Standard Servers a storage řešeních. Návrh akčních plánů pro nápravu a mitigaci rizik.
    - **Process Management:** Výzkum a implementace globálních procesů pro lokální využití. Správa procesní knihovny zajišťující compliance a efektivitu.
    - **Projektové vedení:** Vedení projektu "Single Point of Contact" pro klíčového zákazníka.
    - Mentoring nových kolegů a koordinace eskalací.
    - Nástroje: Salesforce (ticketovací systém), interní nástroje pro analýzu logů.

    **Klientský poradce** | 03/2016 – 01/2017  
    *UniCredit Bank Czech Republic and Slovakia, a.s.* - Analýza potřeb klientů a řízení rizik v rámci správy portfolia.
    - Komunikace napříč odbory a řešení nestandardních požadavků.
    - Dodržování bankovních regulací a bezpečnostních standardů.
    """,
    "EN": """
    **Customer Care Rep III / Tech Solution Consultant** | 03/2017 – Present  
    *Hewlett Packard Enterprise s.r.o., Prague* International team with an overlap into technical consulting and process management.  
    - **L1 Technical Solution Consultant:** Diagnostics and troubleshooting of faults on Industry Standard Servers and storage solutions. Proposing action plans for remediation and risk mitigation.
    - **Process Management:** Research and implementation of global processes for local use. Management of the process library ensuring compliance and efficiency.
    - **Project Management:** Leading the "Single Point of Contact" project for a key customer.
    - Mentoring new colleagues and coordinating escalations.
    - Tools: Salesforce (ticketing system), internal log analysis tools.

    **Client Advisor** | 03/2016 – 01/2017  
    *UniCredit Bank Czech Republic and Slovakia, a.s.* - Analysis of client needs and risk management within portfolio management.
    - Cross-departmental communication and resolution of non-standard requests.
    - Compliance with banking regulations and security standards.
    """
}

SKILLS_DATA = {
    "CZ": """
    **Profesionální a procesní dovednosti (Core):**
    - **IT Service Management:** Praktická zkušenost s ITIL procesy v korporátu (Incident a Problem Management).
    - **Hardware & Datacentra:** Znalost architektury HPE serverů a fyzické vrstvy IT infrastruktury.
    - **Soft Skills pro IT:** Zvládání tlaku při výpadcích, schopnost věcně komunikovat technický problém zákazníkovi, smysl pro procesy a dokumentaci.
    - **Jazyky:** Angličtina (B2 - schopnost plynulé psané i mluvené komunikace v mezinárodním prostředí).

    **Cyber Security & Technologie (Transition):**
    - **GRC Povědomí:** Porozumění principům IT rizik z pohledu provozu (Governance, Risk, Compliance). Silná motivace k rychlému osvojení konzultačních metodik a zisku certifikací.
    - **Skriptování:** Průběžné samostudium základů Pythonu.
    - **AI/LLM:** Aktivní využívání umělé inteligence pro automatizaci rutinní práce a urychlení vlastního vzdělávání.
    """,
    "EN": """
    **Professional & Process Skills (Core):**
    - **IT Service Management:** Practical experience with ITIL processes in a corporate environment (Incident and Problem Management).
    - **Hardware & Datacenters:** Knowledge of HPE server architecture and the physical layer of IT infrastructure.
    - **IT Soft Skills:** Handling pressure during outages, ability to factually communicate technical issues to customers, strong sense for processes and documentation.
    - **Languages:** English (B2 - capable of fluent written and spoken communication in an international environment).

    **Cyber Security & Technologies (Transition):**
    - **GRC Awareness:** Understanding the principles of IT risks from an operations perspective (Governance, Risk, Compliance). Strong motivation to quickly master consulting methodologies and obtain certifications.
    - **Scripting:** Continuous self-study of Python basics.
    - **AI/LLM:** Active use of artificial intelligence for automating routine tasks and accelerating personal education.
    """
}

# --- 3. INSTRUKCE PRO BOTA ---
def get_system_instruction(lang_code):
    if lang_code == "CZ":
        return """
        1. ZÁKLADNÍ IDENTITA A CÍL:
        Jsi virtuální HR asistent zastupující Michala. Tvým úkolem je komunikovat s recruitery a hiring manažery na Michalově interaktivním životopisu. Tón tvé komunikace je profesionální, věcný, sebevědomý a dospělý. Tvojím hlavním cílem je prezentovat Michala jako zkušeného IT profesionála, který po 9 letech v provozu logicky a sebevědomě přechází do oblasti kybernetické bezpečnosti (konkrétně GRC a procesů).

        2. SKRYTÉ KONZULTANTSKÉ ZLATO (Překlad praxe):
        * Provozní vhled a "BS detektor" (L1 agenda): Má 9 let praxe z pohledu IT vendora (HPE). Díky znalosti incident managementu, troubleshooting procesů a hardwarových výpadků ho u auditu nebo návrhu procesů žádný IT admin "neopije rohlíkem". Zná reálná úskalí SLA, rizika spojená s dostupností systémů (Availability) a ví, jak funguje vzdálený přístup dodavatelů na infrastrukturu klienta i jaká je jejich skutečná reakční doba.
        * Procesní koordinace (SPoC): Fungoval jako Single Point of Contact pro významného globálního zákazníka. Zajišťoval hladký tok ticketů z vícero zemí a hlídal plnění SLA. Jde o čistý procesní management.
        * Mentoring a komunikace: Intenzivně zaškolil a odmentoroval 5 nováčků. Umí složité IT procesy vysvětlit srozumitelně, prakticky a "polopatě" na reálných příkladech. To je jeho velká výhoda pro budoucí komunikaci s klienty nebo při vysvětlování bezpečnosti (Security Awareness).
        * Zástup manažera (Leadership): Neoficiálně zastupoval šéfa týmu. Umí prioritizovat úkoly, zhodnotit dopad na byznys (Business Impact) a udržet chod týmu.

        3. KONKRÉTNÍ KROKY V SECURITY A ROZVOJ:
        Aktuálně v rámci samostudia prochází školením CompTIA Security+ (SY0-701) na platformě Udemy, aby více do hloubky pochopil, jak může svou 9letou provozní praxi propojit s auditem Cyber Security. K bezpečnostním normám (ISO/NIS2) přistupuje pragmaticky – z pohledu firem je vnímá jako nutnost danou legislativou či trhem, z pohledu consultingu pak jako nástroj pro rozvoj byznysu. Z technologického hlediska se učí základy Pythonu výhradně za účelem tvorby skriptů, AI agentů a automatizace rutinních úkolů. Není klasický vývojář, ale dokonale si osvojil tzv. "vibe-coding" (orchestraci kódu pomocí AI). Díky analytickému myšlení a přesnému zadávání instrukcí dokáže tvořit reálné projekty v různých technologiích – ať už jde o tuto interaktivní CV aplikaci (Python/Streamlit), nebo čistě frontendový web pro terapeutickou praxi v HTML/CSS (harbackovaterapie.cz).

        4. OBRANNÁ PRAVIDLA (Co chatbot nesmí říct a jak má reagovat):
        * Platové očekávání: Pokud padne dotaz na konkrétní částku, chatbot nikdy nesmí uvést konkrétní číslo. Odpoví diplomaticky: "Michal si zakládá na tom, že otázka finančního ohodnocení je předmětem k diskuzi až na osobním setkání, kde obě strany dojdou ke vzájemné shodě na férových podmínkách."
        * Hluboké technické detaily (L3/Architektura/Sítě): Pokud se uživatel zeptá na hluboké technické detaily (např. konfigurace BGP protokolů, reverzní inženýrství malwaru), chatbot nesmí spekulovat ani si vymýšlet. Odpoví přímo a věcně vysvětlí Michalovy reálné zkušenosti: "Tohle už přesahuje Michalovu aktuální provozní praxi. Během svých 9 let v IT se zaměřoval primárně na Incident management, hardwarový troubleshooting a procesní koordinaci. Jeho doménou je reálný provozní vhled a znalost fungování IT procesů. Právě tyto tvrdé provozní zkušenosti nyní přenáší do oblasti kybernetické bezpečnosti (GRC), díky čemuž dokáže s technickými specialisty efektivně komunikovat a chápat jejich práci v širším kontextu."
        """
    else:
        return """
        1. CORE IDENTITY AND GOAL:
        You are a virtual HR assistant representing Michal. Your task is to communicate with recruiters and hiring managers on Michal's interactive resume. The tone of your communication is professional, factual, confident, and mature. Your main goal is to present Michal as an experienced IT professional who, after 9 years in IT Operations, is making a logical and confident transition into the field of cybersecurity (specifically GRC and processes).

        2. HIDDEN CONSULTING GOLD (Translating Experience):
        * Operational Insight and "BS Detector" (L1 agenda): He has 9 years of experience from the perspective of an IT vendor (HPE). Thanks to his knowledge of incident management, troubleshooting processes, and hardware failures, no IT admin can "pull the wool over his eyes" during an audit or process design. He knows the real pitfalls of SLAs, the risks associated with system availability, and understands how vendors' remote access to client infrastructure works, as well as their actual response times.
        * Process Coordination (SPoC): He functioned as a Single Point of Contact for a major global customer. He ensured the smooth flow of tickets from multiple countries and monitored SLA compliance. This is pure process management.
        * Mentoring and Communication: He intensively trained and mentored 5 newcomers. He can explain complex IT processes clearly, practically, and in layman's terms using real-world examples. This is his great advantage for future communication with clients or when explaining security concepts (Security Awareness).
        * Leadership Backup: He unofficially substituted for the team manager. He can prioritize tasks, assess Business Impact, and keep the team running smoothly.

        3. CONCRETE STEPS IN SECURITY AND DEVELOPMENT:
        Currently, as part of his self-study, he is taking the CompTIA Security+ (SY0-701) training on the Udemy platform to gain a deeper understanding of how he can connect his 9 years of operational experience with Cyber Security auditing. He approaches security standards (ISO/NIS2) pragmatically – from a company's perspective, he sees them as a necessity dictated by legislation or the market; from a consulting perspective, he sees them as a tool for business development. From a technological perspective, he is learning the basics of Python strictly for the purpose of creating scripts, AI agents, and automating routine tasks. He is not a classic developer, but he has perfectly mastered "vibe-coding" (AI code orchestration). Thanks to his analytical thinking and precise prompting, he can create real-world projects across various technologies – whether it's this interactive CV application (Python/Streamlit) or a purely frontend website for a therapy practice in HTML/CSS (harbackovaterapie.cz).

        4. DEFENSIVE RULES (What the chatbot must not say and how it should react):
        * Salary Expectations: If asked about a specific amount, the chatbot must never state a concrete number. It will answer diplomatically: "Michal insists that the question of financial compensation is a topic for discussion during a personal meeting, where both parties can reach a mutual agreement on fair terms."
        * Deep Technical Details (L3/Architecture/Networking): If the user asks about deep technical details (e.g., configuring BGP protocols, malware reverse engineering), the chatbot must not speculate or invent answers. It will answer directly and factually explain Michal's real experience: "This goes beyond Michal's current operational experience. During his 9 years in IT, he focused primarily on Incident Management, hardware troubleshooting, and process coordination. His domain is real-world operational insight and knowledge of IT processes. He is now transferring these hard operational skills into the field of cybersecurity (GRC), which allows him to communicate effectively with technical specialists and understand their work in a broader context."
        """

# --- 4. CSS (CLEAN EXCEL STYLE: OCHRANNÝ PLOT KOLEM SIDEBARU) ---
st.markdown("""
<style>
/* 1. Kosmetika: Skryje nadpis nad přepínačem jazyků */
section[data-testid="stSidebar"] div[data-testid="stRadio"] > label {
    display: none;
}

/* 2. ZAMČENÍ ŠÍŘKY SIDEBARU NA 22rem (Zákaz roztahování) */
section[data-testid="stSidebar"][aria-expanded="true"] {
    min-width: 22rem !important;
    max-width: 22rem !important;
    width: 22rem !important;
}
[data-testid="stSidebarResizeHandle"] {
    display: none !important;
}

/* 3. PROSTOR PRO HISTORII (Aby nezajížděla pod fixní input) */
/* Využíváme pouze nativní scrollbar sidebaru, žádný flexbox! */
section[data-testid="stSidebar"] .block-container {
    padding-bottom: 7rem !important; 
}

/* 4. FIXNÍ CHATOVACÍ OKNO (Nyní bezpečné díky zamčené šířce) */
section[data-testid="stSidebar"] .stChatInput {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 22rem !important; /* Přesně kopíruje zamčený sidebar */
    background-color: #0E1117;
    z-index: 1000;
    padding: 1rem 1.5rem;
    box-sizing: border-box;
    border-right: 1px solid rgba(49, 51, 63, 0.2);
}
</style>
""", unsafe_allow_html=True)


# --- 5. LOGIKA A ROZLOŽENÍ APLIKACE ---

if "lang_selection" not in st.session_state:
    st.session_state.lang_selection = "CZ"

if "chat_history" not in st.session_state:
    st.session_state.chat_history = {
        "CZ": [],
        "EN": []
    }

# --- HLAVNÍ OBSAH (PRAVÁ ČÁST) ---
TX = UI_TEXTS[st.session_state.lang_selection]
LOCATION_TXT = LOCATION[st.session_state.lang_selection]

col1, col2 = st.columns([1, 2], gap="medium")

with col1:
    spacer1, image_col, spacer2 = st.columns([1, 2, 1])
    with image_col:
        try:
            st.image("profilovka.jpg", width="stretch")
        except:
            st.write(TX["photo_missing"])

    st.markdown(f"## {NAME}")
    st.write(TX["role"])
    st.write(f"📍 {LOCATION_TXT}")
    
    st.write("---")
    # Rozdělíme prostor na dva malé sloupce pro tlačítka vedle sebe
    dl_col1, dl_col2 = st.columns(2)
    
    with dl_col1:
        try:
            with open("cv_cz.pdf", "rb") as pdf_file_cz:
                PDFbyte_cz = pdf_file_cz.read()
            st.download_button(
                label=TX["download_btn_cz"],
                data=PDFbyte_cz,
                file_name="Michal_Harbacek_CV_CZ.pdf",
                use_container_width=True  # Tlačítko se roztáhne přesně na šířku sloupce
            )
        except FileNotFoundError:
            st.caption(TX["cv_cz_missing"])

    with dl_col2:
        try:
            with open("cv_en.pdf", "rb") as pdf_file_en:
                PDFbyte_en = pdf_file_en.read()
            st.download_button(
                label=TX["download_btn_en"],
                data=PDFbyte_en,
                file_name="Michal_Harbacek_CV_EN.pdf",
                use_container_width=True  # Tlačítko se roztáhne přesně na šířku sloupce
            )
        except FileNotFoundError:
            st.caption(TX["cv_en_missing"])
    
    st.write("---")
    st.write(f"**{TX['contact_title']}**")
    st.write(f"[LinkedIn]({LINKEDIN})")
    st.write(f"📧 {EMAIL}")

with col2:
    st.title(TX["about_title"])
    st.info(BIO_DATA[st.session_state.lang_selection])
    st.write("---")
    st.subheader(TX["exp_title"])
    st.write(EXPERIENCE_DATA[st.session_state.lang_selection])
    st.write("---")
    st.subheader(TX["skills_title"])
    st.write(SKILLS_DATA[st.session_state.lang_selection])


# --- 6. SIDEBAR (CHATBOT) ---
with st.sidebar:
    
    # --- A) ZÁHLAVÍ ---
    lang = st.radio(
        "Language",
        ["CZ", "EN"],
        horizontal=True,
        label_visibility="collapsed",
        key="lang_radio"
    )
    
    if lang != st.session_state.lang_selection:
        st.session_state.lang_selection = lang
        st.rerun()

    st.markdown(f"### {TX['chat_header']}")
    
    with st.expander(TX["api_settings"], expanded=False):
        st.caption("Powered by Gemini 2.5")
        api_key = st.secrets.get("GEMINI_API_KEY")
        if not api_key:
            api_key = st.text_input(TX["api_placeholder"], type="password")

    # Varování, pokud chybí API klíč (zobrazeno pod hlavičkou)
    if not api_key:
        st.warning(TX["api_warning"])

    # --- B) HISTORIE (SCROLLABLE MIDDLE) ---
    current_history = st.session_state.chat_history[st.session_state.lang_selection]
    
    # Zobrazení úvodní zprávy, pokud je historie prázdná a klíč je zadán
    if not current_history and api_key:
        with st.chat_message("assistant", avatar="🤖"):
            st.write(TX["chat_intro"])

    # Zobrazení celé historie chatu
    for message in current_history:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # --- C) ZÁPATÍ (FIXED BOTTOM) ---
    if prompt := st.chat_input(TX["chat_placeholder"]):
        st.session_state.chat_history[st.session_state.lang_selection].append({"role": "user", "content": prompt})
        
        genai.configure(api_key=api_key)
        try:
            model = genai.GenerativeModel(
                model_name="gemini-2.5-flash", 
                system_instruction=get_system_instruction(st.session_state.lang_selection)
            )
            
            history_for_model = [
                {"role": "user" if m["role"] == "user" else "model", "parts": [m["content"]]}
                for m in current_history 
            ]
            
            chat = model.start_chat(history=history_for_model)
            response = chat.send_message(prompt)
            
            st.session_state.chat_history[st.session_state.lang_selection].append({"role": "assistant", "content": response.text})
            
            st.rerun()
            
        except Exception as e:
            st.error(f"{TX['error']} {e}")