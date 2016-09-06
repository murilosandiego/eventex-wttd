from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Murilo Sandiego', cpf='09161842699',
                    email='murilosandiego1@gmail.com', phone='38991712781')
        self.client.post('/inscricao/',data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect,self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br','murilosandiego1@gmail.com']

        self.assertEqual(expect,self.email.to)

    def test_subscription_email_body(self):

        contents = [
            'Murilo Sandiego',
            '09161842699',
            'murilosandiego1@gmail.com',
            '38991712781',
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
