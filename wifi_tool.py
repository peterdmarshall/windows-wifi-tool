from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E
import subprocess, re
import wifi_connection


class WifiTool:

    def __init__(self, master):
        self.master = master
        master.title = WifiTool
        master.resizable(width=False, height=False)

        self.connections_list = []

    def init_connections_list(self):
        profile_names_list = self.get_profile_names_list()
        # Create a WifiConnection object for each wifi profile in the list
        for i in range(0, len(profile_names_list)):
            self.connections_list[i] = wifi_connection.WifiConnection(profile_names_list[i])

    def update_connections_list(self):
        


    def get_profile_names_list(self):

        profile_names_list = []

        # Run the cmd command to show all profiles and capture the output as raw text
        run_cmd = subprocess.run('netsh wlan show profiles', stdout=subprocess.PIPE)
        raw_text = str(run_cmd.stdout)

        # Establish regex pattern and find all matches in the raw text
        pattern = re.compile(r":\s.*?(?=\\r)")
        profile_names_list = re.findall(pattern, raw_text)

        # Trim extra characters from each profile name
        for i in range(0, len(profile_names_list)):
            profile_names_list[i] = re.sub('[^A-Za-z0-9]+', '', profile_names_list[i])

        return profile_names_list




if __name__ == "__main__":
    root = Tk()
    wifi_tool = WifiTool(root)
    root.mainloop()

