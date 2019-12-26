class LeftRotation:
    def rotate(self, chaine_de_caractere, nb_de_rotation):
        l = str(chaine_de_caractere)
        n = len(l)
        d = int(nb_de_rotation)
        for i in range(n):
            print(l[(i + d) % n], end=' ')
