from django.shortcuts import render
from .models import Post, Like, RESULT
from django.http import HttpResponse
from . readcsv import get_results, update_results


def index(request):

    posts = Post.objects.all()
    df = get_results("SELECT * FROM post_result")
    params = {
        'posts':posts,
        'results': df.to_json(orient='records')
    }
    return render(request, 'index.html', params)


def like(request):

    if request.method == 'GET':
        post_id = request.GET['post_id']
        likedpost = Post.objects.get(id = post_id )
        m = Like( post=likedpost )
        m.save()
        return HttpResponse('successsss')
    else:
        return HttpResponse("unsuccesful")

def update_user_check(request):
    if request.method == 'GET':
        id = request.GET['id']
        user_check = request.GET['user_check']
        update_results(id, ['USER_CHECK',user_check])
        return HttpResponse('success')
    else:
        return HttpResponse("unsuccesful")

def update_note(request):
    if request.method == 'GET':
        id = request.GET['id']
        note = request.GET['note']
        update_results(id, ['NOTE', note])
        return HttpResponse('success')
    else:
        return HttpResponse("unsuccesful")