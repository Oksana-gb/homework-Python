import model
import view

def button_click():
    model.export(model.pars(view.entry()))
    model.import_file()