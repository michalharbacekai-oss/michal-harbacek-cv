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
    Michal je IT Operations specialista s 9 lety praxe v Enterprise prostředí (HPE). 
    Má praktické zkušenosti s diagnostikou serverového hardwaru (Break/fix) a procesem Incident Managementu (ITIL).

    Aktuálně se rozhodl pro kariérní změnu do oblasti Cyber Security. 
    Jde o pragmatické rozhodnutí – tento obor ho zaujal svou náplní a perspektivou. 
    Je na začátku této cesty a jeho cílem je postupně získat znalosti, aby mohl své rozsáhlé provozní zkušenosti (Ops) a znalost IT procesů naplno uplatnit v kybernetické bezpečnosti.
    """,
    "EN": """
    Michal is an IT Operations Specialist with 9 years of experience in an Enterprise environment (HPE).
    He has solid practical experience with server hardware diagnostics (Break/fix) and Incident Management processes (ITIL).

    Currently, he has decided to make a career shift into Cyber Security. 
    This is a pragmatic decision – the field appeals to him due to its analytical nature and future perspective. 
    He is at the beginning of this journey, aiming to gradually acquire knowledge to fully apply his extensive operational experience (Ops) and knowledge of IT processes in the field of cyber security.
    """
}

EXPERIENCE_DATA = {
    "CZ": """
    Pracovní historie (Solidní praxe v Operations):
    1. Hewlett Packard Enterprise (03/2017 - Současnost):
       - Pozice: Tech Solution Consultant / Break-fix Support.
       - Náplň: Diagnostika a výměna serverového hardwaru, řešení incidentů dle SLA.
       - Procesy: Práce v ticketovacích systémech, eskalace, komunikace v týmu.
    2. UniCredit Bank (03/2016 - 01/2017):
       - Klientský poradce, administrativa a dodržování bankovních postupů.
    """,
    "EN": """
    Work History (Solid Operations Experience):
    1. Hewlett Packard Enterprise (03/2017 - Present):
       - Position: Tech Solution Consultant / Break-fix Support.
       - Role: Diagnostics and replacement of server hardware, incident resolution according to SLAs.
       - Processes: Incident Management, ticket handling, escalation procedures, effective team communication.
    2. UniCredit Bank (03/2016 - 01/2017):
       - Client Advisor, risk management, and banking compliance.
    """
}

SKILLS_DATA = {
    "CZ": """
    Technické dovednosti (Level: Student / Začátečník):
    - Python: Začátečník - učí se základy skriptování (samostudium).
    - Cyber Security: Absolutní začátečník - seznamuje se s oborem, má silnou motivaci se učit, ale zatím bez konkrétních znalostí.
    - AI/LLM: Uživatelský zájem o automatizaci.

    Profesionální dovednosti (Level: Zkušený):
    - Hardware Support: Diagnostika HPE serverů (standardní postupy).
    - ITIL Procesy: Znalost životního cyklu incidentu v korporátu.
    - Angličtina (B2 - komunikativní).
    """,
    "EN": """
    Technical Skills (Level: Student / Beginner):
    - Python: Beginner - learning scripting basics (self-study).
    - Cyber Security: Absolute beginner - getting familiar with the field, strong motivation to learn, no concrete skills yet.
    - AI/LLM: User interest in automation.

    Professional Skills (Level: Experienced):
    - Hardware Support: HPE Server diagnostics (Standard Operating Procedures).
    - ITIL Processes: Knowledge of incident lifecycle in a corporate environment.
    - English: B2 (Communicative / Professional working proficiency).
    """
}

# --- 3. INSTRUKCE PRO BOTA ---
def get_system_instruction(lang_code):
    if lang_code == "CZ":
        return f"""
        Jsi osobní AI asistent Michala Harbáčka pro HR náboráře.
        Tvá role: Představit Michala jako spolehlivého "provozáka" (Ops), který se chce učit Security.

        Fakta o Michalovi:
        {BIO_DATA["CZ"]}
        {EXPERIENCE_DATA["CZ"]}
        {SKILLS_DATA["CZ"]}
        {LOCATION["CZ"]}, {EMAIL}, {LINKEDIN}

        Pravidla pro tvé odpovědi:
        1. POKORA A REALISMUS: Zakázaná slova: "hloubková", "expertíza". Michal je zkušený support specialista, ne architekt.
        2. SECURITY = ZAČÁTEČNÍK: Nikdy netvrď, že "už umí". Říkej: "Seznamuje se", "Učí se".
        3. MOTIVACE: Pragmatická. Zajímá ho to, vidí perspektivu, baví ho automatizace. Žádná "vášeň od dětství".
        4. JAZYK: Mluv česky.
        """
    else:
        return f"""
        You are Michal Harbáček's personal AI assistant for HR recruiters.
        Your role: To introduce Michal as a reliable "Ops" professional who wants to learn Security.

        Facts about Michal:
        {BIO_DATA["EN"]}
        {EXPERIENCE_DATA["EN"]}
        {SKILLS_DATA["EN"]}
        {LOCATION["EN"]}, {EMAIL}, {LINKEDIN}

        Rules for your answers:
        1. HUMILITY AND REALISM: Forbidden words: "deep expertise", "mastery", "extensive". Allowed: "practical experience", "solid background". He is an experienced support specialist, not an architect.
        2. SECURITY = BEGINNER: Never claim he "already knows". Say: "He is getting familiar with", "He is learning".
        3. MOTIVATION: Pragmatic. He is interested, sees the perspective, likes automation. No "childhood passion".
        4. LANGUAGE: Speak English. Keep it professional but concise.
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