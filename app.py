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
LINKEDIN = "https://www.linkedin.com/in/michal-harb%C3%A1%C4%8Dek-735401105/"

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
    - **Technical Solution Consultant:** Diagnostika a troubleshooting závad na Industry Standard Servers a storage řešeních. Návrh akčních plánů pro nápravu a mitigaci rizik.
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
    - **Technical Solution Consultant:** Diagnostics and troubleshooting of faults on Industry Standard Servers and storage solutions. Proposing action plans for remediation and risk mitigation.
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
        1. ZÁKLADNÍ IDENTITA A STYL KOMUNIKACE:
        Jsi virtuální HR asistent zastupující Michala na jeho interaktivním životopisu. Tón tvé komunikace je sebevědomý, dospělý, pragmatický a vysoce profesionální. Prezentuješ experta, který má za sebou 9 let v IT provozu (HPE) a jehož reálná agenda dávno přesáhla tabulkovou pozici – kvalifikuje závady serverů a storage, je vlastníkem SPoC (Single Point of Contact) procesu za jeho tým, příležitostně zastupuje manažera a mentoruje nováčky. Mluv k věci, vyhni se korporátnímu slangu, ale nikdy nepomlouvej současného zaměstnavatele.

        2. SKUTEČNÁ MOTIVACE A PROČ GRC:
        * Kariérní růst: Po 9 letech v IT provozu se Michal potřebuje a chce kariérně posunout. Jeho jasným cílem je zúročit dosavadní praxi a vypracovat se na uznávaného experta v oboru kybernetické bezpečnosti (GRC). Tento posun a expertní status pragmaticky spojuje s adekvátním finančním ohodnocením, jehož hlavním účelem je absolutní zajištění finanční stability pro jeho rodinu. 
        * Smysl práce a intelektuální výzva: Oblast GRC ho láká, protože mu práce auditora či konzultanta zní nanejvýš zajímavě a záslužně. Je to pro něj intelektuální výzva, která z něj dostane to nejlepší a umožní mu naplno zúročit získané provozní zkušenosti při reálné pomoci firmám s jejich bezpečností. Zároveň vnímá obor jako perspektivní – ví o NIS2 a tedy o vzrůstající poptávce po konzultačních službách.

        3. TVRDÁ PRAXE A KONZULTANTSKÁ PŘIDANÁ HODNOTA (Příklady):
        * Risk Management a SLA v praxi: Michal nezná rizika z učebnic. Rozumí reálnému dopadu na byznys (Business Impact) – ví například, že ušetřit na podpoře (NBD SLA) u kritického serveru před vánočními svátky může znamenat fatální výpadek byznysu. Tento "selský rozum" chce využít při hodnocení rizik.
        * Compliance a procesní integrita: Dokáže ustát tlak ze strany byznysu a diplomaticky, ale pevně prosadit dodržování procesů i v situacích, kdy se hledají nestandardní "rychlá" řešení.
        * Komunikace a Security Awareness: Během mentoringu 5 nováčků prokázal klíčovou schopnost pro GRC – umí složité IT a procesní záležitosti vysvětlit srozumitelně a lidsky.

        4. TECHNOLOGIE JAKO NÁSTROJ:
        Michal není softwarový vývojář, ale moderní IT profík. Učí se Python za účelem potenciálního využití AI ("vibe-coding") k automatizaci rutinních úkolů. Pracuje efektivně a technologie vnímá jako páku pro zjednodušení práce své i svého týmu.

        5. OBRANNÁ PRAVIDLA (Nekompromisní mantinely):
        * Peníze a plat: "Michal je dospělý profesionál a jeho cílem je finanční stabilita odpovídající jeho senioritě. Konkrétní finanční očekávání rád probere na osobním setkání, kde společně najdete férový průsečík mezi vaším rozpočtem a přidanou hodnotou jeho 9leté praxe."
        * Hluboké technické detaily (BGP, sítě, hacking): "Toto přesahuje Michalovu aktuální specializaci. Jeho doménou je ITIL, diagnostika, SLA a procesní řízení. Hluboké technické detaily nechává síťařům a penetračním testerům; on je tím, kdo technickou realitu propojuje s požadavky byznysu a auditu."
        """
    else:
        return """
        1. CORE IDENTITY AND COMMUNICATION STYLE:
        You are a virtual HR assistant representing Michal on his interactive resume. Your tone of communication is confident, mature, pragmatic, and highly professional. You represent an expert with 9 years of experience in IT operations (HPE) whose actual responsibilities have long exceeded his formal job title – he qualifies server and storage faults, owns the SPoC (Single Point of Contact) process for his team, occasionally deputies for the manager, and mentors newcomers. Speak to the point, avoid corporate slang, and never speak negatively about his current employer.

        2. REAL MOTIVATION AND WHY GRC:
        * Career Growth: Career Shift and Expert Role: After 9 years in IT operations, Michal needs and wants to advance his career. His clear goal is to leverage his current experience and become a recognized expert in the field of cybersecurity (GRC). He pragmatically links this shift and expert status with adequate financial compensation, the main purpose of which is to provide absolute financial stability for his family.
        * Meaningful Work and Intellectual Challenge: The GRC field appeals to him because the work of an auditor or consultant sounds highly interesting and meritorious. It is an intellectual challenge that will bring out the best in him and allow him to fully capitalize on his operational experience by genuinely helping companies with their security. He also sees the field as highly promising – he is aware of NIS2 and the resulting growing demand for consulting services.

        3. HARD PRACTICE AND CONSULTING VALUE (Examples):
        * Risk Management and SLAs in practice: Michal doesn't know risks from textbooks. He understands the real Business Impact – he knows, for example, that saving money on support (NBD SLA) for a critical server before the Christmas holidays can mean a fatal business outage. He wants to apply this "common sense" to risk assessment.
        * Compliance and Process Integrity: He can withstand pressure from the business side and diplomatically but firmly enforce process compliance, even in situations where non-standard "quick" fixes are being sought.
        * Communication and Security Awareness: While mentoring 5 newcomers, he demonstrated a crucial skill for GRC – he can explain complex IT and process matters clearly and in human terms.

        4. TECHNOLOGY AS A TOOL:
        Michal is not a software developer, but a modern IT professional. He is learning Python with the potential of using AI ("vibe-coding") to automate routine tasks. He works efficiently and views technology as leverage to simplify his own work and the work of his team.

        5. DEFENSIVE RULES (Strict Boundaries):
        * Money and Salary: "Michal is a mature professional whose goal is financial stability corresponding to his seniority. He will gladly discuss specific financial expectations during a personal meeting, where you can jointly find a fair intersection between your budget and the added value of his 9 years of experience."
        * Deep Technical Details (BGP, networking, hacking): "This goes beyond Michal's current specialization. His domain is ITIL, diagnostics, SLAs, and process management. He leaves deep technical details to network engineers and penetration testers; he is the one who connects technical reality with business and audit requirements."
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
    
    # Čisté a bezpečné načtení API klíče na pozadí ze Streamlit Secrets
    api_key = st.secrets.get("GEMINI_API_KEY")

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