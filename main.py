import PySimpleGUI as sg
import sys

def main():
    #tema
    sg.theme('Dark2')
    #layout
    layout = [
        [sg.Text('Data Inicial:', font=(" ", 10, 'bold'), size=(10, 0)), sg.Input()],# atribui o campo data inicial e a caixa que recebe o texto,
        [sg.Text('Data Final:', font=(" ", 10, 'bold'), size=(10, 0)), sg.Input()],  # size define o numero de caracteres permitidos
        [sg.Text('\nImportar Arquivo:', font=(" ", 12, 'bold'), size=(20, 0))],
        [sg.Input(key='IN'), sg.FileBrowse()],
        [sg.Text(size=(12,1), key='OUT')],
        [sg.Button('Ok'), sg.Button('Sair', button_color=('white', 'red'))],
        [sg.Text('#By Filipe and Samuel', font=(" ", 10, 'italic'), justification='right', size=(51,0))]

    ]

    #poe aqui o caminho do incone
    window = sg.Window('Compras Colaboradores', layout, resizable = True, icon =r'C:\Users\samue\Pictures\vendas icone.ico')

    #Para o icone aparecer na barra de tarefas
    if sys.platform.startswith('win'):
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            u'CompanyName.ProductName.SubProduct.VersionInformation')

    while True:       #Evento com Loop
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Sair': #fecha a janela no X ou no sair
            break
        if event == 'Ok':
            window['OUT'].update(values['IN'])
    window.close() #fecha a janela

#camiho do icone novamente
if __name__ == '__main__':
    icone = r'C:\Users\samue\Pictures\vendas icone.ico'
    main()