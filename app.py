import streamlit as st

st.set_page_config(page_title="Ongea AI — Swahili Voice", page_icon="🎙️", layout="centered")
st.markdown("""<style>
.stApp{background:#0a0a0a;color:#f5f5f5}
.o-card{background:#1a0a0a;border:1px solid #b71c1c;border-radius:10px;padding:14px 18px;margin:8px 0;text-align:center}
</style>""", unsafe_allow_html=True)

st.markdown("# 🎙️ Ongea AI")
st.markdown("**Swahili Voice AI — Sema, Sikiliza, Elewa**")

st.info("""
**Jinsi inavyofanya kazi:**
1. 🎤 Bonyeza kitufe cha kurekodi sauti yako
2. 🤖 AI inatafsiri na kujibu kwa Kiswahili
3. 🔊 Sikiliza jibu au soma maandishi

**Matumizi bora:**
- Maswali ya afya, dawa, kilimo
- Habari za serikali na haki zako
- Msaada wa biashara na fedha
""")

st.markdown('<div class="o-card"><h2>🎤</h2><p>Rekodi sauti inapatikana katika toleo lijalo.<br><b>Sasa hivi:</b> Andika swali lako hapa chini.</p></div>',
            unsafe_allow_html=True)

st.markdown("### Au andika swali lako:")
q = st.text_area("Swali lako kwa Kiswahili:", height=100, placeholder="Mfano: Jinsi ya kupata mkopo mdogo Kenya...")

if st.button("🤖 Jibu", key="voice_btn") and q:
    import urllib.request, json
    API_KEY = st.secrets.get("GOOGLE_API_KEY") or st.secrets.get("GEMINI_API_KEY","")
    if not API_KEY:
        st.error("API key not configured")
    else:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"
        body = {"contents":[{"role":"user","parts":[{"text":q}]}],
                "systemInstruction":{"parts":[{"text":"Jibu kwa Kiswahili rahisi na fupi. Tumia sentensi fupi. Epuka maneno magumu. Jibu kama unaongea na mtu ana simu ya kawaida."}]},
                "generationConfig":{"temperature":0.3,"maxOutputTokens":300}}
        try:
            req = urllib.request.Request(url,data=json.dumps(body).encode(),
                                         headers={"Content-Type":"application/json"},method="POST")
            with urllib.request.urlopen(req,timeout=30) as r:
                ans = json.loads(r.read())["candidates"][0]["content"]["parts"][0]["text"]
            st.success("✅ Jibu:")
            st.markdown(f'<div class="o-card" style="text-align:left">{ans.replace(chr(10),"<br>")}</div>',
                        unsafe_allow_html=True)
        except Exception as e:
            st.error(f"❌ {e}")

st.markdown("---")
st.caption("🎙️ Ongea AI v1.0 | Voice features: coming soon | CC BY-NC-ND 4.0 | gabrielmahia.ai")
