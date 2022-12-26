import view
import mod
from logger import log


@log
def start():
    view.greetings()
    while True:
        match view.show_menu():
            case 0:
                break
            case 1:
                view.show_people(mod.get_people())
            case 2:
                data = view.show_create_data()
                mod.create_data(data)
            case 3:
                view.show_people(mod.get_people())
                number, item = view.show_upd_data()
                mod.update_data(number, item)
            case 4:
                view.show_people(mod.get_people())
                num = view.show_del_data()
                mod.del_data(num)