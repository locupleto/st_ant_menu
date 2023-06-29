from st_ant_menu import st_ant_menu

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

keys = ["sub1","sub2","sub4","g1","g2","3","4","5","6","9","10","11","12","13","14","grp"]
menu_data = [
        {
        "key": "sub1",
        "label": "Navigation One",
        "icon": "fa-sharp fa-light fa-circle-info",  # FontAwesome icon
        "children": [
            {
                "key": "g1",
                "label": "<b>Item 1</b>",
                "icon": "fa-ambulance",  # FontAwesome icon
                "children": [
                    {"key": "1", "label": "Option 1", "icon": "fa-sharp fa-light fa-dolphin"},  # FontAwesome icon
                    {"type": "divider"},
                    {"key": "2", "label": "Option 2", "icon": None},
                ],
                "type": "group",
            },
            {
                "key": "g2",
                "label": "Item 2",
                "icon": None,
                "children": [
                    {"key": "3", "label": "Option 3", "icon": None},
                    {"key": "4", "label": "Option 4", "icon": None},
                ],
                "type": "group",
            },
        ],
    },
    {
        "key": "sub2",
        "label": "Navigation Two",
        "icon": "fa-sharp fa-regular fa-comments",
        "children": [
            {"key": "5", "label": "Option 5", "icon": None},
            {"key": "6", "label": "Option 6", "icon": None},
            {
                "key": "sub3",
                "label": "Submenu",
                "icon": None,
                "children": [
                    {"key": "7", "label": "Option 7", "icon": None},
                    {"key": "8", "label": "Option 8", "icon": None},
                ],
            },
        ],
    },
    {"type": "divider"},
    {
        "key": "sub4",
        "label": "Navigation Three",
        "icon": "fa-sharp fa-light fa-file-pen",
        "children": [
            {"key": "9", "label": "Option 9", "icon": None},
            {"key": "10", "label": "Option 10", "icon": None},
            {"key": "11", "label": "Option 11", "icon": None},
            {"key": "12", "label": "Option 12", "icon": None},
        ],
    },
    {
        "key": "grp",
        "label": "<b>Group</b>",
        "icon": None,
        "children": [
            {"key": "13", "label": "Option 13", "icon": None},
            {"key": "14", "label": "Option 14", "icon": None},
        ],
        "type": "group",
    },
]
custom_css = {"ant-menu-item-divider" : {"border-top: 10px solid red;"}}

generall_css_styling = """.ant-menu-item-divider {
    /* Add your custom styles for the divider here */
    border-top: 3px solid red !important;
  }"""


with st.sidebar:



    defaultOpenKeys = ['sub1', 'sub2']
    selected_key = st_ant_menu(menu_data, generall_css_styling=generall_css_styling, inlineIndent=24, defaultOpenKeys=defaultOpenKeys, custom_font_awesome_url="https://kit.fontawesome.com/d115db5fb4.js"
                               )


#
st.title("Basic Usage")



col_left, col_right = st.columns((1, 1))

with col_right:
    with st.expander("Menu Data"):
        st.json(menu_data)

    with st.echo():
        with col_left:
            selected_key = st_ant_menu(menu_data,key="menu1"
                                       )
            
            st.write("Return")
            st.write(selected_key)
            
st.divider()


st.title("Custom Usage")

col_left, col_right = st.columns((3, 1))

with col_right:


    defaultSelectedKeys = st.multiselect("defaultSelectedKeys",keys)
    defaultOpenKeys = st.multiselect("defaultOpenKeys",keys, disabled=False)
    multiple = st.checkbox("multiple",False)
    modus = st.selectbox("modus",["inline","horizontal"])


    with st.echo():
        with col_left:
            selected_key = st_ant_menu(menu_data,key="menu2",defaultSelectedKeys=defaultSelectedKeys,defaultOpenKeys=defaultOpenKeys,multiple=multiple,modus=modus,
            )
            
            st.write("Return")
            st.write(selected_key)



st.title("Test")

col_left, col_right = st.columns((3, 1))

with col_right:


    defaultSelectedKeys = ["1"]
    defaultOpenKeys = ["sub1"]
  

    with st.echo():
        with col_left:
            selected_key = st_ant_menu(menu_data,key="menu3",defaultSelectedKeys=defaultSelectedKeys,defaultOpenKeys=defaultOpenKeys
                                       )
            
            st.write("Return")
            st.write(selected_key)


st.title("Test")

col_left, col_right = st.columns((3, 1))

with col_right:


    defaultSelectedKeys = ["1"]
    defaultOpenKeys = ["sub1"]
  

    with st.echo():
        with col_left:
            selected_key = st_ant_menu(menu_data,key="menu5",modus="horizontal"
                                       )
            
            st.write("Return")
            st.write(selected_key)




