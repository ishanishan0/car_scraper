import streamlit as st
import pandas as pd

print("Top of file")

if "input_link" not in st.session_state:
    st.session_state["input_Link"] = ""

if "mode" not in st.session_state:
    st.session_state["mode"] = "input_mode"



if st.session_state["mode"] == "input_mode":
    print("Entered input mode branch")

    def link_handler():
        st.session_state["mode"] = "output_mode"

    st.text_input("Enter AutoTrader Link", key="input_link", on_change=link_handler)

else:
    print("Entered output mode branch")
    d = {'col1': [st.session_state["input_link"], 2], 'col2': [3, 4]}
    df = pd.DataFrame(data=d)
    st.table(df)
