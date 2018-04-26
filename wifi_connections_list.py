import wifi_connection
import subprocess, re
import xml.etree.ElementTree as Et
from xml.etree.ElementTree import Element, SubElement, ElementTree


class WifiConnectionsList:

    def __init__(self, save_data=None):

        if save_data is not None:
            try:
                self.connections_list = []
                self.load_save_data(save_data)
            except Et.ParseError:
                # Create connections list
                self.connections_list = []

                # Get current list of profile names
                profile_names_list = self.get_profile_names_list()

                # Create a WifiConnection object for each wifi profile in the list
                for i in range(0, len(profile_names_list) - 1):
                    self.connections_list[i] = wifi_connection.WifiConnection(profile_names_list[i])

        else:
            # Create connections list
            self.connections_list = []

            # Get current list of profile names
            profile_names_list = self.get_profile_names_list()

            # Create a WifiConnection object for each wifi profile in the list
            for i in range(0, len(profile_names_list)):
                self.connections_list.append(wifi_connection.WifiConnection(profile_names_list[i]))

    def update_connections_list(self):
        # Get current list of profile names
        profile_names_list = self.get_profile_names_list()

        # Check that each WifiConnection object still needs to exist and delete if they do not
        for WifiConnection in self.connections_list:
            if WifiConnection.connection_name not in profile_names_list:
                self.connections_list.remove(WifiConnection)

    def delete_connection(self, wifi_connection_index):
        # Call delete method to run delete command for the object
        self.connections_list[wifi_connection_index].delete_connection()
        self.connections_list.remove(self.connections_list[wifi_connection_index])

    def get_profile_names_list(self):
        # Run the command to show all profiles and capture the output as raw text
        run_cmd = subprocess.run('netsh wlan show profiles', stdout=subprocess.PIPE)
        raw_text = str(run_cmd.stdout)

        # Establish regex pattern and find all matches in the raw text
        pattern = re.compile(r":\s.*?(?=\\r)")
        profile_names_list = re.findall(pattern, raw_text)

        # Trim extra characters from each profile name
        for i in range(0, len(profile_names_list)):
            profile_names_list[i] = re.sub('[^A-Za-z0-9]+', '', profile_names_list[i])

        return profile_names_list

    def load_save_data(self, save_data):
        tree = Et.parse(save_data)
        wifi_connections_file = tree.getroot()
        connections_count = int(wifi_connections_file.find('connections_count').text)
        all_connections = wifi_connections_file.findall('connection')
        for i in range(0, connections_count - 1):
            self.connections_list = wifi_connection.WifiConnection(all_connections[i].text,
                                                                   all_connections[i].get('priority').text,
                                                                   all_connections[i].get('auto_connect').text)

    def create_save_data(self):
        # Create XML file to store data for
        wifi_connections_file = Element('wifi_tools_save_data')
        wifi_connections_file.set('version', '1.0')
        SubElement(wifi_connections_file, 'connections_count').text(Et.tostring(len(self.connections_list)))

        wifi_connections = SubElement(wifi_connections_file, 'connections_list')
        for i in self.connections_list:
            connection = SubElement(wifi_connections, 'connection').text(i.connection_name)
            SubElement(connection, 'priority').text(i.connection_priority)
            SubElement(connection, 'autoconnect').text(i.auto_connect)

        tree = ElementTree(wifi_connections_file)
        tree.write("save_data.xml")




