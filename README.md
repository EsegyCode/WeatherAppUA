Instructions for convert from .py to .exe

pyinstaller --onefile --noconsole --icon=planet.ico --add-data "img/src.png;img" --add-data "img/src_ic.png;img" --add-data "img/weather.png;img" --add-data "img/box.png;img" --hidden-import=tkinter --hidden-import=requests --hidden-import=geopy --hidden-import=timezonefinder --hidden-import=translate --hidden-import=pytz --hidden-import=os --hidden-import=sys MainW.py
