# Streamlit Ant Design Menu Component

This custom Streamlit component allows you to easily integrate an Ant Design menu into your Streamlit application. The component is built using [Ant Design](https://ant.design/) and provides a simple interface for creating a menu with nested items and icons.

<a href="https://flucas-component-overview.streamlit.app/?preselect=7" target="_blank">
    <img src="https://img.shields.io/badge/Live%20Demo-Streamlit-red?style=for-the-badge&logo=streamlit" alt="Live Demo">
</a>

## Features

- Hierarchical menu structure
- Ant Design icons support
- Light and dark theme support
- Customizable CSS styling
- Multiple selection (experimental)
- Auto-adjusting menu height
- Click event handling

## Installation

To install this component, simply run:

```bash
pip install st_ant_menu
```

# Usage

First, import the **st_ant_menu** function from the package:
```python
from st_ant_menu import st_ant_menu
```

Then, create a menu data structure, and call st_ant_menu with the data:

    menu_data = [
    {
        "key": "1",
        "label": "Menu Item 1",
        "icon": "UserOutlined",
    },
    {
        "key": "2",
        "label": "Menu Item 2",
        "icon": "VideoCameraOutlined",
        "disabled": True
    },
    {
        "key": "3",
        "label": "Menu Item 3",
        "icon": "UploadOutlined",
        "children": [
            {
                "key": "3-1",
                "label": "Submenu Item 1",
                "icon": "BarChartOutlined",
            },
            {
                "key": "3-2",
                "label": "Submenu Item 2",
                "icon": "CloudOutlined",
            },
        ],
    },
    ]

    selected_key = st_ant_menu(menu_data)


# API

    st_ant_menu(
    menu_data: List[Dict],
    key: str = "first_menu",
    defaultValue: Optional[str] = None,
    defaultSelectedKeys: Optional[str] = None,
    defaultOpenKeys: Optional[str] = None,
    additionalHeight: int = 100,
    multiple: bool = False,
    css_styling: Optional[Dict] = None,
    theme: str = "light",
    menu_click: bool = False
    ) -> Union[str, List[str]]



Parameters

menu_data (List[Dict]): The data to be displayed in the menu. Must be a list of dictionaries that conform to the Ant Design Menu item specification. See https://ant.design/components/menu/#Menu.Item for more information.

key (str, optional): The key associated with the component. This is used to ensure that the component is rendered properly when its value changes. Defaults to "first_menu".

defaultValue (Optional[str], optional): The default value to be displayed in the component. Defaults to None.

defaultSelectedKeys (Optional[str], optional): The default selected keys in the menu. Defaults to None.
defaultOpenKeys (Optional[str], optional): The default open keys in the menu. Defaults to None.
additionalHeight (int, optional): The additional height of the menu that should be added to the Streamlit iframe height. This is used to ensure that the entire menu is visible in the Streamlit app. Defaults to 100.
multiple (bool, optional): Whether the menu allows multiple selections. (Broken) Defaults to False.
css_styling (Optional[Dict], optional): A dictionary of CSS styling to be applied to the component. Defaults to None.
theme (str, optional): The theme of the menu. Can be either "light" or "dark". Defaults to "light".
menu_click (bool, optional): Set this to True to return the list of open keys on menu click, False will only return the selected key. Defaults to False.

Returns

Union[str, List[str]]: The value of the component. If menu_click is set to True, it will return a list of open keys, otherwise it will return the selected key.
