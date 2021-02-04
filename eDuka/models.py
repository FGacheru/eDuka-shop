from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)

	def __str__(self):
		return self.name


class Product(models.Model):
	STATUS = (
		('True', 'True'),
		('False', 'False'),
	)
	name = models.CharField(max_length=200)
	price = models.FloatField()
	digital = models.BooleanField(default=False,null=True, blank=True)
	image = models.ImageField(null=True, blank=True)
	posted_date= models.DateTimeField(auto_now_add=True)
	category = models.ForeignKey('Category', on_delete=models.CASCADE)
	description = models.TextField(max_length=150)

	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url

	@classmethod
	def search_by_category(cls, search_term):
		'''
		Method to filter images by category
		'''
		product = cls.objects.filter(category__category__icontains=search_term)
		return product

	@classmethod
	def get_product(cls,id):
		try:
			product = Product.objects.get(pk=id)
		except ObjectDoesNotExist:
			raise Http404()
		return Product

class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)
		
	@property
	def shipping(self):
		shipping = False
		orderitems = self.orderitem_set.all()
		for i in orderitems:
			if i.product.digital == False:
				shipping = True
		return shipping

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total 

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total 

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address

# class Comment(models.Model):
# 	STATUS = (
# 		('Now', 'Now'),
# 		('True', 'True'),
# 		('False', 'False'),
# 	)
# 	product = models.ForeignKey(Product, on_delete=models.CASCADE)
# 	user = models.ForeignKey(User, on_delete=models.CASCADE)
# 	subject = models.CharField(max_length=50, blank=True)		
# 	comment = models.CharField(max_length=250, blank=True)
# 	ip = models.CharField(max_length=20, blank=True)
# 	status = models.CharField(max_length=10, choices=STATUS, default='Now')
# 	create_at = models.DateTimeField(auto_now_add=True)
# 	update_at = models.DateTimeField(auto_now=True)

# 	def __str__(self):
# 		return self.subject

class Comment(models.Model):
    content = models.TextField(max_length=150)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_connected = models.ForeignKey(Product, on_delete=models.CASCADE)
		

class Category(models.Model):
    category = models.CharField(max_length =30)

    @classmethod
    def get_all_categories(cls):
        '''
        Method to get all categories
        '''
        categories = cls.objects.all()
        return categories

    def save_category(self):
        '''
        Method to save category
        '''
        self.save()

    @classmethod
    def delete_category(cls,category):
        cls.objects.filter(category=category).delete()

    
    def __str__(self):
        return self.category


