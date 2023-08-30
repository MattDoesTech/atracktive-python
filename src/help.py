import flet as ft

def example(page):
    

    return ft.Column(
            width=1500,
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Row([ft.Text(value="Welcome! Here you can get help with understanding how to use ATRACKTIVE.", style="Medium", color="white")], alignment="center"),

            ],
          
        )

def main(page: ft.Page):
    # page.bgcolor = "#1B2636"
    page.title = "Help"
    page.window_width = 960
    page.window_height = 540
    
    page.add(example(page))
    page.update()

if __name__ == "__main__":
    ft.app(target=main)