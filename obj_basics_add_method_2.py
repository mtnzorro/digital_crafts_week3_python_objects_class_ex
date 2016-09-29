from collections import OrderedDict

class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
        self.persons_greeted = []
        self.unique_persons = []

    def greet(self, other_person):
        print 'Hello %s, I am %s!' % (other_person.name, self.name)
        self.greeting_count += 1
        if other_person.name not in self.persons_greeted:
            self.persons_greeted.append(other_person.name)
        else:
            pass

    def print_contact_info(self):
        print "%s's email: %s, %s's phone number: %s" %(self.name, self.email, self.name, self.phone)

    def add_a_friend(self,new_friend):
        self.friends.append(new_friend)

    def num_friends(self):
        print len(self.friends)

    def __repr__(self):
        return '%s, %s, %s' % (self.name, self.email, self.phone)

    def num_unique_people_greeted(self):
        print len(self.persons_greeted)




sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-35556')
bobby = Person('Bobby', 'dan@aol.com', '495-586-35556')
sonny.greet(jordan)
jordan.greet(sonny)
jordan.greet(sonny)
jordan.greet(sonny)
jordan.greet(bobby)
jordan.greet(sonny)


print "Sonny's contact info: email : %s, phone: %s" %(sonny.email, sonny.phone)
print "Jordan's contact info: email : %s, phone: %s" %(jordan.email, jordan.phone)
sonny.print_contact_info()

jordan.friends.append(sonny)
sonny.friends.append(jordan)
sonny.add_a_friend('bobby')
sonny.num_friends()
print sonny.greeting_count
print jordan.persons_greeted

jordan.num_unique_people_greeted()
print jordan
