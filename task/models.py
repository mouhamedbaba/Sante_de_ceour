from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Workspace(models.Model):

    date=models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=150) 
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.ManyToManyField(User,  related_name="users")
    background = models.ImageField(upload_to='task/workspace/background/', null=True)
    
    
    
    
    def __str__(self):
        return f'workspace of {self.user} - {self.title}'

    class Meta:
        verbose_name = 'Workspace'
        verbose_name_plural = 'Workspaces'
        
class WorkspaceColumn(models.Model):

    title = models.CharField(max_length=350)
    date=models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE) 
    workspace=models.ForeignKey(Workspace, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'list "{self.title}" du workspace "{self.workspace.title}" de "{self.workspace.user.username}"'

    class Meta:
        verbose_name = 'WorkspaceColumn'
        verbose_name_plural = 'WorkspaceColums'
        

class ColumnCard(models.Model):
    
    title = models.CharField(max_length=350)
    date=models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE) 
    description = models.TextField(null=True, blank=True)
    column = models.ForeignKey(WorkspaceColumn, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='task/workspace/card/image' , null=True, blank=True)
    
    def __str__(self):
        return f'#{self.pk} card du liste "{self.column.title}" du workspace "{self.column.workspace.title}" de "{self.column.workspace.user.username}"'

    class Meta:
        verbose_name = 'ColumnCard'
        verbose_name_plural = 'ColumnCards'