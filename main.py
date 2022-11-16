import eel

eel.init('front')


@eel.expose
def r_data(x):
    print(x)


eel.start('index.html', mode='chrome')
