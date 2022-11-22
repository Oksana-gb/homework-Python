import view
import model

def start ():
    while True:
        choice=view.menu()
        if choice == '1':
            model.create_record(model.db_main, view.data(), model.global_mapping)
            model.store_id(model.db_main, "id_list")
        elif choice == '2':
            model.read_record(model.db_main, view.number_record())
        elif choice == '3':
            model.update_record(model.db_main, view.number_record(), view.data(), model.global_mapping)
        elif choice == '4':
            model.delete_record(model.db_main, view.number_record())
        elif choice == '5':
            model.export(model.db_main, 'export.csv')
        elif choice == '6':
            model.import_dict('export.csv')
        elif choice == '7':
            model.import_without_id(model.db_main,'export_without_id.csv', model.global_mapping, model.get_id('id_list'))
            model.store_id(model.db_main, "id_list")
        elif choice == '8':
            print(model.db_main)
        elif choice == '9':
            break



