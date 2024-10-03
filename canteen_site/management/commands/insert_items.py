from django.core.management.base import BaseCommand
from canteen_site.models import MenuItem

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        menu_items = [
    {"title": "Double Cheese Potato Burger", "category": "Burger", "price": 45, "image_url": "assets/images/burger.jpg"},
    {"title": "Cheese Sandwich", "category": "Sandwich", "price": 45, "image_url": "assets/images/sandwich1.jpg"},
    {"title": "Veg Club Sandwich", "category": "Sandwich", "price": 60, "image_url": "assets/images/s2.jpg"},
    {"title": "Cheese Masala Sandwich", "category": "Sandwich", "price": 45, "image_url": "assets/images/sandwich2.jpg"},
    {"title": "Veg Schezuan Sandwich", "category": "Sandwich", "price": 45, "image_url": "assets/images/schez-sandwich.jpg"},
    {"title": "Masala Maggie", "category": "Maggie", "price": 25, "image_url": "assets/images/maggie.jpg"},
    {"title": "Schezuan Maggie", "category": "Maggie", "price": 30, "image_url": "assets/images/maggie-s.jpg"},
    {"title": "Veg Maggie", "category": "Maggie", "price": 30, "image_url": "assets/images/veg-maggie.jpg"},
    {"title": "Cheese Garlic Maggie", "category": "Maggie", "price": 40, "image_url": "assets/images/garlic-maggie.jpg"},
    {"title": "Cheese Veg Maggie", "category": "Maggie", "price": 45, "image_url": "assets/images/cheese-maggie.jpg"},
    {"title": "Masala Fries", "category": "Fries", "price": 35, "image_url": "assets/images/frenchfries.jpg"},
    {"title": "Schezuan Fries", "category": "Fries", "price": 45, "image_url": "assets/images/shezuan.jpg"},
    {"title": "Cheese Fries", "category": "Fries", "price": 40, "image_url": "assets/images/cheese-fries.jpg"},
    {"title": "Red Sause Pasta", "category": "Pasta", "price": 80, "image_url": "assets/images/pasta.jpg"},
    {"title": "White Sause Pasta", "category": "Pasta", "price": 80, "image_url": "assets/images/white-pasta.jpg"},
    {"title": "Milk Shakes", "category": "Beverages", "price": 35, "image_url": "assets/images/milk-shake.jpg"},
    {"title": "Hot Chocolate", "category": "Beverages", "price": 35, "image_url": "assets/images/hot-coffee.jpg"},
    {"title": "Aerated Drinks", "category": "Beverages", "price": 10, "image_url": "assets/images/Aerated-Drinks.jpg"},
    {"title": "Cold Coffee", "category": "Beverages", "price": 35, "image_url": "assets/images/cold-coffee.jpg"},
    {"title": "Coffee", "category": "Beverages", "price": 15, "image_url": "assets/images/coffee.jpg"},
    {"title": "Tea", "category": "Beverages", "price": 10, "image_url": "assets/images/tea.jpg"},
    {"title": "Chocolate Frappe", "category": "Beverages", "price": 35, "image_url": "assets/images/beverage.jpg"},
    {"title": "Veg Puff", "category": "Bakery", "price": 35, "image_url": "assets/images/puff.jpg"},
    {"title": "Paneer Puff", "category": "Bakery", "price": 15, "image_url": "assets/images/samosa.jpg"},
    {"title": "Khari", "category": "Bakery", "price": 20, "image_url": "assets/images/panner-puff.jpg"},
    {"title": "Noodle Puff", "category": "Bakery", "price": 15, "image_url": "assets/images/noodle-puff.jpg"}
    ]

        for item in menu_items:
            MenuItem.objects.create(**item)


