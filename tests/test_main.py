import pytest
from . import app, auth
from httpx import AsyncClient


def get_token(token):
    return {'Authorization': f'Bearer {token}'}


@pytest.mark.asyncio
async def test_get_all_questions():
    async with AsyncClient(app=app, base_url='http://test') as client:
        login_response = await client.post('/api/auth/login', data=auth)
        data = login_response.json()
        token = data['access_token']
        response = await client.get('/api/question/all', headers=get_token(token))
    response_data= response.json()  
    assert response.status_code == 200
    assert response_data != []
    
@pytest.mark.asyncio
async def test_unanswered_questions():
    async with AsyncClient(app=app, base_url='http://test') as client:
        login_response = await client.post('/api/auth/login', data=auth)
        data = login_response.json()
        token = data['access_token']
        response = await client.get('/api/question/unanswered/', headers=get_token(token))
    response_data= response.json()  
    assert response.status_code == 200
    assert response_data != []
    assert response_data[0].get('answer') == None
    
    
@pytest.mark.asyncio
async def test_get_single_question():
    async with AsyncClient(app=app, base_url='http://test') as client:
        login_response = await client.post('/api/auth/login', data=auth)
        data = login_response.json()
        token = data['access_token']
        response = await client.get(f'/api/question/{1}', headers=get_token(token))
    response_data = response.json()  
    assert response.status_code == 200
    assert response_data.get('question') == 'what is Fastapi?'