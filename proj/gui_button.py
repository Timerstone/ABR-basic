import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MainWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="Button Test")
		
		self.button = Gtk.Button(label="Click Here")
		self.button.connect("clicked", self.button_clicked)
		self.add(self.button)
		
	def button_clicked(self, widget):
		print("Hello there")
		
window = MainWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()