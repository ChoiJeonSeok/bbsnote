from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Board(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.id}] {self.subject}'

class Comment(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.IntegerField(blank=True, default=0)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    # 댓글이 최신순으로 위부터 정렬되게 나오는 meta class.
    class Meta:
        ordering = ['-create_date']
    
    def __str__(self):
        return f'[{self.board.id}:{self.board.subject}]{self.content}'