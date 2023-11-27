class Vecteur2D:
    def __init__(self,x,y,nbr):
        self.__x = x
        self.__y = y
        self.__Nbr = nbr
    def ToString(self):
        return ("x=",self.__x ,"y=",self.__y)
    def Norm(self):
        return (self.__x**2 + self.__y**2)**0.5
    def Equais(self,other):
        if (self.__x == other.x) and (self.__y == other.y):
            return True
        else:
            return false
    def getx(self):
        return self.__x 
    def setx(self,x):
        self.__x = x
    def gety(self):
        return self.__y 
    def sety(self,y):
        self.__y = y 
    def getNbr(self):
        return self.__Nbr
    def afficherInfo(self):
        print("le vecteur1 x est :",self.__x)
        print("le vecteur2 y est :",self.__y)
        print("le numbre de vecteur est :",self.__Nbr)

class Vecteur3D(Vecteur2D):
    def __init__(self,x,y,nbr,z):
         Vecteur2D.__init__(self,x,y,nbr)
         self.__x = x
         self.__y = y
         self.__Nbr = nbr
         self.__z = z 
    def getz(self):
        self.__z 
    def setz(self,z): 
        self.__z = z
    def ToString(self):
        return ("x=",self.__x , "y=",self.__y , "z=",self.__z)
    def Norm(self):
        return ((self.__x**2)+(self.__y**2)+(self.__z**2)**(1/2))
    def Equais(self,other):
        if (self.__y == other.y) and (self.__z== other.z) and (self.__x == other.x ):
           return True
        else:
           return false
    def afficherInfo(self):
        print("le vecteur1 x est :",self.__x)
        print("le vecteur2 y est :",self.__y)
        print("le vecteur3 z est :",self.__z)
        print("le numbre de vecteur est :",self.__Nbr)

Vec1 = Vecteur2D(1,2,4)
print(Vec1.getx())
print(Vec1.gety())
print(Vec1.getNbr())
print(Vec1.Norm())
print(Vec1.ToString())
Vec1.afficherInfo()
print(Vec1.Equais())

Ve1=Vecteur3D(1,2,4,6)
print(Ve1.gety())
print(Ve1.getNbr())
print(Ve1.Norm())
print(Ve1.ToString())
print(Ve1.getNbr())
Ve1.afficherInfo()
print(Ve1.Equais())



