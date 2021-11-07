import PySimpleGUI as sg

sg.theme("DarkAmber")


class telapython:
    def __init__(self):
        # Tela
        layout = [
            [sg.Text('Nome'), sg.Input()],
            [sg.Text('Idade'), sg.Input()],
            [sg.Checkbox('GMAIL'), sg.Checkbox('OUTLOOK'), sg.Checkbox('YAHOO')],
            [sg.Text('e-mail: '),sg.Input()],
            [sg.Button('OK')]
        ]
        # Janela
        janela = sg.Window("Dados do Usuario").layout((layout))

        # Dados
        self.button, self.values = janela.Read()

    def Iniciar(self):
        print(self.values)


tela = telapython()
tela.Iniciar()
