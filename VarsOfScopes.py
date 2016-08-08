'''
class Animal:

    state = 'living'

    def skin(self, texture):
        self.texture = texture

s = Animal.skin('scaly')
d = Animal.skin('furry')

print(s.state)
print(d.state)

print(s.texture)
print(d.texture)
'''