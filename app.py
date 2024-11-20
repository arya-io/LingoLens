import streamlit as st
from textblob import TextBlob 
from deep_translator import GoogleTranslator
from language_options import lang_options

def main():
    st.set_page_config(page_title="LingoLens: Translator & Sentiment Analysis", layout="wide")
    st.title("🌐 LingoLens: Translator & Sentiment Analysis")

    # Sidebar for navigation
    st.sidebar.title("Navigation")
    activity = st.sidebar.radio("Choose an Activity", ['Translator', 'Sentiment Analysis'])
    st.sidebar.write("---")
    st.sidebar.info("🔄 Switch between **Translator** and **Sentiment Analysis** using the options above.")

    if activity == 'Translator':
        st.header("📜 Language Translator")
        col1, col2 = st.columns([2, 1])

        with col1:
            text = st.text_area('Enter a sentence to translate:', height=150)
        with col2:
            lang = st.selectbox("🌍 Choose a target language", options=list(lang_options.keys()))
            target_lang = lang_options[lang]
        
        if st.button('Translate'):
            if text:
                try:
                    translated_text = GoogleTranslator(source='auto', target=target_lang).translate(text)
                    st.success(f"🎉 **Translated Text:** {translated_text}")
                except Exception as e:
                    st.error(f"❌ Translation Error: {e}")
            else:
                st.error("⚠️ Please enter text to translate.")
    
    elif activity == 'Sentiment Analysis':
        st.header("📈 Sentiment Analysis")
        text = st.text_area('Enter a sentence for sentiment analysis:')
        
        if st.button('Analyze Sentiment'):
            if text:
                analysis = TextBlob(text).sentiment.polarity
                if analysis == 0:
                    st.warning('🤔 This is a **Neutral** Sentence.')
                elif analysis > 0:
                    st.success('😊 This is a **Positive** Sentence.')
                else:
                    st.error('😞 This is a **Negative** Sentence.')
            else:
                st.error("⚠️ Please enter text for analysis.")
    
    st.sidebar.write("---")
    st.sidebar.write("💻 **Developed with Streamlit**")

if __name__ == '__main__':
    main()
