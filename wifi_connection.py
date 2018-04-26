import subprocess


class WifiConnection:

    def __init__(self, connection_name, priority=None, auto_connect=None):
        if priority is None and auto_connect is None:
            self.connection_name = connection_name
            self.connection_priority = ""
            self.auto_connect = False
        else:
            self.connection_name = connection_name
            self.connection_priority = priority
            self.auto_connect = auto_connect

    def set_priority(self, connection_priority):
        self.connection_priority = connection_priority
        command = 'netsh wlan set profileorder name="' + self.connection_name + '" interface="Wi-Fi" priority="' + connection_priority + '"'
        self.run_command(command)

    def set_auto_connect(self, boolean):
        if boolean:
            command = 'netsh wlan set profileparameter name="' + self.connection_name + '" connectionmode=auto'
            self.run_command(command)
        elif not boolean:
            command = 'netsh wlan set profileparameter name="' + self.connection_name + '" connectionmode=auto'
            self.run_command(command)

    def delete_connection(self):
        command = 'netsh wlan delete profile name="' + self.connection_name + '"'
        self.run_command(command)

    def run_command(self, command):
        subprocess.run(command, shell=True)
