from firebase import firebase

firebase = firebase.FirebaseApplication("https://users-auth-1bcf7-default-rtdb.firebaseio.com/", None)

def fb_post(datos):
    leer = firebase.get('/users', '')
    """ arr = leer.values()
    for elem in arr :
        val = elem.values()

        print(datos.ci) """

    firebase.post('/users/', datos)