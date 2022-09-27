


class accounts:
    def __init__(self, f_name,l_name,email,password,school,school_ID,birthdate,school_year):
        self.f_name=f_name
        self.l_name=l_name
        self.school=school
        self.school_ID=school_ID
        self.birthdate=birthdate
        self.email=email
        self.password=password

    def fullname(self):
        return (self.f_name).capitalize()+' '+(self.l_name).capitalize()


david=accounts('henry','david','cal','208784','01/05/07')

print(david.fullname())