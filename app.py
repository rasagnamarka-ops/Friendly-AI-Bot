import streamlit as st
import ollama

st.set_page_config(
    page_title="Friendly AI Bot",
    page_icon="🤖",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #080b18, #111a35, #080b18);
    color: white;
}

.block-container {
    max-width: 850px;
    padding-top: 50px;
}

.header {
    text-align: center;
    padding: 35px;
    border-radius: 25px;
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.15);
    box-shadow: 0 15px 50px rgba(0,0,0,0.4);
    margin-bottom: 30px;
}

.robot {
    font-size: 60px;
}

.title {
    font-size: 42px;
    font-weight: bold;
    color: #8b7cff;
}

.subtitle {
    color: #b8bfd8;
    font-size: 16px;
}

.status {
    display: inline-block;
    margin-top: 15px;
    padding: 7px 15px;
    border-radius: 20px;
    color: #5cff9d;
    background: rgba(50,220,140,0.1);
    border: 1px solid rgba(50,220,140,0.3);
}

.response {
    margin-top: 30px;
    padding: 25px;
    border-radius: 20px;
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(255,255,255,0.15);
    line-height: 1.8;
}

.response-title {
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 15px;
}

.stButton button {
    width: 220px;
    height: 50px;
    border-radius: 15px;
    border: none;
    background: linear-gradient(135deg, #695cff, #3cbfff);
    color: white;
    font-size: 16px;
    font-weight: bold;
}

.stButton button:hover {
    transform: scale(1.03);
}

.footer {
    text-align: center;
    color: #777f9c;
    margin-top: 30px;
    font-size: 13px;
}
</style>
""", unsafe_allow_html=True)


st.markdown("""
<div class="header">
    <div class="robot">🤖</div>
    <div class="title">Friendly AI Bot</div>
    <div class="subtitle">
        Ask anything. Get intelligent and helpful answers.
    </div>
    <div class="status">● AI Assistant Online</div>
</div>
""", unsafe_allow_html=True)


question = st.text_input(
    "💬 Your Question",
    placeholder="Type your question here..."
)


if st.button("✨ Ask AI"):

    if not question.strip():

        st.warning("⚠️ Please enter a question first.")

    else:

        try:

            with st.spinner("🤔 Thinking..."):

                response = ollama.chat(
                    model="llama3.2",
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are a friendly AI bot. "
                                "Answer questions clearly, helpfully "
                                "and informatively."
                            )
                        },
                        {
                            "role": "user",
                            "content": question
                        }
                    ]
                )

            answer = response["message"]["content"]

            st.markdown(
                f"""
                <div class="response">
                    <div class="response-title">
                        🤖 AI Response
                    </div>
                    {answer}
                </div>
                """,
                unsafe_allow_html=True
            )

        except Exception as e:

            st.error(
                "❌ Ollama connection error. "
                "Make sure Ollama is running and llama3.2 is installed."
            )

            st.code(str(e))


st.markdown("""
<div class="footer">
    Powered by Ollama • Llama 3.2
</div>
""", unsafe_allow_html=True)