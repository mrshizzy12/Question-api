from app import create_app
import asyncio
from app.dependency import init_models
import typer
import os
import uvicorn


app = create_app()

cli = typer.Typer()

@cli.command()
def db_init():
    print('creating database....')
    asyncio.run(init_models())
    print('databse created')


if __name__ == '__main__':
    try:
        if not os.path.exists('db.sqlite'):
            cli()
    except Exception:
        print('databse creation failed!')
    finally:
        uvicorn.run('manage:app', debug=True, reload=True, workers=1)
    