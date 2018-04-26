from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E
import subprocess, re
import wifi_connection, wifi_connections_list
from pathlib import Path


class WifiTool:

    def __init__(self, master):
        self.master = master
        master.title = WifiTool
        master.resizable(width=False, height=False)

        # Create or load list of WifiConnection objects
        if Path("save_data.xml").is_file():
            self.wifi_connections_list = wifi_connections_list.WifiConnectionsList("save_data.xml")
        else:
            self.wifi_connections_list = wifi_connections_list.WifiConnectionsList()


if __name__ == "__main__":
    root = Tk()
    wifi_tool = WifiTool(root)
    root.mainloop()

