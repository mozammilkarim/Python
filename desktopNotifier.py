# simple program for a notification on desktop
from win10toast import ToastNotifier
mytoast=ToastNotifier()

mytoast.show_toast(title="Mera farmaan", msg="Chala Jaa varna !!", icon_path=None, duration=5)
