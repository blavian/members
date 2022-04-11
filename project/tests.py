from django.test import TestCase
from django.contrib.auth.models import User
from .models import Account, Members
# Create your tests here.
class CreationTests(TestCase):
    def setUpTestData():
        testuser1 = User.objects.create_user(username= 'testuser1', password = 'testing')
        testuser1.save()
        ## creating an account
        test_account = Account.objects.create(name = 'Test Account 1')
        test_account.save()
        ## creating a member
        test_member = Members.objects.create(first_name = 'test member', last_name = 'test last', phone_number = '3233233233',client_member_id = 23, account_id = 1)
    
    def test_account_creation(self):
        account = Account.objects.get(id=1)
        name = f'{account.name}'
        self.assertEqual(name, 'Test Account 1')
    
    def test_member_creation(self):
        member = Members.objects.get(id=1)
        first_name = f'{member.first_name}'
        last_name = f'{member.last_name}'
        phone_number = f'{member.phone_number}'
        client_member_id = f'{member.client_member_id}'
        account_id = f'{member.account_id}'
        self.assertEqual(first_name, 'test member')
        self.assertEqual(last_name,'test last')
        self.assertEqual(phone_number, '3233233233')
        self.assertEquals(client_member_id, '23')
        self.assertEqual(account_id, '1')
         


