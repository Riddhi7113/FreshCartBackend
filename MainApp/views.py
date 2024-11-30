from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
import json

@api_view(["GET"])
def home(request):
    print("Hello, world!")
    return Response({"message": "Hello, world!"})

@api_view(["POST"])
def login_view(request):
    try:
        # Parse JSON data from the request body
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
    except (json.JSONDecodeError, KeyError):
        return Response({"message": "Invalid JSON data"}, status=400)

    # Check for missing fields
    if not email or not password:
        return Response({"message": "Email and password are required"}, status=400)

    # Check if the user exists
    try:
        user = User.objects.get(username=email)
    except User.DoesNotExist:
        return Response({"message": "User not found"}, status=404)

    # Verify the password (use Django's `check_password`)
    if not user.check_password(password):
        return Response({"message": "Incorrect password"}, status=401)

    # Generate a token for the user
    token, _ = Token.objects.get_or_create(user=user)

    return Response({"message": "Login successful", "token": token.key})


@api_view(["POST"])
def signup_view(request):
    try:
        # Parse JSON data from the request body
        data = json.loads(request.body)
        email = data.get('email')
        name = data.get('name')
        password = data.get('password')
    except (json.JSONDecodeError, KeyError):
        return Response({"message": "Invalid JSON data"}, status=400)

    # Check for missing fields
    if not email or not password:
        return Response({"message": "Email and password are required"}, status=400)

    # Check if the user already exists
    if User.objects.filter(username=email).exists():
        return Response({"message": "User already exists"}, status=409)

    # Create a new user
    user = User.objects.create_user(username=email,name=name)
    user.set_password(password)
    user.save()

    token, _ = Token.objects.get_or_create(user=user)

    return Response({"message": "User created successfully", "user_id": user.id,"token": token.key})

@api_view(["POST"])
def verify_token(request):
    try:
        # Parse JSON data from the request body
        data = json.loads(request.body)
        token = data.get('token')
    except (json.JSONDecodeError, KeyError):
        return Response({"message": "Invalid JSON data"}, status=400)

    # Check for missing fields
    if not token:
        return Response({"message": "Token is required"}, status=400)

    # Check if the token exists
    if not Token.objects.filter(key=token).exists():
        return Response({"message": "Invalid token"}, status=401)
    
    # get user from token
    user = Token.objects.get(key=token).user

    return Response({"message": "Token is valid"})
