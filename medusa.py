from infi.systray import SysTrayIcon
import subprocess

def about(systray):
    print("Medusa is a quick app launcher, which currently has not an implemented way to add program withought programing. Will do it in the future, if it comes to it.")

def start_batch(batch_name): 
    subprocess.call([batch_name])
    
def first_program(systray):
    start_batch(r'banana.bat')

menu_options = (("Run first program", None, first_program),
                ("Submenu test", None, (('First item', "simon.ico", about),
                                        ('Second item', "simon.ico", about))),
                ("About ", None, about),
                )

systray = SysTrayIcon("blk.ico", "Medusa - App menu", menu_options, default_menu_index=1)
systray.start()