from .models import Evaluation
from django.conf import settings
import requests
import json


class EvaluationApi(object):

    def all(self):
        """Send requisition to get all evaluations."""
        url = settings.API_URL + 'patients/'
        # return self._get_filtered_list(url)
        return True


