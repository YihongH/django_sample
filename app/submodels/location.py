from django.db import models

class Location(models.Model):
	name = models.CharField(max_length=50)
	address = models.CharField(max_length=100)
	created_time = models.DateTimeField(auto_now_add=True)
	updated_time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '%s: %s' % (self.name, self.address)

	class Meta:
		db_table = 'locations'
		permissions = (
            ('view_location', 'Can view location'),
        )
	
