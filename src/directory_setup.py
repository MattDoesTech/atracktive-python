import os
import flet as ft

def example(page):
    done = ft.Row([ft.Text(value=""),], alignment="center")
    # Open directory dialog
    def get_directory_result(e: ft.FilePickerResultEvent):
        fl_directory.value = e.path if e.path else "Cancelled!"
        fl_directory.update()

    get_directory_dialog = ft.FilePicker(on_result=get_directory_result)
    fl_directory = ft.Text(value="", color="white")

    # hide all dialogs in overlay
    page.overlay.extend([get_directory_dialog])

    done = ft.Text(value="", color="white")

    def setup_directory(e):
        complete = os.path.join(fl_directory.value, 'Complete')
        wip = os.path.join(fl_directory.value, 'WIP')
        cbu = os.path.join(fl_directory.value, 'Unmastered')
        os.mkdir(complete)
        os.mkdir(wip)
        os.mkdir(cbu)
    
        done.value = "ATRACKTIVE has begun organizing your projects! 🎉"
        done.update()
        e.control.page.update()

    page.theme = ft.Theme(color_scheme_seed='red')
    # page.bgcolor = "#1B2636"

    return ft.Column(
            width=1500,
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Row([ft.Text(value="Welcome! Select your FL Studio 'Projects' folder below, once complete ATRACKTIVE will begin organizing!", style="Medium", color="white")], alignment="center"),
                ft.Row(
            [
                ft.ElevatedButton(
                    "Select FL Studio Projects Folder",
                    icon=ft.icons.FOLDER_OPEN,
                    on_click=lambda _: get_directory_dialog.get_directory_path(),
                    disabled=page.web,
                ),
            ],
                alignment="center"
        ),
                ft.Row([fl_directory], alignment="center"),

        ft.Row(
            [
                ft.ElevatedButton(
                    "Get Started 👍",
                    on_click=(setup_directory),
                    
                ),  
        
            ],
              
                alignment="center"
        ),
        
            ft.Row([done], alignment="center"),
                # ft.Row([example.setup_directory], alignment="center"),

            ],
          
        )
    

def main(page: ft.Page):
    # page.bgcolor = "#1B2636"
    page.title = "Setup"
    page.window_width = 960
    page.window_height = 540
    
    page.add(example(page))
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
