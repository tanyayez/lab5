def get_valid_input(input_string, valid_options):
    ''' (str, tuple) -> str
    Return a valid input from user if it is in valid_options using an
    input_string
    '''
    input_string += " ({}) ".format(", ".join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response


class Property:
    ''' class for property representation'''
    def __init__(self, square_feet='', beds='', baths='', **kwargs):
        ''' (Property, str, str, str ...) -> NoneType
        '''

        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        '''(Property) -> NoneType
        Prints the information about property
        '''
        print("PROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_baths))
        print()

    def prompt_init():
        ''' None -> dict
        Creates a dictionary with info from user
        '''
        return dict(square_feet=input("Enter the square feet: "),
                    beds=input("Enter number of bedrooms: "),
                    baths=input("Enter number of baths: "))
    prompt_init = staticmethod(prompt_init)


class Apartment(Property):
    ''' class for apartment representation'''
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony='', laundry='', **kwargs):
        '''(Apartment, str, str, ...) -> NoneType
        Creates a new apartment
        '''

        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        '''(Apartment) -> NoneType
        Prints info about apartment and property
        '''

        super().display()
        print("APARTMENT DETAILS")
        print("laundry: %s" % self.laundry)
        print("has balcony: %s" % self.balcony)

    def prompt_init():
        '''None -> dict
        Creates and return a dict with info from the user.
        '''

        parent_init = Property.prompt_init()
        laundry = get_valid_input("What laundry facilities does the property have? ",
                                  Apartment.valid_laundries)
        balcony = get_valid_input("Does the property have a balcony? ",
                                  Apartment.valid_balconies)
        parent_init.update({"laundry": laundry, "balcony": balcony})
        return parent_init
    prompt_init = staticmethod(prompt_init)


class House(Property):
    '''class for house representation'''
    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")

    def __init__(self, num_stories='', garage='', fenced='', **kwargs):
        '''(House, str, str, ...) -> NoneType
        Creates a new house
        '''
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        '''(House) -> NoneType
        Prints info about house and property
        '''
        super().display()
        print("HOUSE DETAILS")
        print("# of stories: {}".format(self.num_stories))
        print("garage: {}".format(self.garage))
        print("fenced yard: {}".format(self.fenced))

    def prompt_init():
        '''None -> dict
        Creates and return a dict with info from the user.
        '''
        parent_init = Property.prompt_init()
        fenced = get_valid_input("Is the yard fenced? ", House.valid_fenced)
        garage = get_valid_input("Is there a garage? ", House.valid_garage)
        num_stories = input("How many stories? ")
        parent_init.update({"fenced": fenced, "garage": garage,
                            "num_stories": num_stories})
        return parent_init
    prompt_init = staticmethod(prompt_init)


class Purchase:
    '''class for purchase representation '''
    def __init__(self, price='', taxes='', **kwargs):
        '''(Purchase, str, str, ...) -> NoneType
        create a new purchase
        '''

        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        ''' (Purchase)-> NoneType
        Prints the info about purchase and property
        '''

        super().display()
        print("PURCHASE DETAILS")
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))

    def prompt_init():
        ''' (None) -> dict
        Return a dict with info frm the user about purchase
        '''

        return dict(price=input("What is the selling price? "),
                    taxes=input("What are the estimated taxes? "))

    prompt_init = staticmethod(prompt_init)


class Rental:
    '''class for rental representation'''
    def __init__(self, furnished='', utilities='', rent='', **kwargs):
        '''(Purchase, str, str, ...) -> NoneType
        create a new rental
        '''

        super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        ''' (Rental)-> NoneType
        Prints the info about rental and super calss info
        '''

        super().display()
        print("RENTAL DETAILS")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(self.utilities))
        print("furnished: {}".format(self.furnished))

    def prompt_init():
        ''' (None) -> dict
        Return a dict with info frm the user about rental
        '''
        return dict(rent=input("What is the monthly rent? "),
                    utilities=input("What are the estimated utilities? "),
                    furnished=get_valid_input("Is the property furnished? ",
                                              ("yes", "no")))

    prompt_init = staticmethod(prompt_init)


class HouseRental(Rental, House):
    ''' class for Houserental combination'''
    def prompt_init():
        '''(NoneType) -> dict
        Gets info from user about house and rental and creates dict with it
        '''

        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class ApartmentRental(Rental, Apartment):
    ''' class for rental apartment combination '''
    def prompt_init():
        '''(NoneType) -> dict
        Gets info from user about apartment and rental and creates dict with it
        '''
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class ApartmentPurchase(Purchase, Apartment):
    ''' class for purchase apartment combination '''
    def prompt_init():
        '''(NoneType) -> dict
        Gets info from user about apartment and purchase and creates
        dict with it
        '''
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class HousePurchase(Purchase, House):
    ''' class for purchase house combination '''
    def prompt_init():
        '''(NoneType) -> dict
        Gets info from user about house and purchase and creates dict with it
        '''

        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class Agent:
    '''class for agent representation '''
    def __init__(self):
        '''(Agent) -> NoneType
        Creates a new Agent
        '''
        self.property_list = []

    def display_properties(self):
        '''(Agent) -> None
        Displays info about each proprty in property_list
        '''
        for property in self.property_list:
            property.display()
    type_map = {("house", "rental"): HouseRental,
                ("house", "purchase"): HousePurchase,
                ("apartment", "rental"): ApartmentRental,
                ("apartment", "purchase"): ApartmentPurchase}

    def add_property(self):
        '''(Agent) -> NoneType
        Gets info about new piece of property from user and adds
        it to property_list
        '''

        property_type = get_valid_input("What type of property? ",
                                        ("house", "apartment")).lower()
        payment_type = get_valid_input("What payment type? ",
                                       ("purchase", "rental")).lower()
        PropertyClass = self.type_map[(property_type, payment_type)]
        init_args = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init_args))

    def property_type_get(self, type_prop):
        '''(Agent, str) -> list
        Returns list of pieces of property depending on type of property given
        type_prop should be: "HouseRental", "ApartmentRental",
        "ApartmentPurchase", "HousePurchase"
        '''

        types_all = ["HouseRental", "ApartmentRental",
                     "ApartmentPurchase", "HousePurchase"]
        if type_prop in types_all:
            res = []
            for prop in self.property_list:
                if type_prop in str(type(prop)):
                    res.append(prop)
            return res
        else:
            print("Error: Wrong type_prop (watch documentation)")
            return None

    def square_compare(self, bottom_square, res_type):
        '''(Agent, num, str) -> list
        res_type should be: 'low' or 'high'
        bottom_square: square_feet that other properties should be compared to
        This method comares the square of property and return a dict of
        property compared to bottom_square
        if res_type is low the properties in res will be smaller than
        bottom_square and if res_type is high they will be larger
        '''

        res = []
        if type(bottom_square) == int:
            if res_type == 'low':
                for prop in self.property_list:
                    if int(prop.square_feet) <= bottom_square:
                        res.append(prop)
                return res
            elif res_type == 'high':
                for prop in self.property_list:
                    if int(prop.square_feet) >= bottom_square:
                        res.append(prop)
                return res
            else:
                print("Error wrong value for parameter res_type:documentation")
                return None
        else:
            print("Error wrong value for bottom_square:watch documentation")
            return None

'''
agent = Agent()
agent.add_property()
a = agent.property_list
for i  in a:
    print(type(i))
print(agent.square_compare(200, 'high'))
'''
