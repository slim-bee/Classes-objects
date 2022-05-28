class Student:
    # [assignment] Skeleton class. Add your code here
    
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks =tracks
        self.score = float(score)
        
    # Adds an instance variable 
    def change_name(self, name):
        print(name)
        # Retrieves instance variable
    def change_age(self, age):
        print(age)
        
    def add_tracks(self, tracks):
       
        self.tracks += [tracks]
        print(self.tracks)
    
    def get_score(self):
        print(self.score)



Bob = Student(name="Bob", age=26, tracks=["Food","Love", "Play"],score=20.90)

# Expected methods
Bob.change_name("Bisola Kareem")
Bob.change_age(44)
Bob.add_tracks("Sleep")
Bob.get_score()
