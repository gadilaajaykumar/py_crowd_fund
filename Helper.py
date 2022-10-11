import re


class Helper:

    # email validator
    def email_validator(self, email):
        if len(email) > 7:
            if re.match("^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$", email) is not None:
                return True
        return False

    # phoneNumber validator - 01(01245)
    def phone_number_validator(self, phoneNumber):
        if len(phoneNumber) > 7:
            if re.match("^01[01245][0-9]{8}$", phoneNumber) is not None:
                # if re.match("r'^(?:\+?44)?[07]\d{9,13}$'", phoneNumber) is not None:
                return True
        return None

    # password confirmation
    def password_confirmation(self, password, confirmPassword):
        if password == confirmPassword:
            return True
        else:
            return False

    # Not Empty String
    # def notEmpty(self, string_statement):
    #     if string_statement:
    #         return True
    #     else:
    #         return False

    # Display Data
    def display_data(self, dataCollection):
        return None

    # color function
    def color_function(self):
        return None
