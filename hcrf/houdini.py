''''''

# standard
import socket
# related
# local

class HoudiniData(object):
    '''A class containing the instance of the houdini module that HCRF will use,
    any other common data involving houdini.
    '''

    def __init__(self, auto_connect=True):
        '''
        '''
        if auto_connect:
            try:
                import houxmlrpc
                self.hou = houxmlrpc.ServerProxy('http://localhost:8888').hou
            except socket.error:
                print 'No Houdini session found, using default.'
                self.hou = __import__('hou')
                self.connected = False
            else:
                self.connected = True
                print 'Houdini session found and connected.'
        else:
            self.hou = __import__('hou')
            self.connected = True

