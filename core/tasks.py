from celery import shared_task
from .models import Post

@shared_task
def send_post_notification(post_id):
    try:
        post = Post.objects.get(id=post_id)
        print(f"🔔 Notification sent for post: {post.title}")
    except Post.DoesNotExist:
        print("❌ Post not found.")
