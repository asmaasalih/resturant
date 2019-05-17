class Meal:
    def __init__(self,id,name,photo_url,details,price):
        self.id = id
        self.name = name
        self.photo_url = photo_url
        self.details = details
        self.price = price

meal_list = []
orders_list = []

class Customer:
    def get_all(self):
        return meal_list

    def get_meal_by_id(self, id):
        result = None
        for meal in meal_list:
            if meal.id == id:
                result = meal
                break
        return result

    def add_meal(self,id):
        meal = self.get_meal_by_id(id)
        orders_list.append(meal)


class Admin:
    def add_new_meal(self,meal):
        meal_list.append(meal)
        return meal_list

    def get_orders(self):
        return orders_list

    def get_by_id(self,id):
        result = None
        for meal in orders_list:
            if meal.id == id:
                result = meal
                break
        return result

    def update(self,id,fields):
        meal = self.get_by_id(id)
        meal.name = fields['name']
        meal.photo_url = fields['photo_url']
        meal.details = fields['details']
        meal.price = fields['price']
        return meal

    def delete(self,id):
        meal = self.get_by_id(id)
        meal_list.remove(meal)
        return orders_list



meal1 = Meal(id=1,
         name='Lasagna Roll',
         photo_url='https://thestayathomechef.com/wp-content/uploads/2017/08/Most-Amazing-Lasagna-4-e1503516670834.jpg',
          details='Homemade Lasagna',
         price='$40')
meal2 = Meal(id=2,
         name='pasta',
         photo_url='https://food.fnr.sndimg.com/content/dam/images/food/fullset/2019/1/07/0/JE401_Giadas-Pasta-with-Creamy-White-Beans_s4x3.jpg.rend.hgtvcom.826.620.suffix/1546886427856.jpeg',
         details='Pasta with Creamy White Beans Recipe',
         price='$30')

A = Admin()
A.add_new_meal(meal1)
A.add_new_meal(meal2)
C = Customer()
print(C.get_all())
C.add_meal(1)
print(A.get_orders())
A.delete(1)
print(C.get_all())
fields = {
    'name':'Lasagna Roll',
    'photo_url':'https://thestayathomechef.com/wp-content/uploads/2017/08/Most-Amazing-Lasagna-4-e1503516670834.jpg',
    'details':'Homemade Lasagna',
    'price':'$40'
}
A.update(1,fields)
print(C.get_meal_by_id(1))
