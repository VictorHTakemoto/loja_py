from django.test import TestCase
from django.core import mail
from main import forms

class TestarForms(TestCase):
    def testar_formulario_fale_conosco_corretamente_preenchido(self):
        formulario = forms.FormFaleConosco(
            {
                'nome': 'Francisco Maciel',
                'email_origem': 'francisco@teste.com',
                'mensagem': 'Testando a funcionalidade do foremulario fale conosco'
            }
        )

        self.assertTrue(formulario.is_valid())
        formulario.enviar_mensagem_por_email()
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'FALE CONOSCO: Mensagem recebida.')
    def testar_formilario_fale_conosco_invalido(self):
        formulario = forms.FormFaleConosco(
            {
                'mensagem': 'Testando a funcionalidade do formulario fale conosco'
            }
        )
        self.assertFalse(formulario.is_valid())
