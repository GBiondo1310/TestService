from jnius import autoclass
from time import sleep
from plyer import vibrator
from kivy.network.urlrequest import UrlRequest


PythonService = autoclass("org.kivy.android.PythonService")
PythonService.mService.setAutoRestartService(True)

while True:

    def success(*args):
        vibrator.vibrate(0.3)

    req = UrlRequest(
        "http://0.0.0.0:8000/test_service/", success, timeout=5
    )  # Se app android, cambiare con ip del pc host
    sleep(2)
