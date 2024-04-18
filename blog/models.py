from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=212)
    image = models.ImageField(upload_to='author', blank=True, null=True)
    profession = models.CharField(max_length=212)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=212)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class AboutResume(models.Model):
    icon = models.URLField()
    image = models.ImageField(upload_to='resume')

    def __str__(self):
        return self.icon


class Article(models.Model):
    title = models.CharField(max_length=212)
    image = models.ImageField(upload_to='article', blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now=True)

    # comment = models.ForeignKey('Comment', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    name = models.CharField(max_length=212)
    email = models.EmailField()
    website = models.URLField()
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class About(models.Model):
    title = models.CharField(max_length=212)
    description = models.TextField()
    name = models.CharField(max_length=212)
    date_ofb = models.CharField(max_length=212)
    address = models.CharField(max_length=212)
    zip_code = models.BigIntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=212)
    image = models.ImageField(upload_to='posts', blank=True, null=True)
    cv = models.FileField()
    project_c = models.CharField(max_length=212)

    def __str__(self):
        return self.name


class Education(models.Model):
    edu_year = models.CharField(max_length=212)
    title = models.CharField(max_length=212)
    university = models.CharField(max_length=212)
    description = models.TextField()

    def __str__(self):
        return self.title


class Experience(models.Model):
    work_year = models.CharField(max_length=212)
    title = models.CharField(max_length=212)
    university = models.CharField(max_length=212)
    description = models.TextField()

    def __str__(self):
        return self.title


class Skills(models.Model):
    title = models.CharField(max_length=50)
    percentage = models.IntegerField()
    last_week_p = models.IntegerField()
    week_p = models.IntegerField()

    def __str__(self):
        return self.title


class Awards(models.Model):
    award_year = models.CharField(max_length=212)
    title = models.CharField(max_length=212)
    please = models.CharField(max_length=212)
    description = models.TextField()

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=212)
    description = models.TextField()

    def __str__(self):
        return self.title


class Categories(models.Model):
    name = models.CharField(max_length=212)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    img = models.ImageField(upload_to='blog', null=True, blank=True)
    title2 = models.CharField(max_length=212)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True)
    paragraph = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Projects(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    img = models.ImageField(upload_to='projects', null=True)

    def __str__(self):
        return self.title




