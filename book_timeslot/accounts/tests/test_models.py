from django.test import TestCase
from accounts.models import User


class TestModels(TestCase):

    def setUp(self):
        self.user1 = User.objects.create(
            username='Test',
            first_name='test',
            last_name='test',
            phone='7978797977',
            email='test@gmail.com',
            is_customer=True,
            is_manager=False
        )

    # def setUp(self):
    #     self.user2 = User.objects.create(
    #         username='femi',
    #         first_name='Femi',
    #         last_name='Shaju',
    #         phone='7012289727',
    #         email='femi1602@gmail.com',
    #         is_customer=True,
    #         is_manager=False
    #     )

    def test_user_creation(self):
        self.assertEquals(self.user1.username, 'Test')
        self.assertEquals(self.user1.is_customer, True)
        # self.assertEquals(self.user2.username, 'femi')
        # self.assertEquals(self.user2.is_customer, True)