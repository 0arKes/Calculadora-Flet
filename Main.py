import flet as ft

def main(pg : ft.Page):
    pg.title = 'Calculadora'
    resultado = ft.Text(value='0')

    pg.add(
        ft.Row(controls=[resultado],alignment='end'),
        
            ft.Row(
            controls=
        [
            ft.ElevatedButton(text='AC'),
            ft.ElevatedButton(text='+/-'),
            ft.ElevatedButton(text='%'),
            ft.ElevatedButton(text='/'),
        ]
    ),
        ft.Row(controls=
        [
            ft.ElevatedButton(text='7'),
            ft.ElevatedButton(text='8'),
            ft.ElevatedButton(text='9'),
            ft.ElevatedButton(text='x'),
        ]
    ),
        ft.Row(controls=
        [
            ft.ElevatedButton(text='4'),
            ft.ElevatedButton(text='5'),
            ft.ElevatedButton(text='6'),
            ft.ElevatedButton(text='-'),
        ]
    ),
        ft.Row(controls=
        [
            ft.ElevatedButton(text='1'),
            ft.ElevatedButton(text='2'),
            ft.ElevatedButton(text='3'),
            ft.ElevatedButton(text='+'),
        ]
    ),
        ft.Row(controls=
        [
            ft.ElevatedButton(text='0'),
            ft.ElevatedButton(text='.'),
            ft.ElevatedButton(text='='),
        ]
    )

    )
    

ft.app(target=main)