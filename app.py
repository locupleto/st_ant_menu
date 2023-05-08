from st_ant_menu import st_ant_menu

import streamlit as st




menu_data = [
    {
        "key": "sub1",
        "label": "Navigation One",
        "icon": "MailOutlined",
        "children": [
            {
                "key": "g1",
                "label": "<b>Item 1</b>",
                "icon": None,
                "children": [
                    {"key": "1", "label": "Option 1", "icon": None},
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
        "icon": "AppstoreOutlined",
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
        "icon": "SettingOutlined",
        "children": [
            {"key": "9", "label": "Option 9", "icon": None},
            {"key": "10", "label": "Option 10", "icon": None},
            {"key": "11", "label": "Option 11", "icon": None},
            {"key": "12", "label": "Option 12", "icon": None},
        ],
    },
    {
        "key": "grp",
        "label": "Group",
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

   

    selected_key = st_ant_menu(menu_data, generall_css_styling=generall_css_styling)