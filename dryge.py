import random

class Human:
    def __init__(self, name="Human", job=None, home=None, car=None,):
        self.cat = cat()
        self.name = name
        self.home = home
        self.job = job
        self.car = car
        self.money = 100
        self.gladness = 50
        self.satiety = 50

    def get_home(self):
        self.home = House()
    def cat(self):
        self.cat = cat()
    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.cat.satiety >=100:
                self.cat.satiety = 100
                return
            if self.satiety >=100:
                self.satiety = 100
                return
            self.cat.satiety += 10
            self.cat.gladness += 10
            self.satiety += 5
            self.home.food -=10

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        if manage == "fuel":
            print("I bought fuel")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("I bought food")
            self.money -= 50
            self.home.food += 50
        elif manage == "eggs":
            print("Holy Eggs! Delicious!")
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

    def chill(self):
        self.gladness += 10
        self.home.mess += 5
        a = random.randint(1,2)
        if a == 1:
            self.cat.play()
            print('Пограюсь з котом')
            self.gladness += 7
        if a == 2:
            pass

    def clean_house(self):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def day_index(self, day):
        day = f"Today the {day} of {self.name}`s life!"
        print(f"{day:=^50}","\n")

        human_index = self.name + "`s indexes"
        print(f"{human_index:=^50}","\n")
        print(f"Money - {self.money}")
        print(f"Satiety - {self.satiety}")
        print(f"Gladness - {self.gladness}")

        home_index = "Home index"
        print(f"{home_index:=^50}", "\n")
        print(f"Food - {self.home.food}")
        print(f"Mess - {self.home.mess}")

        car_index = f"{self.car.brand} car indexes"
        print(f"{car_index:=^50}","\n")
        print(f"Fuel - {self.car.fuel}")
        print(f"Strength - {self.car.strength}")

        cat_index = self.cat.name + "`s indexes"
        print(f"{cat_index:=^50}", "\n")
        print(f"Satiety - {self.cat.satiety}")
        print(f"Gladness - {self.cat.gladness}")
    def is_alive(self):
        if self.gladness < 0:
            print("Depression...")
            return False
        if self.satiety < 0:
            print("Dead...")
            return False
        if self.money < -500:
            print("Bankrupt...")
            return False
        if self.cat == False:
            print('Кіт помер, він теж помер бо цього не витримав')


    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print("Settled in the house!")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"I bought a car {self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"I don`t have a job, going to get a job {self.job.job} with salary {self.job.salary}")
        self.day_index(day)

        dice = random.randint(1, 4)
        if self.satiety < 20 or self.cat.satiety < 20:
            print("I`ll go to eat! і покормлю кота")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print("I want to chill, but there is so much mess...\nSo I will clean the house")
                self.clean_house()
            else:
                print("Let`s chill!")
                self.chill()
        elif self.money < 0:
            print("Start working!")
            self.work()
        elif self.car.strength < 15:
            print("i need to repair my car")
            self.to_repair()
        elif dice == 1:
            print("Let`s chill!")
            self.chill()
        elif dice == 2:
            print("Start working!")
            self.work()
        elif dice == 3:
            print("I want to clear my house")
            self.clean_house()
        elif dice == 4:
            print("Time to treats!")
            self.shopping(manage="eggs")

brands_of_car = {
    "BMW":{"fuel":100, "strength":100, "consumption":6},
    "Lada":{"fuel":50, "strength": 40, "consumption":10},
    "Volvo":{"fuel":70, "strength":150, "consumption":8},
    "Ferrari":{"fuel":80, "strength":120, "consumption":14}
}

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The car cannot move")
            return False

class House:
    def __init__(self):
        self.mess = 0
        self.food = 0

job_list = {
    "Java Developer":{"salary":50, "gladness_less":10},
    "Python Developer":{"salary":40, "gladness_less":3},
    "C++ Developer":{"salary":45, "gladness_less":25},
    "Ruby Developer":{"salary":70, "gladness_less":1}
}

class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]

class cat:
        def __init__(self, name='Cat'):
                self.name = name
                self.gladness = 50
                self.satiety = 50

        def sleep(self):
            self.gladness += 20
            self.satiety -= 5
        def play(self):
            self.satiety -= 1
            self.gladness += 30

        def is_alive(self):
            if self.gladness < 0:
                print('У кота депрессія (я хз як)')
                return False
            elif self.satiety < 0:
                print('Хозяїн падла не зміг мене покормити')
                return False

        def live(self):
            if self.is_alive() == False:
                return False
            dice = random.randint(1,2)
            if dice == 1:
                print('Коти вміють спати')
                self.sleep()
            else:
                print('Кіт грається а чо і ні')
                self.play()
ivan = Human(name="Ivan")
Lion = cat(name='Lion')

for day in range(1, 8):
    if ivan.live(day) == False or Lion.live():
        break