from app import create_app
import logging
import uvicorn
from app.database import SessionLocal
from app.dependency import init_db


app = create_app()



@app.on_event('startup')
async def on_startup():
    try:
        print('Checking database connection...')
        db = SessionLocal()
        # Try to create session to check if DB is awake
        await db.execute('SELECT 1')
        print('Done.')
    except Exception as e:
        print('Database conncetion failed. ', e)
    finally:
        await db.close()


if __name__ == '__main__':
    uvicorn.run('manage:app', debug=True, reload=True, workers=1)
    