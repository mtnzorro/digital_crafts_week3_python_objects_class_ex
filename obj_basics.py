class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def greet(self, other_person):
        print 'Hello %s, I am %s!' % (other_person.name, self.name)

sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-35556')
sonny.greet(jordan)
jordan.greet(sonny)

print "Sonny's contact info: email : %s, phone: %s" %(sonny.email, sonny.phone)
print "Jordan's contact info: email : %s, phone: %s" %(jordan.email, jordan.phone)
