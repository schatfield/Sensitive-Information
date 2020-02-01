# Create a class to represent a patient of a doctor's office. The Patient class will accept the following information during initialization

# Social security number

# Date of birth
# Health insurance account number
# First name
# Last name
# Address
# The first three properties should be read-only. First name and last name should not be exposed as properties at all, but instead expose a calculated property of full_name. Address should have a getter and setter.

# cashew = Patient(
#     "097-23-1003", "08/13/92", "7001294103",
#     "Daniela", "Agnoletti", "500 Infinity Way"
# )

# # This should not change the state of the object
# cashew.social_security_number = "838-31-2256"

# # Neither should this
# cashew.date_of_birth = "01-30-90"

# # But printing either of them should work
# print(cashew.social_security_number)   # "097-23-1003"

# # These two statements should output nothing
# print(cashew.first_name)
# print(cashew.last_name)

# # But this should output the full name
# print(cashew.full_name)   # "Daniela Agnoletti"

class Patient:
    def __init__(self, ssn, dob, health_in, first_name, last_name, address):
        self.__ssn = ssn
        self.__dob = dob
        self.__health_in = health_in
        self.__first_name = first_name
        self.__last_name = last_name
        self.__address = address

    # getters for first 3 properties. define a function that gets the ssn and returns a private version of ssn (.__ssn). NO setter because this should never be set, it is read only.

    @property
    def ssn(self):
        return self.__ssn
    @property
    def dob(self):
        return self.__dob
    @property
    def health_in(self):
        return self.__health_in

# first name and last name should not be exposed as properties at all, but instead expose a calculated property of full_name.
    @property
    def full_name(self):
        return f'{self.__first_name} {self.__last_name}'


#  Address should have a getter and setter


    @property
    def address(self):
        return self.__address
    
    # address is the value being passed in, .__address is the property from the init
    # setter SET AND STORE values
    @address.setter
    def address(self, address):
        if type(address) is str:
            self.__address = address
        else:
            raise TypeError('PLease enter a string for the address becaue I HATE NUMBERS')


eddy = Patient("097-23-1003", "08/13/92", "7001294103",
    "Daniela", "Agnoletti", "500 Infinity Way")
print(eddy.ssn)

    
      

