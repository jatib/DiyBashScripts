import pgi
pgi.require_version('Gtk', '3.0')
from pgi.repository import Gtk, Gdk

class ClipboardWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Clipboard Example")

        table = Gtk.Table(2, 2)

        self.clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
        self.entry = Gtk.Entry()
        self.image = Gtk.Image.new_from_icon_name("process-stop", Gtk.IconSize.MENU)

        button_acept_text = Gtk.Button("Aceptar")
        button_cancel_text = Gtk.Button("Cancelar")
	button_close_text = Gtk.Button("Cerrar")
        #button_copy_image = Gtk.Button("Copy Image")
        #button_paste_image = Gtk.Button("Paste Image")

        table.attach(self.entry, 0, 4, 0, 1)
        #table.attach(self.image, 0, 1, 0, 2)
        table.attach(button_acept_text, 1, 2, 1, 2)
        table.attach(button_cancel_text, 2, 3, 1, 2)
        table.attach(button_close_text, 3, 1, 1, 2)
        #table.attach(button_copy_image, 1, 2, 1, 2)
        #table.attach(button_paste_image, 2, 3, 1, 2)

        button_acept_text.connect("clicked", self.copy_text)
        button_cancel_text.connect("clicked", self.paste_text)
        button_close_text.connect("clicked", self.paste_text)
        #button_copy_image.connect("clicked", self.copy_image)
        #button_paste_image.connect("clicked", self.paste_image)

        self.add(table)

    def copy_text(self, widget):
        self.clipboard.set_text(self.entry.get_text(), -1)

    def paste_text(self, widget):
        text = self.clipboard.wait_for_text()
        if text is not None:
            self.entry.set_text(text)
        else:
            print("No text on the clipboard.")

    def copy_image(self, widget):
        if self.image.get_storage_type() == Gtk.ImageType.PIXBUF:
            self.clipboard.set_image(self.image.get_pixbuf())
        else:
            print("No image has been pasted yet.")

    def paste_image(self, widget):
        image = self.clipboard.wait_for_image()
        if image is not None:
            self.image.set_from_pixbuf(image)


win = ClipboardWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

