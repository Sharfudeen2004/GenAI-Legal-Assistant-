import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------- AUTH ----------------
from auth.login import authenticate

# ---------------- INGESTION ----------------
from classification.contract_type import classify_contract
from ingestion.extract_text import extract_text

# ---------------- LANGUAGE ----------------
from preprocessing.language_detect import detect_language

# ---------------- CLAUSES ----------------
from clauses.clause_splitter import split_clauses

# ---------------- NLP ----------------
from nlp_engine.ner import extract_entities
from nlp_engine.obligation import detect_obligation

# ---------------- RISK ----------------
from risk_engine.risk_rules import detect_risk
from risk_engine.risk_score import calculate_score

# ---------------- LLM ----------------
from llm.explain import explain_clause


# =================================================
# PAGE CONFIG
# =================================================
st.set_page_config(page_title="GenAI Legal Assistant", layout="wide")


# =================================================
# 🔥 BIG FONT STYLE (fix small text issue)
# =================================================
st.markdown("""
<style>
html, body, [class*="css"]  {
    font-size: 18px;
}

h1, h2, h3 {
    font-size: 26px !important;
}
</style>
""", unsafe_allow_html=True)


# =================================================
# TITLE
# =================================================
st.title("⚖️ GenAI Legal Assistant")
st.write("Analyze contracts • Detect risks • Get AI explanations • Visual dashboard")


# =================================================
# 🔐 LOGIN SYSTEM
# =================================================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:

    st.subheader("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authenticate(username, password):
            st.session_state.logged_in = True
            st.session_state.user = username
            st.success("Login successful ✅")
            st.rerun()
        else:
            st.error("Invalid credentials ❌")

    st.stop()


# =================================================
# SIDEBAR
# =================================================
with st.sidebar:
    st.write(f"👤 {st.session_state.user}")
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()


st.success(f"Welcome {st.session_state.user} 👋")


# =================================================
# FILE UPLOAD
# =================================================
file = st.file_uploader(
    "📤 Upload Contract (PDF / DOCX / TXT)",
    type=["pdf", "docx", "txt"]
)

if file:

    # =================================================
    # TEXT EXTRACTION (⚠️ DON'T CLEAN TEXT)
    # =================================================
    raw_text = extract_text(file)
    text = raw_text
    # ===============================
    # CONTRACT TYPE DETECTION
    # ===============================
    contract_type = classify_contract(text)

    st.success(f"📄 Contract Type: {contract_type}")


    st.success("✅ Contract text extracted")

    # =================================================
    # LANGUAGE DETECTION
    # =================================================
    lang = detect_language(text)
    st.info(f"🌐 Detected Language: {lang}")


    # =================================================
    # CLAUSE SPLIT
    # =================================================
    clauses = split_clauses(text)

    st.subheader(f"🧩 Total Clauses Found: {len(clauses)}")

    if len(clauses) == 0:
        st.error("No clauses detected ❌")
        st.stop()

    all_risks = []

    # =================================================
    # CLAUSE ANALYSIS
    # =================================================
    for i, clause in enumerate(clauses, start=1):

        with st.expander(f"📌 Clause {i}"):

            st.write(clause)

            # Clause Type
            ctype = detect_obligation(clause)
            st.write(f"**Clause Type:** {ctype}")

            # Entities
            entities = extract_entities(clause)
            if entities:
                st.write("**Entities:**", entities)

            # Risk detection
            risks = detect_risk(clause)

            if risks:
                st.markdown("### 🚨 Risks")

                for r, level in risks:
                    all_risks.append((r, level))

                    if level == "HIGH":
                        st.error(f"{r} ({level})")
                    elif level == "MEDIUM":
                        st.warning(f"{r} ({level})")
                    else:
                        st.success(f"{r} ({level})")
            else:
                st.success("No major risks")

            # =================================================
            # 🤖 ChatGPT style explanation
            # =================================================
            st.markdown("### 💬 AI Explanation")
            with st.chat_message("assistant"):
                st.write(explain_clause(clause))


    # =================================================
    # OVERALL RISK SCORE
    # =================================================
    score = calculate_score(all_risks)

    st.subheader("📊 Overall Risk Score")

    st.progress(score / 10)
    st.write(f"### 🔢 Score: {score} / 10")


    # =================================================
    # 📊 DASHBOARD CHARTS
    # =================================================
    st.subheader("📊 Risk Dashboard")

    if all_risks:

        df = pd.DataFrame(all_risks, columns=["Risk", "Level"])

        counts = df["Level"].value_counts()

        fig, ax = plt.subplots()
        counts.plot(kind="bar", ax=ax)
        ax.set_title("Risk Level Distribution")
        ax.set_ylabel("Count")

        st.pyplot(fig)

        st.write("### Risk Table")
        st.dataframe(df)

    else:
        st.success("No risks detected 🎉")

else:
    st.info("👆 Upload a contract file to start")
