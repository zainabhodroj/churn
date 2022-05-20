import streamlit as st


# Streamlit Style Settings
def webapp_style():
    hide_streamlit_style = """
                <style>
                    section.e1fqkh3o0 > .css-hby737 {
                                background-color: #faebd7;
                                }
                    a:link {
                            background-color: white;
                            text-decoration: underline;
                            }
                    h1 {
                        background-color: #faebd7;
                        }
                    #MainMenu {
                                visibility: none;
                                }
                    div.stButton > button:first-child{
                            background-color: #faebd7;
                            box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);
                            }
                    footer {
                            visibility: hidden;
                            }
                    footer:after {
                                content:'Made by Zainab Hodroj'; 
                                visibility: visible;
                                display: block;
                                position: relative;
                                text-align: center;
                                padding: 15px;
                                top: 2px;
                                }
    
                </style>
                """
    markdown = st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    return markdown
