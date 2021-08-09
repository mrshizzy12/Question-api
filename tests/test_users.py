import pytest
from . import app, auth
from httpx import AsyncClient


def get_token(token):
    return {'Authorization': f'Bearer {token}'}




@pytest.mark.asyncio
async def test_get_all_users():
    async with AsyncClient(app=app, base_url='http://test') as client:
        login_response = await client.post('/api/auth/login', data=auth)
        data = login_response.json()
        token = data['access_token']
        response = await client.get('/api/user/all', headers=get_token(token))
    response_data= response.json()  
    assert response.status_code == 200
    assert response_data != []

@pytest.mark.asyncio
async def test_get_all_experts():
    async with AsyncClient(app=app, base_url='http://test') as client:
        login_response = await client.post('/api/auth/login', data=auth)
        data = login_response.json()
        token = data['access_token']
        response = await client.get('/api/user/experts', headers=get_token(token))
    response_data= response.json()  
    assert response.status_code == 200
    assert response_data != []

@pytest.mark.asyncio
async def test_promote_user():
    async with AsyncClient(app=app, base_url='http://test') as client:
        login_response = await client.post('/api/auth/login', data=auth)
        data = login_response.json()
        token = data['access_token']
        response = await client.put(f'/api/user/{4}/promote/', headers=get_token(token))
    response_data= response.json() 
    assert response.status_code != 401
    assert response_data.get('expert') == True