from kivy.app import App
from kivy.uix.label import Label
from random import randint
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

str_be = 1
min_p = 40
max_p = 60
is_repeat = False


def change_text(label, period, new_text):
    old_text, label.text = label.text, new_text
    Clock.schedule_once(lambda _: change_text(label, period, old_text), period)


class limiter(App):
    def build(self):
        global str_be

        grlt = GridLayout(cols=2)

        start_valve_obj = TextInput(
            text="1", font_size='10sp', multiline=False)
        str_be_obj = Button(text="Строк доступно: ")
        str_be_obj.on_press = self.update
        start_timer_obj = Button(text="start timer")
        end_timer_obj = Button(text="end timer")
        start_valve_obj.bind(text=self.get_start)

        grlt.add_widget(start_valve_obj)
        grlt.add_widget(str_be_obj)
        grlt.add_widget(start_timer_obj)
        grlt.add_widget(end_timer_obj)
        start_timer_obj.on_press = self.start_timer_def
        end_timer_obj.on_press = self.stop_timer

        return grlt

    def exit_repeat(self):
        global is_repeat
        is_repeat = False

    def update(self):
        global str_be
        lbl_obj = Label(text=str(str_be))
        KMessageBox = Popup(
            title="Количество строк",
            content=lbl_obj,
            size_hint=(None, None),
            size=(300, 200))
        KMessageBox.open()

    def stop_timer(self):
        def stop_it():
            global is_repeat
            is_repeat = False

        blt = BoxLayout(orientation='vertical')
        lbl_obj = Label(text=" Вы выключаете таймер,\n если вы это сделеали случайно \n нажмите рядом с окном")
        btn_exit_obj = Button(text="exit")
        btn_exit_obj.on_press = stop_it
        blt.add_widget(lbl_obj)
        blt.add_widget(btn_exit_obj)
        KMessageBox = Popup(
            title="Предупреждение!",
            content=blt,
            size_hint=(None, None),
            size=(300, 200))

        KMessageBox.open()

    def start_timer_def(self):
        global is_repeat
        is_repeat = True

    def get_start(self, instance, value):
        global str_be
        try:
            str_be = int(value)
        except:
            str_be = 0

    def repeat(self, dt):
        global str_be, is_repeat
        if is_repeat:
            str_be += 1


appl = limiter()
appl.build()
Clock.schedule_interval(appl.repeat, randint(40, 60))
appl.run()