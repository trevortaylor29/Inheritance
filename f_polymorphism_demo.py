# This program demonstrates polymorphism.

import f_animals as animals

def main():
    
    # Create a Mammal object, a Dog object, and
    # a Cat object.
    mammal = animals.Mammal('regular animal')
    dog = animals.Dog()
    cat = animals.Cat()

    '''
    # Display information about each one.
    print('Here are some animals and')
    print('the sounds they make.')
    print('--------------------------')
    mammal.show_species()
    mammal.make_sound()

    print()

    dog.show_species()
    dog.make_sound()

    print()

    cat.show_species()
    cat.make_sound()
    '''
    show_mammal_info(mammal)
    show_mammal_info(dog)
    show_mammal_info(cat)
    show_mammal_info('Bird')

def show_mammal_info(creature):
    if isinstance(creature, animals.Mammal):

        creature.show_species()
        creature.make_sound()
    else:
        print('This is not a mammal')
# Call the main function.
main()
