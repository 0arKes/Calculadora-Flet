import flet as ft

def historico(h:list):
    with open ('Historico.txt','a') as arq:
        arq.write(f'{h}\n')

def main(pg : ft.Page):
    #paleta de cores
    c_blue = '#16213E'
    c_red = '#EB1D36'
    c_white = '#F5EDDC'
    c_lightblue = '#0F3460'
    c_lowblue = '#14427A'
    c_yellow = '#FAC213'

    #configuração da pagina
    pg.title = 'Calculadora'
    pg.window_height = 410
    pg.window_width = 355
    pg.bgcolor = ft.colors.BLACK

    resultado = ft.TextField(value='',
                             read_only=True,
                             border_color=c_white,
                             text_style=ft.TextStyle(size=30,color=c_white)
                            )

    def BT (e):
        data = e.control.data

        if data in ['1','2','3','4','5','6','7','8','9','0','*','.','%','/','-','+']:  
            resultado.value = str(resultado.value) + str(data)
            pg.update()

        if data == 'ac':
            resultado.value = ''
            pg.update()

        if data == '=':

            guardar = []
            guardar.append(resultado.value)
            historico(guardar)

            resultado.value = str(eval(resultado.value))
            print(resultado.value)
            pg.update()


    pg.add(
        ft.Container
        (
            width=340,
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
                        ft.ElevatedButton(text='AC', bgcolor=c_lightblue, color=c_red,expand=2,data='ac',on_click=BT),
                        ft.ElevatedButton(text='/', bgcolor=c_lightblue, color=c_yellow,expand=1,data='/',on_click=BT),
                        
                        #ft.ElevatedButton(text='H', bgcolor=c_lightblue, color=c_white,expand=1),

                    ], 
                ),
                    ft.Row(controls=
                    [
                        ft.ElevatedButton(text='7', bgcolor=c_lowblue, color=c_white,expand=1,data='7',on_click=BT),
                        ft.ElevatedButton(text='8', bgcolor=c_lowblue, color=c_white,expand=1,data='8',on_click=BT),
                        ft.ElevatedButton(text='9', bgcolor=c_lowblue, color=c_white,expand=1,data='9',on_click=BT),
                        ft.ElevatedButton(text='x', bgcolor=c_lightblue, color=c_yellow,expand=1,data='*',on_click=BT),
                    ],
                ),
                    ft.Row(controls=
                    [
                        ft.ElevatedButton(text='4', bgcolor=c_lowblue, color=c_white,expand=1,data='4',on_click=BT),
                        ft.ElevatedButton(text='5', bgcolor=c_lowblue, color=c_white,expand=1,data='5',on_click=BT),
                        ft.ElevatedButton(text='6', bgcolor=c_lowblue, color=c_white,expand=1,data='6',on_click=BT),
                        ft.ElevatedButton(text='-', bgcolor=c_lightblue, color=c_yellow,expand=1,data='-',on_click=BT),
                    ],
                ),
                    ft.Row(controls=
                    [
                        ft.ElevatedButton(text='1', bgcolor=c_lowblue, color=c_white,expand=1,data='1',on_click=BT),
                        ft.ElevatedButton(text='2', bgcolor=c_lowblue, color=c_white,expand=1,data='2',on_click=BT),
                        ft.ElevatedButton(text='3', bgcolor=c_lowblue, color=c_white,expand=1,data='3',on_click=BT),
                        ft.ElevatedButton(text='+', bgcolor=c_lightblue, color=c_yellow,expand=1,data='+',on_click=BT),
                    ],
                ),
                    ft.Row(controls=
                    [
                        ft.ElevatedButton(text='0', bgcolor=c_lowblue, color=c_white,expand=2,data='0',on_click=BT),
                        ft.ElevatedButton(text='.', bgcolor=c_lowblue, color=c_white,expand=1,data='.',on_click=BT),
                        ft.ElevatedButton(text='=', bgcolor=c_lightblue, color=c_yellow,expand=1, data='=',on_click=BT),
                    ],
                )
                ]
            )
        )
)

ft.app(target=main)