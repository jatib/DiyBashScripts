import subprocess
import pgi
pgi.require_version('Gtk', '3.0')
from pgi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):
	Gtk.Window.__init__(self, title="Separate PDF")

        self.button = Gtk.Button(label="Start")
        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)

    def on_button_clicked(self, widget):
        print("Hello World")
	subprocess.call("ls")

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

#""""
#label = Gtk.Label()
#text = "Fulle"
#label.set_text(text)
#txt = label.get_text()
#type(txt), txt
#txt == text
#""""
