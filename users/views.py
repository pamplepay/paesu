from .forms import LoginForm
from .models import User
from .choices import REGION_CHOICES

from django.contrib import messages, auth
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import FormView

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


def register_view(request):

    if request.method == 'POST':
        
        my_dict = {x[1]: x[0] for x in REGION_CHOICES}

        User.objects.create_user(
            user_id = request.POST['user_id'],
            password= request.POST['password1'],
            email = request.POST.get('user_email'),
            hp = request.POST.get('hp'),
            business_name = request.POST.get('BusinessName'),
            business_add = '',
            business_regnum = request.POST.get('BusinessNumber'),
            region = my_dict[request.POST.get('area')],
        )

        return redirect('/')

    else:
        context = {
            'region' : [x[1] for x in REGION_CHOICES],
        }
        return render(request, 'users/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')


def ChageInfo(request):

    if request.method == 'POST':

        hp = request.POST['hp']
        email = request.POST['email']
        business_name = request.POST['business_name']
        business_add = request.POST['business_add']
        business_regnum = request.POST['business_regnum']

        user = request.user
        update_field = []

        user.hp = hp
        update_field.append('hp')
        user.email = email
        update_field.append('email')
        user.business_name = business_name
        update_field.append('business_name')
        user.business_add = business_add
        update_field.append('business_add')
        user.business_regnum = business_regnum
        update_field.append('business_regnum')

        user.save(update_fields=update_field)

        # password 수정 삭제
        # password = request.POST['password']
        # if password != '':
        #     user.set_password(password)
        #     user.save()
        #     update_session_auth_hash(request, request.user)


        return redirect('/changeInfo')

    else:
        if request.user.is_authenticated:
            user_info = User.objects.get(user_id = request.user)
            context = {
                'user_info': user_info
                }
            
            return render(request, 'users/changeinfo.html', context)

        else:
            return redirect('/')


class LoginView(FormView):
    '''
    View for the main page that handles login form requests.
    '''
    template_name = 'users/index.html'
    form_class = LoginForm
    success_url = '/list'

    def form_valid(self, form):
        user_id = form.cleaned_data.get("user_id")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=user_id, password=password)

        if user:
            self.request.session['user_id'] = user_id
            login(self.request, user)
            return super().form_valid(form)

    def form_invalid(self, form):
        '''
        Handles invalid form submissions by displaying an error message.
        '''
        messages.error(self.request, '아이디 또는 비밀번호를 확인해주세요.')
        return super().form_invalid(form)


class IdValidation(APIView):
    '''
    중복 아이디가 있는지 검증하는 API
    jquery blur로 AJAX통해 제출.
    '''
    def post(self, request):
        try:
            user_id = request.data['user_id']
            try:
                user = User.objects.get(user_id=user_id)
            except Exception as e:
                user = None
            
            context = {
                'data' : "not exist" if user is None else "exist"
            }

        except KeyError:
            return Response({'message': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse(context)
        
# class HPValidation(APIView):
#     '''
#     중복 휴대폰 번호가 있는지 검증하는 API
#     jquery blur로 AJAX통해 제출.
#     '''
#     def post(self, request):
#         try:
#             hp = request.data['hp']
#             try:
#                 user = User.objects.get(hp=hp)
#             except Exception as e:
#                 user = None
            
#             context = {
#                 'data' : "not exist" if user is None else "exist"
#             }

#         except KeyError:
#             return Response({'message': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return JsonResponse(context)
        
class EmailValidation(APIView):
    '''
    중복 이메일이 있는지 검증하는 API
    jquery blur로 AJAX통해 제출.
    '''
    def post(self, request):
        try:
            email = request.data['user_email']
            try:
                user = User.objects.get(email=email)
            except Exception as e:
                user = None
            
            context = {
                'data' : "not exist" if user is None else "exist"
            }

        except KeyError:
            return Response({'message': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse(context)