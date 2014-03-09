import factory
import people.factories
from people.models import Link

class LinkFactory(factory.django.DjangoModelFactory):

	FACTORY_FOR = Link
	
	url = factory.Sequence(lambda n: 'www.rosedu.org' % n)

	person=factory.SubFactory(PersonFactory)

	

