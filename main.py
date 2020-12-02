import sys
from LeftRotation import LeftRotation
# Main
if __name__== "__main__":
    chaine_de_caractere=sys.argv[1]
    nb_de_rotation=sys.argv[2]
    left_rotation=LeftRotation()
    left_rotation.rotate(chaine_de_caractere,nb_de_rotation)