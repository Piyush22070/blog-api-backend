from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
import json

@csrf_exempt
def register(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST allowed'}, status=405)

    try:
        data = json.loads(request.body)
        username = data['username']
        email = data['email']
        password = data['password']

        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username already exists'}, status=400)

        user = User.objects.create_user(username=username, email=email, password=password)
        return JsonResponse({'message': 'User registered successfully'})
    except:
        return JsonResponse({'error': 'Invalid data'}, status=400)


@csrf_exempt
def login_view(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST allowed'}, status=405)

    try:
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return JsonResponse({'message': 'Login successful'})
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)
    except:
        return JsonResponse({'error': 'Invalid data'}, status=400)


@csrf_exempt
@login_required
def create_post(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST allowed'}, status=405)

    try:
        data = json.loads(request.body)
        title = data['title']
        content = data['content']
        post = Post.objects.create(author=request.user, title=title, content=content)
        return JsonResponse({'id': post.id, 'message': 'Post created'})
    except:
        return JsonResponse({'error': 'Invalid data'}, status=400)


def get_all_posts(request):
    posts = Post.objects.all().order_by('-created_at')
    data = [
        {
            'id': post.id,
            'title': post.title,
            'author': post.author.username,
            'created_at': post.created_at
        }
        for post in posts
    ]
    return JsonResponse(data, safe=False)


def get_single_post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        comments = Comment.objects.filter(post=post).order_by('-created_at')
        comment_data = [
            {
                'user': comment.user.username,
                'text': comment.text,
                'created_at': comment.created_at
            }
            for comment in comments
        ]
        data = {
            'id': post.id,
            'title': post.title,
            'content': post.content,
            'author': post.author.username,
            'created_at': post.created_at,
            'comments': comment_data
        }
        return JsonResponse(data)
    except Post.DoesNotExist:
        return JsonResponse({'error': 'Post not found'}, status=404)


@csrf_exempt
@login_required
def comment_on_post(request, post_id):
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST allowed'}, status=405)

    try:
        post = Post.objects.get(id=post_id)
        data = json.loads(request.body)
        text = data['text']
        comment = Comment.objects.create(post=post, user=request.user, text=text)
        return JsonResponse({'id': comment.id, 'message': 'Comment added'})
    except Post.DoesNotExist:
        return JsonResponse({'error': 'Post not found'}, status=404)
    except:
        return JsonResponse({'error': 'Invalid data'}, status=400)
