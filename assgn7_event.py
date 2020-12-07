import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class mainwindow:
    def __init__(self):
        Gtk.Window.__init__(self, title= "Button clicker")
        self.button= Gtk.Button(label= "Click here")
        self.button.connect("Clicked", self.button_clicked)
        self.add(self.button)
    
    def button_clicked(self, widget):
        print("Event printing")
        
win= mainwindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()