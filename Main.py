import flet as ft

def main(pg : ft.Page):

    pg.title = 'Calculadora'
    pg.window_height = 300
    pg.window_width = 320
    c_blue = '#16213E'
    c_red = '#EB1D36'
    c_white = '#F5EDDC'

    resultado = ft.Text(value='0')

    pg.add(
        ft.Row(controls=[resultado],alignment='end'),
        
            ft.Row(
            controls=
        [
            ft.ElevatedButton(text='AC',bgcolor=c_blue,color=c_red),
            ft.ElevatedButton(text='+/-',bgcolor=c_blue,color=c_white),
            ft.ElevatedButton(text='%',bgcolor=c_blue,color=c_white),
            ft.ElevatedButton(text='/',bgcolor=c_blue,color=c_white),
        ], 
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    ),
        ft.Row(controls=
        [
            ft.ElevatedButton(text='7',bgcolor=c_blue,color=c_white),
            ft.ElevatedButton(text='8',bgcolor=c_blue,color=c_white),
            ft.ElevatedButton(text='9',bgcolor=c_blue,color=c_white),
            ft.ElevatedButton(text='x',bgcolor=c_blue,color=c_white),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    ),
        ft.Row(controls=
        [
            ft.ElevatedButton(text='4',bgcolor=c_blue,color=c_white),
            ft.ElevatedButton(text='5',bgcolor=c_blue,color=c_white),
            ft.ElevatedButton(text='6',bgcolor=c_blue,color=c_white),
            ft.ElevatedButton(text='-',bgcolor=c_blue,color=c_white),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    ),
        ft.Row(controls=
        [
            ft.ElevatedButton(text='1',bgcolor=c_blue,color=c_white),
            ft.ElevatedButton(text='2',bgcolor=c_blue,color=c_white),
            ft.ElevatedButton(text='3',bgcolor=c_blue,color=c_white),
            ft.ElevatedButton(text='+',bgcolor=c_blue,color=c_white),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    ),
        ft.Row(controls=
        [
            ft.ElevatedButton(text='0',bgcolor=c_blue,color=c_white),
            ft.ElevatedButton(text='.',bgcolor=c_blue,color=c_white),
            ft.ElevatedButton(text='=',bgcolor=c_blue,color=c_white),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    )
    

ft.app(target=main)