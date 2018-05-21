from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

class Order(models.Model):
	STATUS_CHOICES = ('P', 'pending'), ('D', 'delivered')
	TAG_CHOICES = ('Y', 'Yes'), ('N', 'No')
	created_time = models.DateTimeField(auto_now_add=True)
	updated_time = models.DateTimeField(auto_now_add=True)
	comment = models.TextField()
	status= models.CharField(choices=STATUS_CHOICES, max_length=1)
	location = models.ForeignKey('Location', on_delete=models.SET_NULL, related_name='order_location', null=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='order_user', null=True)
	deleted = models.CharField(choices=TAG_CHOICES, max_length=1, default = 'N')

	class Meta:
		db_table = 'orders' 
		# permissions = (
  #           ('view_order', 'View order'),
  #       )


	def delete(self, using=None): 
		self.deleted = 'Y'
		self.save()