import directory_setup
import flet as ft


class AppTile(ft.ListTile):
    def __init__(self, name, view, icon_name, file_name):
        super().__init__()
        self.view = view
        self.bgcolor = ft.colors.SURFACE_VARIANT
        self.title = ft.Text(name)
        self.leading = ft.Icon(icon_name)
        self.on_click = self.app_button_clicked
        self.name = name
        self.file_name = file_name

    def app_button_clicked(self, e):
        e.control.page.views.append(
            ft.View(
                controls=[
                    ft.AppBar(
                        title=ft.Text(f"{e.control.name}"),
                        actions=[
                            ft.IconButton(
                                content=ft.Image(
                                    src="github-mark.svg", width=24, height=24
                                ),
                                url=f"https://github.com/flet-dev/examples/tree/main/python/apps/studio-gallery/{self.file_name}",
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
    page.add(
        ft.ListView(
            controls=[
                AppTile(
                    name="Setup",
                    file_name="directory_setup.py",
                    view=directory_setup.example(page),
                    icon_name=ft.icons.SETTINGS,
                ),
            ]
        )
    )

    def view_pop(view):
        page.views.pop()
        top_view = page.views[0]
        page.go(top_view.route)

    page.on_view_pop = view_pop
    page.window_width = 960
    page.window_height = 540
    page.update()


ft.app(target=main, assets_dir="assets")
