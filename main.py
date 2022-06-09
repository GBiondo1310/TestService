from kivy import platform
from kivy.lang import Builder
from kivy.clock import Clock
from kivymd.app import MDApp
from kivymd.uix.list import BaseListItem
from kivy.properties import StringProperty
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.list import MDList
from math import ceil
from kivy.network.urlrequest import UrlRequest
from kivy.metrics import dp
from kivy.core.window import Window
from plyer import notification, vibrator
from requests import request


Window.softinput_mode = "pan"


class TestApp(MDApp):
    server = "http://0.0.0.0:8000/"  # Se app android, cambiare con ip del pc host

    def build(self):
        self.theme_cls.material_style = "M3"
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.accent_palette = "Red"
        self.theme_cls.accent_hue = "400"
        self.theme_cls.theme_style = "Light"
        self.screen = Builder.load_file("main.kv")
        return self.screen

    def test_server(self):
        def request_ok(response, result):
            print(response, result)
            self.screen.ids.response_label.text = f"Response:\n{result}"

        def request_fail(*args):
            print(args)
            self.screen.ids.response_label.text = f"Response:\nERRORE"

        r = UrlRequest(
            self.server, on_success=request_ok, timeout=5, on_error=request_fail
        )

    def on_start(self):
        if platform == "android":
            self.start_service()

    @staticmethod
    def start_service():
        if platform == "android":
            from jnius import autoclass

            service = autoclass(
                "org.gb1310.test_service.ServiceTestServ"
            )  # Vedi buildozer.spec riga 56
            mActivity = autoclass("org.kivy.android.PythonActivity").mActivity
            service.start(mActivity, "")
            return service


app = TestApp()
app.run()
