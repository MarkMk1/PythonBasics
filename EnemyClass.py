'''
class Enemy:
    health = 3
    power = 2
    int = 1

    def attack(self):
        print("argh!")
        self.health -= 1

    def death(self):
        if self.health <= 0:
            print("oof!")
        else:
            print("Mm...")

enemy1 = Enemy()
enemy2 = Enemy()

enemy1.death()
enemy2.death()

def commandloop(command):
    while enemy1.health or enemy2.health > 0:
        if command is "hit enemy 1":
            enemy1.attack()
            enemy1.death()

        if input("command?") is "hit enemy 2":
            enemy2.attack()
            enemy2.death()

commandloop(input("command?"))
'''