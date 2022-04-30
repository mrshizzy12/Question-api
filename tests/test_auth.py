from fastapi import status
import pytest
from httpx import AsyncClient

auth = {"username":"johndoe", "password":"jupiter"}



@pytest.mark.asyncio
async def test_create_users(async_client: AsyncClient):
    
    response = await async_client.post('/api/auth/register', 
                                     json={'user_name': 'johndoe', 'password': 'jupiter'})
    data = response.json()
    assert response.status_code == status.HTTP_201_CREATED
    assert data['user_name'] == "johndoe"
    
   
@pytest.mark.asyncio
async def test_login(async_client: AsyncClient):
    res = await async_client.post('/api/auth/register', 
                                     json={'user_name': 'johndoe', 'password': 'jupiter'})
    
    response = await async_client.post('/api/auth/login', data=auth)
    data = response.json()  
    assert response.status_code == status.HTTP_202_ACCEPTED
    assert 'access_token' in data
    
@pytest.mark.asyncio
async def test_invalid_credentials(async_client: AsyncClient):
    res = await async_client.post('/api/auth/register', 
                                     json={'user_name': 'johndoe', 'password': 'jupiter'})
    
    response = await async_client.post('/api/auth/login',
                                        data={"username":"janedoe", "password":"jupiter"})
    data = response.json()   
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert data['detail'] == 'username or password is inccorect'
    
'''
@pytest.mark.asyncio
async def test_create_users():
    async with AsyncClient(app=app, base_url='http://test') as client:
        response = await client.post('/api/auth/register', 
                                     json={'user_name': 'johndoe', 'password': 'jupiter'})
    data = response.json()
    assert response.status_code == 400
    assert data['detail'] == 'username already exists, please pick another username'
    

@pytest.mark.asyncio
async def test_login():
    async with AsyncClient(app=app, base_url='http://test') as client:
        response = await client.post('/api/auth/login', data=auth)
    data = response.json()  
    assert response.status_code == 202
    assert 'access_token' in data
    
    
@pytest.mark.asyncio
async def test_invalid_credentials():
    async with AsyncClient(app=app, base_url='http://test') as client:
        response = await client.post('/api/auth/login',
                                     data={'username': 'janedoe', 'password': 'saturn'})
    data = response.json()  
    assert response.status_code == 404
    assert data['detail'] == 'username or password is inccorect'
'''
    