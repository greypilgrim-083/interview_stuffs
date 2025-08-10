from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    CAMPUS_CHOICES = [
        ('ON', 'On-Campus'),
        ('OFF', 'Off-Campus'),
    ]

    STATUS_CHOICES = [
        ('ACCEPTED', 'Accepted'),
        ('REJECTED', 'Rejected'),
        ('TBD', 'To Be Decided'),
    ]

    title = models.CharField(max_length=200)
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    campus_type = models.CharField(max_length=3, choices=CAMPUS_CHOICES, default='ON')
    salary_range = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='TBD')
    cg_criteria = models.CharField(max_length=20, default='None')
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def score(self):
        # total upvotes - total downvotes
        upvotes = self.votes.filter(vote_type='UP').count()
        downvotes = self.votes.filter(vote_type='DOWN').count()
        return upvotes - downvotes


class Vote(models.Model):
    VOTE_CHOICES = [
        ('UP', 'Upvote'),
        ('DOWN', 'Downvote'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="votes", on_delete=models.CASCADE)
    vote_type = models.CharField(max_length=5, choices=VOTE_CHOICES)

    class Meta:
        unique_together = ('user', 'post')  # one vote per user per post

    def __str__(self):
        return f"{self.user} - {self.vote_type} - {self.post.title}"


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post.title}"
