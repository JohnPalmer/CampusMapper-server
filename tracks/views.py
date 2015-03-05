from rest_framework import viewsets
from rest_framework.generics import mixins
from serializers import DataPointSerializer
from models import DataPoint
from django.shortcuts import render
import string
import random


class ReadOnlyModelViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    A viewset that provides `retrieve`, and 'list` actions.

    To use it, override the class and set the `.queryset` and
    `.serializer_class` attributes.
    """
    pass


class WriteOnlyModelViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    A viewset that provides`create` action.

    To use it, override the class and set the `.queryset` and
    `.serializer_class` attributes.
    """
    pass


class ReadWriteOnlyModelViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet, mixins.ListModelMixin):
    """
    A viewset that provides `retrieve`, 'list`, and `create` actions.

    To use it, override the class and set the `.queryset` and
    `.serializer_class` attributes.
    """
    pass


# for production, change to write only
class DataPointViewSet(ReadWriteOnlyModelViewSet):
    queryset = DataPoint.objects.all()
    serializer_class = DataPointSerializer


def show_user_code(request):
    this_code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))
    context = {'this_code': this_code}
    return render(request, 'tracks/get_user_code.html', context)
