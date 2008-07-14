#!/usr/bin/env python

'''
A gui to standardize the testing of component creation.
'''

# standard
# related
import pygtk
pygtk.require('2.0')
import gtk
# local


class ExternalGUI(object):


    def __init__(self):
        # Create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        
        # Set the window dimensions
        self.window.set_geometry_hints(min_width=400,
                                       min_height=500)

        # Set the window title
        self.window.set_title("Houdini Component Rigging Framework")

        self.window.connect("delete_event", self.delete_event)
        self.window.connect("destroy", self.destroy)

        # Sets the border width of the window.
        self.window.set_border_width(5)

        # Create the Notebook and apply its settings
        notebook = gtk.Notebook()
        notebook.set_tab_pos(gtk.POS_TOP)
        
        # Add the notebook
        self.window.add(notebook)
        
        # Create the Tables for the tabs.
        component_table = gtk.Table(16, 6, True)
        
        # Append the tables to the tabs.
        notebook.append_page(component_table, gtk.Label('Test'))
        
        # Create first button
        button = gtk.Button('Create Component')
        component_table.attach(button, 0, 3, 0, 1)
        button.show()

        component_table.show()
        notebook.show()
        self.window.show()

    def delete_event(self, widget, event, data=None):
        '''
        @return: Returns False to call L{self.destroy}
        '''
        print 'Delete Event Occured.'
        return False

    def destroy(self, widget, data=None):
        print 'Destroy Event Occured.'
        gtk.main_quit()

    def main(self):
        gtk.main()

if __name__ == "__main__":
    gui = ExternalGUI()
    gui.main()