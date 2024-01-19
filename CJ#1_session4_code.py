class Animal:
    def __init__(self, arms, legs, num_of_eyes, tail, furry):
        self.arms = arms
        self.legs = legs
        self.num_of_eyes = num_of_eyes
        self.tail = tail
        self.furry = furry
    
    def describe(self):
        print(f"this animal's arm is {self.arms} meters long")
        print(f"this animal's leg is  {self.legs} meters long")
        print(f"this animal has {self.num_of_eyes} eyes")
        if self.tail:
            print('this animal has a tail')
        else:
            print("this animal doesn't have a tail")
        if self.furry:
            print("this animal is furry")
        else:
            print("this animal isn't furry")

def ask_input():
    arms = float(input("how long is your animal's arm?"))   
    legs = float(input("how long is your animal's leg?")) 
    num_of_eyes = int(input("how many eyes does your animal have?"))
    tail = (input("does your animal has tail? yes/no:"))
    if tail == "yes":
        tail = True
    else:
        tail = False
    furry = (input("is your animal furry? yes/no:"))
    if furry == "yes":
        furry = True
    else:
        furry = False

    return Animal(arms, legs, num_of_eyes, tail, furry)

def main():
    animal = ask_input()
    animal.describe()

if __name__ == "__main__":
    main()