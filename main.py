# import streamlit as st
# st.title("🟢INTERN")
# st.header("Full header")
# st.write("- ### My text")
# st.write("- _priya_")

# st.code("""
# #include <stdio.h>
# int main() {
   
#    printf("Hello, World!");
#    return 0;
# }

# """, language="c")
# with st.sidebar:
#     name=st.text_input("enter name")
#     st.button("click me")
#     st.write(name)
#     st.balloons()
# col1,col2,col3=st.columns(3)
# #st.metric("vinsup infotech","Python",-100)
# #st.metric("vinsup infotech","Python",+100)
# with col1:
#     st.metric("vinsup infotech","Python",-100)
# with col2:
#     st.metric("vinsup infotech","Python",+100)
# with col3:
#     st.metric("vinsup infotech","Python",50)
import streamlit as st
from streamlit_option_menu import option_menu
with st.sidebar:
    selected=option_menu(
        menu_title="Internship",
        options=["Home","About","Contact"],
        icons=["house-fill","file-person","person-lines-fill"]
    )
if selected=="Home":
    st.title("home Page")
elif selected=="Contact":
    st.title("contact Page")
elif selected=="About":
    st.title("about Page")


