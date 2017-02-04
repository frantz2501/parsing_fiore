import os
path='/var/www/html/fiore/armes/epeedeuxmains'
for fichier in os.listdir(path):
    nom, ext=os.path.splitext(fichier)
    if fichier.endswith('.php'):
        print(fichier)
        f = open(path+'/'+fichier, 'r')
        chaine = f.read()
        f.close()
        result = chaine.replace("\n", "<p>")
        f=open(path+fichier, 'w')
        f.write(result)
        f.close()

