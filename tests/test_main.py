from fastapi import status
import pytest
from httpx import AsyncClient


def get_token(token):
    return {'Authorization': f'Bearer {token}'}


@pytest.mark.asyncio
async def test_get_all_questions(async_client: AsyncClient):
    res = await async_client.post('/api/auth/register', 
                                     json={'user_name': 'johndoe', 'password': 'jupiter'})
    
    response = await async_client.post('/api/auth/login',
                                        data={"username":"johndoe", "password":"jupiter"})
    
    data = response.json()
    token = data['access_token']
    response = await async_client.get('/api/question/all', headers=get_token(token))
    
    response_data = response.json()  
    assert response.status_code == status.HTTP_200_OK
    assert response_data == []