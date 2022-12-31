import pytube
import Actor
class Media:
    def __init__(self,type,id, name,director,IMDBscore,url,duration,casts):
        self.type=type
        self.id=id
        self.name=name
        self.director=director
        self.IMDBscore=IMDBscore
        self.url=url
        self.duration=duration
        self.casts=casts
    

    def showInfo(self):
        if(int(self.type)==0):
            print("Type: Film")
        elif(int(self.type)==1):
            print("Type: Series")
        elif(int(self.type)==2):
            print("Type: Documentary")
        elif(int(self.type)==3):
            print("Type: Clip")

        print("Id: ",self.id)
        print("Name: ",self.name)
        print("Director: ",self.director)
        print("IMDB score",self.IMDBscore)
        print("URL: ",self.url)
        print("Duration: ",self.duration)
        print("Casts:")
        for x in self.casts:
            x.show()
        


        

    def download(self):
        yt = pytube.YouTube(self.url)
        yt.streams.download()

