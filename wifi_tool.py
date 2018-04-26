from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E
import subprocess, re
import wifi_connection, wifi_connections_list


class WifiTool:

    def __init__(self, master):
        self.master = master
        master.title = WifiTool
        master.resizable(width=False, height=False)

        # List of WifiConnection objects
        self.wifi_connections_list = wifi_connections_list.WifiConnectionsList()


if __name__ == "__main__":
    root = Tk()
    wifi_tool = WifiTool(root)
    root.mainloop()

