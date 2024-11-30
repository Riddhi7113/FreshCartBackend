from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    monthly_budget = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    preferences = models.JSONField(default=dict, blank=True)  # Store user preferences, e.g., dietary restrictions
    points = models.IntegerField(default=0)  # For gamification

    def __str__(self):
        return self.user.username
    
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(blank=True, null=True)
    suggested_complementary_items = models.ManyToManyField('self', blank=True, symmetrical=False)

    def __str__(self):
        return self.name

class ShoppingList(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shopping_lists')
    budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    shared_with = models.ManyToManyField(User, blank=True, related_name='shared_lists')

    def total_price(self):
        return sum(item.price * item.quantity for item in self.items.all())

class ShoppingListItem(models.Model):
    list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE, related_name='items')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    checked_off = models.BooleanField(default=False)  # Whether the item has been marked as purchased

    def __str__(self):
        return f"{self.quantity}x {self.item.name} ({self.list.name})"

class Store(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=300)  # Address or coordinates
    map_image_url = models.URLField(blank=True, null=True)  # Store map image

    def __str__(self):
        return self.name

class Aisle(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='aisles')
    name = models.CharField(max_length=100)
    items = models.ManyToManyField(Item, related_name='aisles')

    def __str__(self):
        return f"{self.name} - {self.store.name}"

class Reward(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    points_required = models.IntegerField()

    def __str__(self):
        return self.name

class UserReward(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rewards')
    reward = models.ForeignKey(Reward, on_delete=models.CASCADE)
    earned_at = models.DateTimeField(auto_now_add=True)

class PurchaseHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchase_history')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    purchased_at = models.DateTimeField(auto_now_add=True)

class SpendingSummary(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='spending_summary')
    total_spent = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    category_breakdown = models.JSONField(default=dict)  # Example: {"Dairy": 50.00, "Vegetables": 30.00}

class StoreVisit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='store_visits')
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    entered_at = models.DateTimeField(auto_now_add=True)
    exited_at = models.DateTimeField(null=True, blank=True)

class VoiceCommand(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='voice_commands')
    command_text = models.CharField(max_length=300)
    executed_at = models.DateTimeField(auto_now_add=True)

