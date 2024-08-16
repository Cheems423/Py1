class Emplooyee:

    used_codes=set()

    def __init__(self, code, name, age, salary):
        if code in Emplooyee.used_codes:
            raise ValueError('Trùng mã')
        self.code=code
        self.name=name
        self.age=age
        self.salary=salary
        Emplooyee.used_codes.add(code)

    def income(self):
        ic=self.salary*12*0.9
        return ic
    
    def display(self):
        print(f'Mã số: {self.code}, Tên: {self.name}, Tuổi: {self.age}, Lương: {self.salary:.2f}, Thu nhập năm: {self.income():.2f}')

    def increaseSalary(self, amount):
        if amount>0:
            self.salary+=amount

    def decreaseSalary(self, amount):
        if amount>0 and amount<=self.salary*0.2:
            self.salary-=amount

    @staticmethod
    def reset_codes():
        Emplooyee.used_codes.clear()