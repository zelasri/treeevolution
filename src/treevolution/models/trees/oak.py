from treevolution.models.tree import Tree
from treevolution.context.context import Context
#sortie de dossier trees
import random
import math


class Oak(Tree):
    MIN_HEIGHT, MAX_HEIGHT = 5, 7
    MIN_AGE, MAX_AGE = 5, 10
    
    def __init__(self, coordinate,birth, world):
        super().__init__( coordinate,birth,world )

    def evolve(self,context:Context):
        super().evolve(context)
        if self.height< Oak.MAX_HEIGHT:
            self.height+=0.005
        #return self.height


# la santé de l’arbre est définie par sa valeur nutritionnelle actuelle ;
    @property
    def health(self):
        return self.nutrient
    @property
    def width(self):
        return self.height*0.08
    
    