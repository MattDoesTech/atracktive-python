import directory_setup
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
    UserControl,
    theme,
    Image,

)


class AppTile(ft.ListTile):
    def __init__(self, name, view, icon_name, file_name):
        super().__init__()
        self.view = view
        self.bgcolor = "#1B2636"
        self.title = ft.Text(name, color="white", size=15)
        self.leading = ft.Icon(icon_name, color="white", size=30)
        self.on_click = self.app_button_clicked
        self.name = name
        self.file_name = file_name
        

    def app_button_clicked(self, e):
        e.control.page.views.append(
            ft.View(
                bgcolor= "#1B2636",
                controls=[
                    ft.AppBar(
                        color = "white",
                        bgcolor= "#1B2636",
                        title=ft.Text(f"{e.control.name}", color="white"),
                        actions=[
                            ft.IconButton(
                                content=ft.Image(
                                    src=f"/atracktive3.png", width=100, height=100
                                ),
                                url=f"https://atracktive.app/",
                                url_target="_blank",
                            )
                        ],
                    ),
                    e.control.view,
                ],
            )
        )
        e.control.page.update()


def main(page: ft.Page):
    img = ft.Image(
    src=f"/atracktive.png",
    width=1500,
    height=250,
    # opacity=0.5,
    )
    page.add(
        ft.ListView(
            horizontal=False,
            spacing=20,
            controls=[
                AppTile(
                    name = "Setup",
                    file_name="directory_setup.py",
                    view=directory_setup.example(page),
                    icon_name=ft.icons.SETTINGS,   
                ),
                AppTile(
                    name = "Notes",
                    file_name="notes.py",
                    view=directory_setup.example(page),
                    icon_name=ft.icons.NOTE,         
                ),
                
                AppTile(
                    name = "My Producer Stats",
                    file_name="stats.py",
                    view=directory_setup.example(page),
                    icon_name=ft.icons.PIE_CHART,   
                ),
                AppTile(
                    name = "Help",
                    file_name="help.py",
                    view=directory_setup.example(page),
                    icon_name=ft.icons.HELP,
                ),
                img,
            ],
        ),
    )
    def view_pop(view):
        page.views.pop()
        top_view = page.views[0]
        page.go(top_view.route)
    
    
    page.title = "ATRACKTIVE"
    page.bgcolor = "#1B2636"    
    page.padding = 15
    page.on_view_pop = view_pop
    page.window_width = 1024
    page.window_height = 768
    # img = ft.Image(
    # src=f"/atracktive.png",
    # width=1500,
    # height=250,
    # fit=ft.ImageFit.CONTAIN,
    # )

    # page.add(ft.Column(width=1500,expand=True,
    #         alignment=ft.MainAxisAlignment.CENTER, controls=[(img)]))

    page.update()


ft.app(target=main, assets_dir="../assets")
