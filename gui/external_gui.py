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
        component_table.show()
        
        # Create component name field
        self.create_component_name_entry = gtk.Entry(
            max=20
        )
        self.create_component_name_entry.set_text('HCRF_Component')
        component_table.attach(self.create_component_name_entry, 0, 6, 0, 1)
        self.create_component_name_entry.connect(
            'activate', self.component_name_entered)
        self.create_component_name_entry.show()
        
        # Create Component Button
        button = gtk.Button('Create Component')
        component_table.attach(button, 3, 6, 1, 2)
        button.show()
        
        # Create the menu widgets (Do not .show())
        self.choose_component_menu = gtk.Menu()
        
        # Currently no component lookup code is programmed, so use these fakes.
        categories = (
            {'name':'Fake Category',
             'components':(
                 {'name':'Comp A',
                  'path':'compa'},
                 {'name':'Comp B',
                  'path':'compb'},
                 {'name':'Comp C',
                  'path':'compc'},
             )},
            {'name':'Other Category',
             'components':(
                 {'name':'Comp A',
                  'path':'compa'},
                 {'name':'Comp B',
                  'path':'compb'},
                 {'name':'Comp C',
                  'path':'compc'},
             )},
        )
        
        for category in categories:
            category_item = gtk.MenuItem(category['name'])
            self.choose_component_menu.append(category_item)
            
            category_submenu = gtk.Menu()
            for component in category['components']:
                component_item = gtk.MenuItem(component['name'])
                component_item.connect(
                    'activate',
                    self.choose_component_item_response,
                    component
                )
                category_submenu.append(component_item)
                component_item.show()

            category_item.show()
            category_item.set_submenu(category_submenu)
        
        # Select Component Button
        self.choose_component_menu_button = gtk.Button('Choose a Component')
        component_table.attach(self.choose_component_menu_button,
                               0, 3, 1, 2)
        self.choose_component_menu_button.connect_object(
            'event', self.choose_component_pressed,
            self.choose_component_menu)
        self.choose_component_menu_button.show()
        
        # Append the tables to the tabs.
        notebook.append_page(component_table, gtk.Label('Test'))
        notebook.show()
        self.window.show()

    def choose_component_item_response(self, widget, data):
        '''
        '''
        print 'Data: %s' % str(data)
        self.choose_component_menu_button.set_label('Comp: %s' % data['name'])
    
    def choose_component_pressed(self, widget, event):
        '''
        '''
        if event.type == gtk.gdk.BUTTON_PRESS:
            widget.popup(None, None, None, event.button, event.time)
            # Tell calling code that we have handled this event the buck
            # stops here.
            return True
        # Tell calling code that we have not handled this event pass it on.
        return False
    
    def component_name_entered(self, widget):
        '''
        '''
        # Replace spaces with underscores.
        widget.set_text(widget.get_text().replace(' ', '_'))
    
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

