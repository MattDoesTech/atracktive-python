import os
import flet as ft
from flet import (
    ElevatedButton,
    FilePicker,
    FilePickerResultEvent,
    Page,
    Row,
    Text,
    icons,
    Column,
    Container,
    colors,
    border,
    padding,

)
def main(page: ft.Page):
    # Open directory dialog
    def get_directory_result(e: ft.FilePickerResultEvent):
        fl_directory.value = e.path if e.path else "Cancelled!"
        fl_directory.update()

    get_directory_dialog = ft.FilePicker(on_result=get_directory_result)
    fl_directory = ft.Text()

    # hide all dialogs in overlay
    page.overlay.extend([get_directory_dialog])

    def setup_directory(e):
        complete = os.path.join(fl_directory.value, 'Complete')
        wip = os.path.join(fl_directory.value, 'WIP')
        cbu = os.path.join(fl_directory.value, 'Unmastered')
        os.mkdir(complete)
        os.mkdir(wip)
        os.mkdir(cbu)
        done = ft.Text(value=f"ATRACKTIVE has begun organizing your projects! 💪")
        page.update()
        page.add(ft.Column(width=1500,controls=[ft.Row([done], alignment="center"),],),)

    # page.bgcolor = colors.BLACK
    page.theme = ft.Theme(color_scheme_seed='red')
    # page.theme = ft.Theme(
    # color_scheme=ft.ColorScheme(
    #     primary=ft.colors.BLUE,
    #     primary_container=ft.colors.BLUE_200,
    #     on_primary=ft.colors.INDIGO_900,
#     ),
# )
    page.add(
        ft.Column(
            width=1500,
            controls=[
                ft.Row([ft.Text(value="Welcome! Select your FL Studio 'Projects' folder below, once complete ATRACKTIVE will begin organizing!", style="Medium")], alignment="center"),
                        ft.Row([ft.Text(value="")]),

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
                    on_click=setup_directory,
                    
                    
                ),
            
            ],
                alignment="center"
        ),
              
            ],
        ),
    )

    page.title = "ATRACKTIVE"
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.SETTINGS, label="Setup"),
            ft.NavigationDestination(icon=ft.icons.NOTES, label="Notes"),
            ft.NavigationDestination(
                icon=ft.icons.BAR_CHART_OUTLINED,
                selected_icon=ft.icons.BAR_CHART_OUTLINED,
                label="Stats",
            ),
        ]
    )
    page.add()


ft.app(target=main)