import json

from .models import Car, Make, Model

from graphene_django.utils.testing import GraphQLTestCase


def sample_car(license_plate, **params):
    make_instance, _ = Make.objects.get_or_create(name='test make')
    model_instance, _ = Model.objects.get_or_create(name='test make')
    defaults = {
        'license_plate': license_plate,
        'notes': 10,
        'make': make_instance,
        'model': model_instance
    }
    defaults.update(params)

    return Car.objects.create(**defaults)


class GraphTestCase(GraphQLTestCase):
    def setUp(self):
        for i in range(5):
            sample_car(license_plate=f"Number-{i}")

    def test_car_list(self):
        response = self.query(
            '''
            query {
                cars {
                    id
                    model {
                    name
                    }
                }
            }
            ''',
        )

        content = json.loads(response.content)
        self.assertEqual(len(content.get('data').get('cars')), 5)
        self.assertResponseNoErrors(response)

    def test_make_create(self):
        response = self.query(
            '''
            mutation Test {
              createMake(input: {name:"Testmake"}) {
                ok
                make {
                  id
                  name
                }
              }
            }
            ''',
        )
        content = json.loads(response.content)
        print(content)
        self.assertTrue(Make.objects.filter(name="Testmake").exists())
        self.assertResponseNoErrors(response)
