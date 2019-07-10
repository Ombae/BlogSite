import unittest
from app.models import User,Blog
from app import db

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(password = 'banana', username = "Seth",email = "seth@ms.com",profile_pic_path = "/static/photos")

    def test_save_user(self):
        self.new_user.save_user()
        # self.assertTrue(len(User.query.all()>0))

class BlogTest(unittest.TestCase):
    def setUp(self):
        # self.user_Seth = User(id=1,username = 'Seth',password = 'banana', email = 'seth@ms.com',bio="Time is an abstract")
        self.new_blog = Blog(id=5,title='Review for pitches',content="content",date_posted = "10-7-2018"  )

    def tearDown(self):
        Blog.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.id,5)
        self.assertEquals(self.new_blog.title,'Review for pitches')
        self.assertEquals(self.new_blog.date_posted,"10-7-2018")


    def test_save_blog(self):
        self.new_blog.save_blog()
        # self.assertTrue(len(Blog.query.all())>0)
