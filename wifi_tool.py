from tkinter import *
import subprocess, re
import wifi_connection, wifi_connections_list
from pathlib import Path


class WifiTool:

    def __init__(self, master):
        self.master = master
        master.title = WifiTool
        master.resizable(width=True, height=True)

        # Create or load list of WifiConnection objects
        if Path("NOT_CORRECT_PATH.xml").is_file():
            self.wifi_connections_list = wifi_connections_list.WifiConnectionsList("save_data.xml")
        else:
            self.wifi_connections_list = wifi_connections_list.WifiConnectionsList()

        self.draw_gui()

    def draw_gui(self):
        self.wifi_connections_list.update_connections_list()
        listbox = Listbox(self.master)
        for i in range(0, len(self.wifi_connections_list.connections_list) - 1):
            listbox.insert(i, self.wifi_connections_list.connections_list[i].connection_name)

        listbox.grid()


    def quit(self):
        sys.exit()


if __name__ == "__main__":
    root = Tk()
    wifi_tool = WifiTool(root)
    root.mainloop()

