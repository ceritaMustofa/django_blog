from turtle import title
from urllib import response
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post

class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username= "testuser", email="test@email.com", password="secret"
        )
        
        cls.post = Post.objects.create(
            title="Test post title",
            body = "Test post body",
            author= cls.user,
        )

    def test_post_model(self):
        self.assertEqual(self.post.title, "Test post title")
        self.assertEqual(self.post.body, "Test post body")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(str(self.post), "Test post title")
        self.assertEqual(self.post.get_absolute_url(), "/post/test-post-title/")
        
    def test_url_exists_at_correct_location_listview(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        
    def test_url_exists_at_correct_location_detailview(self):
        response = self.client.get("/post/test-post-title/")
        self.assertEqual(response.status_code, 200)
        
    def test_post_listview(self): 
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test post body")
        self.assertTemplateUsed(response, "home.html")
        
    def test_post_detailview(self): 
        response = self.client.get(reverse("post_detail",
        kwargs={"slug": self.post.slug}))
        no_response = self.client.get("/post/third-post/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Test post title")
        self.assertTemplateUsed(response, "post_detail.html")
        
    def test_post_createview(self):
        response = self.client.post(
            reverse("add_post"),
            {
                "title":"New post",
                "body":"New body",
                "author":self.user.id,
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "New post")
        self.assertEqual(Post.objects.last().body, "New body")
    def test_post_updateview(self): # new
        response = self.client.post(
        reverse("edit_post", kwargs={"slug":self.post.slug}),
            {
            "title": "Updated title",
            "body": "Updated text",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "Updated title")
        self.assertEqual(Post.objects.last().body, "Updated text")
    
    def test_post_deleteview(self): # new
        response = self.client.post(reverse("delete_post", kwargs={"slug":self.post.slug}))
        self.assertEqual(response.status_code, 302)