import traceback
import base64
import geojson
from six.moves.urllib.parse import urlparse
from wsgiref.util import FileWrapper
from django.db.models import Q, Min
from django.db import transaction
from django.http import HttpResponse
from django.core.files.base import ContentFile
from django.core.exceptions import ValidationError
from django.conf import settings
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from rest_framework import viewsets, serializers, status, generics, views
from rest_framework.decorators import detail_route, list_route,renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, BasePermission
from rest_framework.pagination import PageNumberPagination
from datetime import datetime, timedelta
from collections import OrderedDict
from django.core.cache import cache
from ledger.accounts.models import EmailUser,Address
from ledger.address.models import Country
from disturbance import utils
from datetime import datetime,timedelta, date
from disturbance.components.organisations.models import  (   
                                    Organisation,
                                    OrganisationRequest,
                                    OrganisationRequestUserAction,
                                    OrganisationContact,
                                    OrganisationAccessGroup,
                                )

from disturbance.components.organisations .serializers import (   
                                        OrganisationSerializer,
                                        OrganisationRequestSerializer,
                                        OrganisationRequestDTSerializer,
                                        OrganisationContactSerializer,
                                        OrganisationCheckSerializer,
                                        OrganisationPinCheckSerializer,
                                        OrganisationRequestActionSerializer,
                                    )

class OrganisationViewSet(viewsets.ModelViewSet):
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer

    @detail_route(methods=['GET',])
    def contacts(self, request, *args, **kwargs):
        pass

    @detail_route(methods=['POST',])
    def validate_pins(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = OrganisationPinCheckSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            data = {'valid': instance.validate_pins(serializer.validated_data['pin1'],serializer.validated_data['pin2'])} 
            return Response(data);
        except serializers.ValidationError:
            print(traceback.print_exc())
            raise
        except ValidationError as e:
            print(traceback.print_exc())
            raise serializers.ValidationError(repr(e.error_dict))
        except Exception as e:
            print(traceback.print_exc())
            raise serializers.ValidationError(str(e))

    @list_route(methods=['POST',])
    def existance(self, request, *args, **kwargs):
        try:
            serializer = OrganisationCheckSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            data = Organisation.existance(serializer.validated_data['abn']) 
            return Response(data);
        except serializers.ValidationError:
            print(traceback.print_exc())
            raise
        except ValidationError as e:
            print(traceback.print_exc())
            raise serializers.ValidationError(repr(e.error_dict))
        except Exception as e:
            print(traceback.print_exc())
            raise serializers.ValidationError(str(e))
    
class OrganisationRequestsViewSet(viewsets.ModelViewSet):
    queryset = OrganisationRequest.objects.all()
    serializer_class = OrganisationRequestSerializer

    @list_route(methods=['GET',])
    def datatable_list(self, request, *args, **kwargs):
        try:
            qs = self.get_queryset()
            serializer = OrganisationRequestDTSerializer(qs,many=True)
            return Response(serializer.data) 
        except serializers.ValidationError:
            print(traceback.print_exc())
            raise
        except ValidationError as e:
            print(traceback.print_exc())
            raise serializers.ValidationError(repr(e.error_dict))
        except Exception as e:
            print(traceback.print_exc())
            raise serializers.ValidationError(str(e))

    @detail_route(methods=['GET',])
    def assign_request_user(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.assign_to(request.user,request)
            serializer = OrganisationRequestSerializer(instance)
            return Response(serializer.data) 
        except serializers.ValidationError:
            print(traceback.print_exc())
            raise
        except ValidationError as e:
            print(traceback.print_exc())
            raise serializers.ValidationError(repr(e.error_dict))
        except Exception as e:
            print(traceback.print_exc())
            raise serializers.ValidationError(str(e))

    @detail_route(methods=['GET',])
    def unassign(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.unassign(request)
            serializer = OrganisationRequestSerializer(instance)
            return Response(serializer.data) 
        except serializers.ValidationError:
            print(traceback.print_exc())
            raise
        except ValidationError as e:
            print(traceback.print_exc())
            raise serializers.ValidationError(repr(e.error_dict))
        except Exception as e:
            print(traceback.print_exc())
            raise serializers.ValidationError(str(e))

    @detail_route(methods=['GET',])
    def accept(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.accept(request)
            serializer = OrganisationRequestSerializer(instance)
            return Response(serializer.data) 
        except serializers.ValidationError:
            print(traceback.print_exc())
            raise
        except ValidationError as e:
            print(traceback.print_exc())
            raise serializers.ValidationError(repr(e.error_dict))
        except Exception as e:
            print(traceback.print_exc())
            raise serializers.ValidationError(str(e))

    @detail_route(methods=['POST',])
    def assign_to(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            user_id = request.data.get('user_id',None)
            user = None
            if not user_id:
                raise serializers.ValiationError('A user id is required')
            try:
                user = EmailUser.objects.get(id=user_id)
            except EmailUser.DoesNotExist:
                raise serializers.ValidationError('A user with the id passed in does not exist')
            instance.assign_to(user,request)
            serializer = OrganisationRequestSerializer(instance)
            return Response(serializer.data) 
        except serializers.ValidationError:
            print(traceback.print_exc())
            raise
        except ValidationError as e:
            print(traceback.print_exc())
            raise serializers.ValidationError(repr(e.error_dict))
        except Exception as e:
            print(traceback.print_exc())
            raise serializers.ValidationError(str(e))

    @detail_route(methods=['GET',])
    def action_log(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            qs = instance.action_logs.all()
            serializer = OrganisationRequestActionSerializer(qs,many=True)
            return Response(serializer.data) 
        except serializers.ValidationError:
            print(traceback.print_exc())
            raise
        except ValidationError as e:
            print(traceback.print_exc())
            raise serializers.ValidationError(repr(e.error_dict))
        except Exception as e:
            print(traceback.print_exc())
            raise serializers.ValidationError(str(e))

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.validated_data['requester'] = request.user
            with transaction.atomic():
                instance = serializer.save()
                instance.log_user_action(OrganisationRequestUserAction.ACTION_LODGE_REQUEST.format(instance.id),request)
            return Response(serializer.data)
        except serializers.ValidationError:
            print(traceback.print_exc())
            raise
        except ValidationError as e:
            print(traceback.print_exc())
            raise serializers.ValidationError(repr(e.error_dict))
        except Exception as e:
            print(traceback.print_exc())
            raise serializers.ValidationError(str(e))

class OrganisationAccessGroupMembers(views.APIView):
    
    renderer_classes = [JSONRenderer,]
    def get(self,request, format=None):
        members = []
        group = OrganisationAccessGroup.objects.first()
        if group:
            for m in group.all_members:
                members.append({'name': m.get_full_name(),'id': m.id})
        else:
            for m in EmailUser.objects.filter(is_superuser=True,is_staff=True,is_active=True):
                members.append({'name': m.get_full_name(),'id': m.id})
        return Response(members)

