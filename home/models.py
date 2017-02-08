from django.db import models

# Create your models here.
class submissions(models.Model):
	name = models.CharField((u"Name"),max_length=200)
	email = models.CharField((u"Email-ID"),max_length=200)
	subject = models.CharField((u"Subject"),max_length=200)
	message = models.CharField((u"Message"),max_length=10000)

	class Meta:
		verbose_name = 'Submissions'
		verbose_name_plural = 'Submissions'

	def __str__(self):
		return self.name+' - '+self.email+'-'+self.subject
