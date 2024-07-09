import streamlit as st
import pandas as pd

print("Top of file")

if "linklist" not in st.session_state:
    st.session_state["linklist"] = []

if "mode" not in st.session_state:
    st.session_state["mode"] = "input_mode"

if st.session_state["mode"] == "input_mode":
    print("Entered input mode branch")
    def link_handler():
        st.session_state["linklist"].append(st.session_state["input_link"])
        st.session_state["input_link"] = ""

    st.text_input("Enter Autotrader Link", key="input_link", on_change=link_handler)

    for link in st.session_state["linklist"]:
        st.write(link)

    if st.button("Submit links", type="primary"):
        print("Button pressed")
        st.session_state["mode"] = "output_mode"
        print("Output mode")
        st.rerun()

else:
    print("Entered output mode branch")
    d = {'col1': [1, 2], 'col2': [3, 4]}
    df = pd.DataFrame(data=d)
    st.table(df)
