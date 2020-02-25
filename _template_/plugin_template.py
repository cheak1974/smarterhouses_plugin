import core.globals
import core.plugin
import sys

# put a copy of the needed library into the lib folder and import it like:
# import plugin.myplugin.lib.myNeededLib as myLib

plugin_description =    'Persistence Object for persisting to a ordinary text file'
plugin_version =        '0.01'
plugin_author =         'Christian Kueken, Germany'
plugin_library =        'none'

plugin_parameters = {'': ''}                                # Empty here. Normally key = arg name, value = desiption


class Plugin_template(core.plugin.Plugin):                  # Name of the Class has to be eqal to filename but with capital first letter

    def __init__(self, name, friendly_name):
        super().__init__(name, friendly_name)
        self.status = 'stopped'                             # Set status to stopped. Indicate the start() method that init is complete.
                                                            # status can be init, stopped or running

    def run(self):
        # Nothing to run here. You can leave it empty if you just need methods to be called.
        # Of course you can put a sophisticated program inside here.
        # If you fire the event core.globals.bus.emit('plugin_start', core.globals.pool['plug']['PluginInstanceName'], threads=True) the run method is called and status is set to running
        # If you fire the event core.globals.bus.emit('plugin_stop', core.globals.pool['plug']['PluginInstanceName'], threads=True) the status is set to stopped
        pass


    def exampleMethod(self, **kwargs):
    # You can use Methods internally, but you can also call them with core.globals.pool['plug']['PluginInstanceName'].exampleMethod(arg1 = 'myarg')

        if self.status == 'running':
            print('Do something')

    @staticmethod
    @core.globals.bus.on('my_very_own_event')
    def reactOnOwnEvent():
    # You could also created an own event like that, that calls a method (here a static one)
        pass


    @core.globals.bus.on('my_other_very_own_event')
    def reactOnOtherOwnEvent(self, arg1):
        # You could also created an own event like that, that calls a instance method. You have to pass the Instance when emitting that event like:
        # core.globals.bus.emit('my_other_very_own_event', core.globals.pool['plug']['PluginInstanceName'], myarg1, threads=True)
        pass

