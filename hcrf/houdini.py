''''''

# standard
import socket
# related
import pygtk
pygtk.require('2.0')
import gtk
# local

class HoudiniData(object):
    '''This class manages the connection to HOM, and holds references to basic
    data.
    '''

    def __init__(self, auto_connect=True):
        '''
        '''
        if auto_connect:
            self.connect()
        else:
            self._hou = __import__('hou')
        
        self.dialog_window = None
        
        # This is so WingIDE knows what some variables are.
        if 0:
            import hou
            assert isinstance(self._hou, hou)

    def check_hou(self):
        '''Check to see if the connection to hou has broken and if it has,
        fall back to the default connection.
        '''
        
        def not_handled():
            pass
        
        def broken_connection():
            message = ('The live session to Houdini has been broken but HCRF '
            'will continue to run on the Houdini HOM.')
            if self.dialog_window is not None:
                dialog = gtk.MessageDialog(
                    self.dialog_window,
                    flags=gtk.DIALOG_MODAL,
                    type=gtk.MESSAGE_WARNING,
                    buttons=gtk.BUTTONS_OK,
                    message_format=message
                )
                dialog.run()
                dialog.destroy()
            
            # The message for the CLI will probably need to be customized to
            # fit a CLI message format.
            print message
            
            self._hou = __import__('hou')
        
        connection_switch = {
            -1:broken_connection,
            0:not_handled,
            1:not_handled,
        }
        
        connection_switch[self.connection_state()]()
    
    def connect(self):
        '''Try and connect to a live houdini session.
        @return: True if the connection was successful, False otherwise.
        '''
        
        try:
            import houxmlrpc
            self._s = houxmlrpc.ServerProxy('http://localhost:8888')
            self._hou = self._s.hou
        except socket.error:
            self._hou = __import__('hou')
            print 'No Houdini session found, using default.'
            return False
        else:
            print 'Houdini session found and connected.'
            return True
    
    def connected(self):
        '''Check if there is a live connection to Houdini.
        '''
        
        connection_switch = {
            -1:False,
            0:False,
            1:True,
        }
        return connection_switch[self.connection_state()]
    
    def connection_state(self):
        '''Check the state of the houdini connection.
        @return: This function returns one of three states:
         - -1: If a live connection was broken.
         -  0: If there is no live connection.
         -  1: If a connection to a live Houdini exists.
        '''
        
        try:
            if self._hou.applicationName() == 'houdini':
                return 1
            else:
                return 0
        except socket.error, inst:
            return -1
    
    def get_hou(self):
        self.check_hou()
        return self._hou
    
    def set_dialog_window(self, window):
        '''
        '''
        self.dialog_window = window
