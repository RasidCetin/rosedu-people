import factory
from people.models import Person

class PersonFactory(factory.django.DjangoModelFactory):
	FACTORY_FOR = Person

	description = factory.Sequence(lambda n: 'Author"s name is %sCetin%s ' % (n, n));
	
	@factory.post_generation
	def organisations(self, create, extracted, **kwargs):		
		if not create:
			return
		if extracted:
			for organisation in extracted:
				self.organisations.add(organisation)
	
