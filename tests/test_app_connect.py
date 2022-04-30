from fastapi import status
import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_api_connect(async_client: AsyncClient):
    response = await async_client.get('/api/question/')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'ping': 'pong'}
    

