import email
import click

from clients.services import ClientService
from clients.models import Client


@click.group()
def clients():
    """Maneges the clients lifecycle"""
    pass


@clients.command()
@click.option('-n', '--name',
                type=str,
                prompt=True,
                help='The client name')
@click.option('-c', '--company',
                type=str,
                prompt=True,
                help='The client company')
@click.option('-e', '--email',
                type=str,
                prompt=True,
                help='The client email')
@click.option('-p', '--position',
                type=str,
                prompt=True,
                help='The client position')                                
@click.pass_context
def create(ctx, name, company, email, position):
    """Create a new Client"""
    client = Client(name, company, email, position)

    clientService = ClientService(ctx.obj['clients_table'])
    clientService.create_client(client)


@clients.command()
@click.pass_context
def list(ctx):
    """List all clients"""
    clientService = ClientService(ctx.obj['clients_table'])

    clients_list = clientService.client_list()

    click.echo('  ID  |  Name  |  Company  |  Email  |  Position  ')
    click.echo('*' * 50)

    for client in clients_list:
        click.echo('  {uid}  |  {name}  |  {company}  |  {email}  |  {position}  '.format(
            uid=client['uid'],
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position']
        ))


@clients.command()
@click.pass_context
def update(ctx, client_uid):
    """Updates a client"""
    pass


@clients.command()
@click.pass_context
def delete(ctx, client_uid):
    """Deletes a client"""
    pass

all = clients