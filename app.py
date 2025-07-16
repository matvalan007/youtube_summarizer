import streamlit as st
from utube_summarization import summarize

st.title("YouTube Video Summarizer")

youtube_url = st.text_input("Enter YouTube Video URL", placeholder="https://www.youtube.com/watch?v=example")

if st.button("Summarize"):
    if not youtube_url.strip():
        st.warning("Please enter a valid YouTube URL.")
    else:
        try:
            with st.spinner("Summarizing…"):
                summary = summarize(youtube_url)
            st.subheader("Summary")
            st.text_area("Summarized Output", summary, height=300)
        except Exception as e:
            st.error(f"⚠️  {e}")
