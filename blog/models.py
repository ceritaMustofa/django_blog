import string
import random
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(unique=True, max_length=200, editable=False)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    body = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        slug = slugify(self.title)
        try:
            post_obj = Post.objects.get(slug=slug)
            random_suffix = ''.join([
                random.choice(string.ascii_letters + string.digits)
                for i in range(5)
            ])
            slug += "-" + random_suffix
        except Post.DoesNotExist:
            pass
        self.slug = slug

        super(Post, self).save(*args, **kwargs) # Call the real save() method
    
    def generate_slug(self, save_to_obj=False, add_random_suffix=True):
        
        generated_slug = ""

        random_suffix = ""
        if add_random_suffix:
            random_suffix = ''.join([
                random.choice(string.ascii_letters + string.digits)
                for i in range(5)
            ])
            generated_slug += '-%s' % random_suffix

        if save_to_obj:
            self.slug = generated_slug
            self.save(update_fields=['slug'])
        
        return generated_slug
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})
    
