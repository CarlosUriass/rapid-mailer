import click

@click.command()
@click.argument('project_name', default="email-service")
@click.argument('output_dir', default=".")
def create_service(project_name, output_dir):
    click.echo(f'Microservicio "{project_name}" generado en "{output_dir}".')

if __name__ == '__main__':
   
    create_service()
