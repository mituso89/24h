import json
from django.test import TestCase
from django.urls import reverse
from .models import Tag
from .serializers import TagBaseSerializer
from utils.helpers.test_helpers import TestHelpers
# Create your tests here.


class TagTestCase(TestCase):

    def setUp(self):
        self.token = TestHelpers.testSetup(self)

        item0 = {
            "uid": "key0",
            "value": "value0",
        }
        item1 = {
            "uid": "key1",
            "value": "value1",
        }
        item2 = {
            "uid": "key2",
            "value": "value2",
        }

        self.item0 = TagBaseSerializer(data=item0)
        self.item0.is_valid(raise_exception=True)
        self.item0.save()
        self.item0 = Tag.objects.get(**self.item0.data)

        self.item1 = TagBaseSerializer(data=item1)
        self.item1.is_valid(raise_exception=True)
        self.item1.save()
        self.item1 = Tag.objects.get(**self.item1.data)

        self.item2 = TagBaseSerializer(data=item2)
        self.item2.is_valid(raise_exception=True)
        self.item2.save()
        self.item2 = Tag.objects.get(**self.item2.data)

    def test_list(self):
        response = self.client.get(
            reverse('api_v1:tag:list'),
            Authorization='JWT ' + self.token,
        )
        self.assertEqual(response.status_code, 200)
        response = response.json()
        self.assertEqual(response['count'], 3)

    def test_detail(self):
        # View not exist
        response = self.client.get(
            reverse(
                'api_v1:tag:detail',
                kwargs={'pk': 0}
            ),
            Authorization='JWT ' + self.token,
        )
        self.assertEqual(response.status_code, 404)

        # View success
        response = self.client.get(
            reverse(
                'api_v1:tag:detail',
                kwargs={'pk': self.item1.pk}
            ),
            Authorization='JWT ' + self.token,
        )
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        dataSuccess = {
            'uid': 'key3',
            'value': 'value3'
        }
        dataFail = {
            'uid': 'key2',
            'value': 'value3'
        }

        # Add duplicate
        response = self.client.post(
            reverse('api_v1:tag:create'),
            json.dumps(dataFail),
            content_type='application/json',
            Authorization='JWT ' + self.token,
        )
        self.assertEqual(response.status_code, 400)

        # Add success
        response = self.client.post(
            reverse('api_v1:tag:create'),
            json.dumps(dataSuccess),
            content_type='application/json',
            Authorization='JWT ' + self.token,
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Tag.objects.count(), 4)

    def test_edit(self):
        dataSuccess = {
            "uid": "key3",
            "value": "value3"
        }

        dataFail = {
            "uid": "key2",
            "value": "value2"
        }

        # Update not exist
        response = self.client.put(
            reverse(
                'api_v1:tag:edit',
                kwargs={
                    'pk': 0
                }
            ),
            json.dumps(dataFail),
            content_type='application/json',
            Authorization='JWT ' + self.token,
        )
        self.assertEqual(response.status_code, 404)

        # Update duplicate
        response = self.client.put(
            reverse(
                'api_v1:tag:edit',
                kwargs={
                    'pk': self.item1.pk
                }
            ),
            json.dumps(dataFail),
            content_type='application/json',
            Authorization='JWT ' + self.token,
        )
        self.assertEqual(response.status_code, 400)

        # Update success
        response = self.client.put(
            reverse(
                'api_v1:tag:edit',
                kwargs={
                    'pk': self.item1.pk
                }
            ),
            json.dumps(dataSuccess),
            content_type='application/json',
            Authorization='JWT ' + self.token,
        )
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        # Remove not exist
        response = self.client.delete(
            reverse(
                'api_v1:tag:delete',
                kwargs={
                    'pk': 0
                }
            ),
            Authorization='JWT ' + self.token,
        )
        self.assertEqual(response.status_code, 404)
        self.assertEqual(Tag.objects.count(), 3)

        # Remove single success
        response = self.client.delete(
            reverse(
                'api_v1:tag:delete',
                kwargs={
                    'pk': self.item1.pk
                }
            ),
            Authorization='JWT ' + self.token,
        )
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Tag.objects.count(), 2)

        # Remove list success
        response = self.client.delete(
            reverse(
                'api_v1:tag:delete',
                kwargs={
                    'pk': ','.join([str(self.item0.pk), str(self.item2.pk)])
                }
            ),
            Authorization='JWT ' + self.token,
        )
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Tag.objects.count(), 0)
