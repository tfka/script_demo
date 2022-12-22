import streamlit as st
from multiapp import MultiApp
from apps import script_demo,text2video_demo


app = MultiApp()
app.add_app("剧本", script_demo.app)
app.add_app("text2video", text2video_demo.app)
app.run()