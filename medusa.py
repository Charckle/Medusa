from infi.systray import SysTrayIcon
import subprocess
import webbrowser

def about(systray):
    print("Medusa is a quick app launcher, which currently has not an implemented way to add program withought programing. Will do it in the future, if it comes to it.")

def start_batch(batch_name): 
    subprocess.call([batch_name])
    
#if the file requires the creation and reading of files, it will do it all in the medusa folder, beware!
def start_python(script_path):
    subprocess.call(["python", script_path])

def open_webpage(web_page):
    webbrowser.open(web_page, new=0, autoraise=True)

def first_program(systray):
    start_batch(r'banana.bat')

def second_program(systray):
    start_python(r"C:\Users\andrej\Python_projects_win\WikiSearch\app.py")

menu_options = (("Run batch file", None, first_program),
                ("Run python script", None, second_program),
                ("Run webpage", None, lambda: open_webpage("http://www.google.com")),
                ("Submenu test", None, (('First item', "simon.ico", about),
                                        ('Second item', "simon.ico", about))),
                ("About ", None, about),
                )

systray = SysTrayIcon("blk.ico", "Medusa - App menu", menu_options, default_menu_index=1)
systray.start()