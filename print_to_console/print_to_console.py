import core.globals
import core.plugin
import sys


sys.path.append(sys.path[0] + './/plugin//print_to_console//lib')
# import your Library, here are no libraries needed

plugin_description =    'Persistence Object for persisting to a ordinary text file'
plugin_version =        '0.01'
plugin_author =         'Christian Kueken, Germany'
plugin_library =        'none'

plugin_parameters = {'': ''}  # Empty here. Normally key = arg name, value = desiption


class Print_to_console(core.plugin.Plugin):

    def __init__(self, name, friendly_name):

        super().__init__(name, friendly_name)
        self.status = 'stopped'                             # Set status to stopped. Indicate the start() method that init is complete.

    def run(self):
        # Nothing to run here
        pass

    def print_to_console(self, Message):

        if self.status == 'running':
            print('MESSAGE FROM PLUGIN: ' + Message)
