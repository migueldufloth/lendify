from django.core.management.base import BaseCommand
from accounts.models import User


class Command(BaseCommand):
    help = 'Cria usuários iniciais para desenvolvimento'

    def handle(self, *args, **options):
        seeds = [
            {
                'email': 'admin@lendify.com',
                'name': 'Administrador',
                'role': User.Role.ADMINISTRADOR,
                'password': 'Admin@1234',
                'is_staff': True,
            },
            {
                'email': 'operador@lendify.com',
                'name': 'Operador Padrão',
                'role': User.Role.OPERADOR,
                'password': 'Operador@1234',
            },
            {
                'email': 'solicitante@lendify.com',
                'name': 'Solicitante Padrão',
                'role': User.Role.SOLICITANTE,
                'password': 'Solicitante@1234',
            },
        ]

        for data in seeds:
            email = data.pop('email')
            password = data.pop('password')
            if User.objects.filter(email=email).exists():
                self.stdout.write(f'  já existe: {email}')
            else:
                User.objects.create_user(email=email, password=password, **data)
                self.stdout.write(self.style.SUCCESS(f'  criado: {email}'))
