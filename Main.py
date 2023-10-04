import flet as ft

def main(pg : ft.Page):
    #paleta de cores
    c_blue = '#16213E'
    c_red = '#EB1D36'
    c_white = '#F5EDDC'
    c_lightblue = '#0F3460'

    #configuração da pagina
    pg.title = 'Calculadora'
    pg.window_height = 410
    pg.window_width = 355
    pg.bgcolor = ft.colors.BLACK

    resultado = ft.TextField(value='0',
                             read_only=True,
                             border_color=c_white,
                             text_style=ft.TextStyle(size=30,color=c_white)
                            )

    pg.add(
        ft.Container
        (   width=340,
            height=350,
            bgcolor=c_blue,
            border_radius=ft.border_radius.all(20),
            padding=10,
            content=ft.Column(
                controls=[
                    
                    ft.Row(
                        controls=
                    [
                        resultado
                    ], 
                    ),
                    
                        ft.Row(
                        controls=
                    [
                        ft.ElevatedButton(text='AC', bgcolor=c_lightblue, color=c_red,expand=1),
                        ft.ElevatedButton(text='+/-', bgcolor=c_lightblue, color=c_white,expand=1),
                        ft.ElevatedButton(text='%', bgcolor=c_lightblue, color=c_white,expand=1),
                        ft.ElevatedButton(text='/', bgcolor=c_lightblue, color=c_white,expand=1),
                    ], 
                    #alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                    ft.Row(controls=
                    [
                        ft.ElevatedButton(text='7', bgcolor=c_lightblue, color=c_white,expand=1),
                        ft.ElevatedButton(text='8', bgcolor=c_lightblue, color=c_white,expand=1),
                        ft.ElevatedButton(text='9', bgcolor=c_lightblue, color=c_white,expand=1),
                        ft.ElevatedButton(text='x', bgcolor=c_lightblue, color=c_white,expand=1),
                    ],
                    #alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                    ft.Row(controls=
                    [
                        ft.ElevatedButton(text='4', bgcolor=c_lightblue, color=c_white,expand=1),
                        ft.ElevatedButton(text='5', bgcolor=c_lightblue, color=c_white,expand=1),
                        ft.ElevatedButton(text='6', bgcolor=c_lightblue, color=c_white,expand=1),
                        ft.ElevatedButton(text='-', bgcolor=c_lightblue, color=c_white,expand=1),
                    ],
                    #alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                    ft.Row(controls=
                    [
                        ft.ElevatedButton(text='1', bgcolor=c_lightblue, color=c_white,expand=1),
                        ft.ElevatedButton(text='2', bgcolor=c_lightblue, color=c_white,expand=1),
                        ft.ElevatedButton(text='3', bgcolor=c_lightblue, color=c_white,expand=1),
                        ft.ElevatedButton(text='+', bgcolor=c_lightblue, color=c_white,expand=1),
                    ],
                    #alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                    ft.Row(controls=
                    [
                        ft.ElevatedButton(text='0', bgcolor=c_lightblue, color=c_white,expand=2),
                        ft.ElevatedButton(text='.', bgcolor=c_lightblue, color=c_white,expand=1),
                        ft.ElevatedButton(text='=', bgcolor=c_lightblue, color=c_white,expand=1),
                    ],
                    #alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                )
                ]
            )
        )
)

ft.app(target=main)