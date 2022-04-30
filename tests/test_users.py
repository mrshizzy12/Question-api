from fastapi import status
import pytest
from httpx import AsyncClient


def get_token(token):
    return {'Authorization': f'Bearer {token}'}

@pytest.mark.asyncio
async def test_get_all_users(async_client: AsyncClient):
    
    res = await async_client.post('/api/auth/register', 
                                     json={'user_name': 'admin', 'password': 'admin'})
    
    login_res = await async_client.post('/api/auth/login',
                                        data={"username":"admin", "password":"admin"})
    data = login_res.json()
    token = data['access_token']
    response = await async_client.get('/api/user/all', headers=get_token(token))
    response_data= response.json()
    assert response.status_code == status.HTTP_200_OK
    assert response_data != []
    assert response_data[0].get('user_name') == 'admin'
    assert response_data[0].get('admin') == True
    