from django.db import models
from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
	
	def create_user(self, email, password=None):
		if not email:
			raise ValueError('Email must not be blank.')
				
		user = self.model(email=email)
		user.set_password(password)
		user.save(using=self._db)
		return user


	def create_superuser(self, email, password=None):
		user = self.create_user(email, password)
		user.is_admin = True
		user.save(using=self._db)
		return user
