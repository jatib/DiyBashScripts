import pgi
pgi.require_version('Gtk', '3.0')
from pgi.repository import Gtk

window = Gtk.Window()
entry = Gtk.Entry()
button_ok = Gtk.Button("OK")
button_cancel = Gtk.Button("Cancel")
vbox = Gtk.VBox()
vbox.pack_start(entry)
hbox = Gtk.HBox()
hbox.pack_start(button_ok)
hbox.pack_start(button_cancel)
vbox.pack_start(hbox)
window.add(vbox)
window.show_all()

