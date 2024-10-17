from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Subjects'
        ordering = ['name']

class University(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Universities'
        ordering = ['name']


class Professor(models.Model):
    name = models.CharField(max_length=50)
    university = models.ForeignKey(University, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Professors'
        ordering = ['name']


class Faculty(models.Model):
    name = models.CharField(max_length=50)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Faculties'
        ordering = ['name']


class Group(models.Model):
    name = models.CharField(max_length=50)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Groups'
        ordering = ['name']


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    balance = models.IntegerField(default=0)
    university = models.ForeignKey(University, on_delete=models.CASCADE, null=True, blank=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    rating = models.IntegerField(default=0)
    profile_picture = models.ImageField(null=True, blank=True)
    role = models.IntegerField(default=1)
    is_banned = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = 'Users'
        ordering = ['-created_at']


class Work(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True, default=None)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='works')
    file = models.FileField(upload_to='works/')
    image = models.ImageField(upload_to='works/', null=True, blank=True, default=None)
    price = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authored_works')
    university = models.ForeignKey(University, on_delete=models.CASCADE, null=True, blank=True, default=None, related_name='university_works')
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, null=True, blank=True, default=None, related_name='assigned_works')
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_unique = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Works'
        ordering = ['-created_at']



class Purchase(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchases_made')
    work = models.ForeignKey(Work, on_delete=models.CASCADE, related_name='purchases')
    purchase_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Purchases'
        ordering = ['-purchase_date']

    def __str__(self):
        return f"{self.buyer.username} bought {self.work.title} from {self.work.author.username} at {self.purchase_date.strftime('%Y-%m-%d')}"


class FavoriteWork(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_works')
    work = models.ForeignKey(Work, on_delete=models.CASCADE, related_name='favorited_by')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Favorite works'
        verbose_name = 'Favorite work'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} added {self.work.title} to favorites at {self.created_at.strftime('%Y-%m-%d')}"


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.sender.username} sent message '{self.message}' to {self.receiver.username} at {self.created_at.strftime('%Y-%m-%d')}"

    class Meta:
        verbose_name_plural = 'Messages'
        ordering = ['-created_at']


class Review(models.Model):
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='given_reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_reviews')
    review = models.TextField()
    rating = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.reviewer.username} leaved review for {self.user.username} with rating: {self.rating} and text: {self.review}"

    class Meta:
        verbose_name_plural = 'Reviews'
        ordering = ['-created_at']


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    balance_addition = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Transactions'
        ordering = ['-created_at']


class WorkReport(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_work_reports')
    work = models.ForeignKey(Work, on_delete=models.CASCADE, related_name='work_reports')
    reason = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Work Reports'
        verbose_name = 'Work Report'
        ordering = ['-created_at']


class UserReport(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_user_reports')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_reports')
    reason = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'User Reports'
        verbose_name = 'User Report'
        ordering = ['-created_at']


class ReviewReports(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_review_reports')
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    reason = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Review Reports'
        verbose_name = 'Review Report'
        ordering = ['-created_at']
