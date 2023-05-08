import { Menu } from "antd";
import { MenuProps } from "antd/lib/menu";
import React, { useEffect, useState } from "react";
import {
  ComponentProps,
  Streamlit,
  withStreamlitConnection,
} from "streamlit-component-lib";
import * as AllIcons from "@ant-design/icons";
import { ComponentType } from "react";


// Create a mapping of all available Ant Design icons
const Icons: Record<string, ComponentType<any>> = {};
Object.keys(AllIcons).forEach((key) => {
  Icons[key as keyof typeof AllIcons] = AllIcons[key as keyof typeof AllIcons] as ComponentType<any>;
});


interface MenuItem {
  key: string;
  label: string | null;
  icon?: React.ReactNode;
  children?: MenuItem[];
  type?: "group" | "divider" | null;
  disabled?: boolean;
}

// // /**
//  * Recursively parse a hierarchical list of menu items into the expected format.
//  * @param data The raw menu data to be parsed
//  * @returns An array of MenuItem objects
//  */
function parseMenuItems(data: any[], iconSize: string): MenuItem[] {
  return data.map((item: any) => {
    const menuItem: MenuItem = {
      key: item.key,
      label: item.label === null ? null : "",
      icon: undefined,
      children: item.children ? parseMenuItems(item.children, iconSize) : undefined,
      type: item.type || undefined,
      disabled: item.disabled ? true : false,
    };
    if (item.icon) {
      try {
        const Icon = Icons[item.icon];
        if (Icon) {
          menuItem.icon = React.createElement(Icon, {
            style: { fontSize: iconSize }
          });
        }
      } catch (error) {
        console.warn(`Failed to create icon for "${item.icon}":`, error);
      }
    }
    if (item.label && item.label !== null) {
      if (item.label.match(/<(.*?)>/)) {
        menuItem.label = (
          <span
            dangerouslySetInnerHTML={{ __html: item.label }}
          ></span>
        ) as unknown as string;
      } else {
        menuItem.label = item.label as string;
      }
    }
    return menuItem;
  });
}

/**
 * Get the height of the menu component, taking into account any additional height specified by the user.
 * @returns The total height of the menu, in pixels
 */
function get_height_menu() {
  var menu_array = Array.from(document.getElementsByClassName("ant-menu"));
  var menu_height = 0;
  menu_array.forEach((element) => {
    var height = (element as HTMLElement).offsetHeight;

    //if height is an integer return it
    if (height) {
      //test integer
      if (height % 1 === 0) {
        menu_height = height;
      }
    }
  });

  menu_height = menu_height + 150;

  return menu_height;
}

/**
 * A React component that renders an Ant Design menu based on the provided menu data.
 */
const MenuComponent = (props: ComponentProps) => {
  const { menu_data, key, defaultSelectedKeys, defaultOpenKeys, additionalHeight, multiple, css_styling, theme,menu_click, iconSize,modus,generall_css_styling} = props.args;
  const [openKeys, setOpenKeys] = useState<string[]>([]);
  const [selectedKeys, setSelectedKeys] = useState<string[]>([]);
  const rootSubmenuKeys = menu_data.map((item: any) => item.key);

 // Set the height of the Streamlit iframe to match the height of the menu
 useEffect(() => {
  const height = get_height_menu() + additionalHeight;
  Streamlit.setFrameHeight(parseInt(`${height}`, 10));
}, []);

  const onOpenChange: MenuProps['onOpenChange'] = (keys) => {
    const latestOpenKey = keys.find((key) => openKeys.indexOf(key) === -1);
    if (rootSubmenuKeys.indexOf(latestOpenKey!) === -1) {
      setOpenKeys(keys);
      setTimeout(() => {
        var height = get_height_menu()
        Streamlit.setFrameHeight(height + additionalHeight);
      }, 300);
    } else {
      if (menu_click == true) {
      Streamlit.setComponentValue(keys);
      }
      setOpenKeys(latestOpenKey ? [latestOpenKey] : []);
  
      setTimeout(() => {
        var height = get_height_menu()
        Streamlit.setFrameHeight(height + additionalHeight);
      }, 300);
    }
  };

  const onClick = ({ key }: { key: string }) => {
    if (multiple) {
      if (selectedKeys.includes(key)) {
        setSelectedKeys(selectedKeys.filter(k => k !== key));
      } else {
        setSelectedKeys([...selectedKeys, key]);
      }
    } else {
      setSelectedKeys([key]);
    }
  };
  
  useEffect(() => {
    Streamlit.setComponentValue(selectedKeys);
  }, [selectedKeys]);



  return (
    <>
      <style dangerouslySetInnerHTML={{ __html: generall_css_styling }} />
      <Menu
        id={key}
        mode={modus}
        openKeys={openKeys}
        onOpenChange={onOpenChange}
        style={{
          width: "100%",
          height: "100%",
          borderRight: 0,
          overflow: "auto",
          borderRadius: "20px",
          ...css_styling
        }}
        theme={theme}
        items={parseMenuItems(menu_data, iconSize)}
        multiple={multiple}
        defaultSelectedKeys={[defaultSelectedKeys]}
        defaultOpenKeys={[defaultOpenKeys]}
        onClick={onClick}
      />
    </>
  );
};

export default withStreamlitConnection(MenuComponent);