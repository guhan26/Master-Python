from guhan.vehcile import Vehicle, Guhan, GoodGuhan

# creating object
num1 = Vehicle('xxx','abc')
num2 = Guhan('yyy','mno')
num3 = GoodGuhan('zzz','123')


for v in [num1, num2, num3]:
    # calling drive function
    v.drive();


def perform_tasks(vehcile_object):
    vehcile_object.drive()

perform_tasks(num1)


