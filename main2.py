from pyscript import document, display

def showPlayers(e):

    players = {
        '1.)': 'Casul',
        '2.)': 'Jimenez',
        '3.)': 'Quinto',
        '4.)': 'Vida',
        '5.)': 'Ancheta',
        '6.)': 'Chua',
        '7.)': 'Francia',
        '8.)': 'Fermocil',
        '9.)': 'Catapang',
        '10.)': 'Magday',
        '11.)': 'Sarao',
        '12.)': 'Asuncion',
        '13.)': 'Eusebio',
        '14.)': 'Mabilog',
        '15.)': 'Fernando',
        '16.)': 'Evangelio',
        '17.)': 'Moya',
        '18.)': 'Sy,C',
        '19.)': 'Battung',
        '20.)': 'Mactal',
        '21.)': 'Udono',
        '22.)': 'Buenvenida',
        '23.)': 'Fado',
        '24.)': 'Mutia',
        '25.)': 'Nazareno',
        '26.)': 'Santos',
        '27.)': 'Romero',
        '28.)': 'Sy,B',
        'stop': 'stop' 
    }
    
    document.getElementById("plist").innerText = ""
    
    for num, name in players.items():
        if num == 'stop':
            break
        else:
            display(num + " " + name, target="plist")