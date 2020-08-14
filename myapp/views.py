from django.shortcuts import render, redirect
from django.contrib.auth import logout
import requests

def mainPage(request):
    context = {}
    if request.user.is_authenticated:
        user = request.user
        user_token = user.social_auth.values()[0]["extra_data"]["access_token"]
        user_friends = requests.get(
            f'https://api.vk.com/method/friends.get?user_id={user.username[2:]}'
            f'&order=random&count=5&fields=photo_100'
            f'&access_token={user_token}'
            f'&v=5.122').json()
        user_friends = user_friends["response"]['items']
        user_friends = [{"first_name": friend["first_name"], "last_name": friend["last_name"], "img": friend['photo_100']}
                   for friend in user_friends]
        context["friends"] = user_friends
    return render(request, 'base.html', context)

def logout_view(request):
        logout(request)
        return redirect("/")