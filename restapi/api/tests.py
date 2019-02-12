# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import collections

from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Person
from .serializers import PersonSerializer

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_person(name="", email=""):
        if name != "" and email != "":
            Person.objects.create(name=name, email=email)

    def setUp(self):
        # add test data
        self.create_person("like glue", "sean paul")
        self.create_person("simple song", "konshens")
        self.create_person("love is wicked", "brick and lace")
        self.create_person("jam rock", "damien marley")


class GetAllPersonsTest(BaseViewTest):

    def test_get_all_persons(self):
        """
        This test ensures that all persons added in the setUp method
        exist when we make a GET request to the persons/ endpoint
        """
        # hit the API endpoint
        response = self.client.get("/api/person/")
        # fetch the data from db
        expected = Person.objects.all()
        serialized = PersonSerializer(expected, many=True)
        data = json.loads(response.content.decode('utf8').replace("'", '"'))
 
        result = json.loads(json.dumps(data["objects"]), object_pairs_hook=collections.OrderedDict)
        self.assertEqual(len(result), len(serialized.data))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
