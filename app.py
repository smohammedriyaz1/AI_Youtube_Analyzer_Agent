from Youtube_Analyzer import build_youtube_agent
import streamlit as st
st.set_page_config(
    page_title="youtube video analyzer",
    layout="centered",
)

@st.cache_resource
def get_youtube_agent():
   return build_youtube_agent()

agent=get_youtube_agent()
st.title("🎥 AI YouTube Video Analyzer")
video=st.text_input("Enter YouTube Video URL", placeholder="https://www.youtube.com/watch?v=JkaxUblCGz0")
button=st.button("Analyze Video")

if video and button:
   with st.spinner("Analyzing video..."):
      response=agent.run(
         f"Analyze this video: {video}",
      )
      st.markdown("Analysis Of Video Report.")
      st.markdown(response.content)
      