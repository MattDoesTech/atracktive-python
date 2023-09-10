import flet as ft
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import sqlite3
from directory_setup import Setup

class getDirectory:
    conn = sqlite3.connect('atracktive.db')
    c = conn.cursor()
    insert_query = """
        SELECT details FROM atracktive WHERE user_info = "Directory"; 
        """
    c.execute(insert_query)
    for data in c.fetchone():
        global directory
        directory = data
    conn.close()

class OnMyWatch:
    # Set the directory on watch
    # test = Setup()
    # watchDirectory = directory
    # print (watchDirectory)

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, directory, recursive = True)
        print(directory)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Event is created, you can process it now
            print("Watchdog received created event - % s." % event.src_path)
        elif event.event_type == 'modified':
            # Event is modified, you can process it now
            print("Watchdog received modified event - % s." % event.src_path)

def example(page):
      
    return ft.Column(
        width=1500,
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Row([ft.Text(value="Welcome! Here you can add notes corresponding to any project to better track your work.", style="Medium", color="white")], alignment="center"),
            ft.Row([ft.Text(value=directory, color="white")], alignment="center"),
        ],
        
        
    )



def main(page: ft.Page):
    # page.bgcolor = "#1B2636"
    page.title = "Notes"
    page.window_width = 960
    page.window_height = 540
    
    page.add(example(page))
    page.update()
    # watch = OnMyWatch()
    # watch.run()



if __name__ == "__main__":

    ft.app(target=main)

    