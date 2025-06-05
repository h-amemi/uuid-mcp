import asyncio
import re
import uuid

import pytest

from uuid_mcp.server import call_tool

@pytest.mark.asyncio
async def test_generate_uuid_version_1():
    responses = await call_tool("generate_uuid", {"version": 1})
    assert len(responses) == 1
    message = responses[0].text
    assert message.startswith("Generated UUID (version 1): ")
    uuid_str = message.split(": ")[-1]
    generated_uuid = uuid.UUID(uuid_str)
    assert generated_uuid.version == 1

@pytest.mark.asyncio
async def test_generate_uuid_version_4():
    responses = await call_tool("generate_uuid", {"version": 4})
    assert len(responses) == 1
    message = responses[0].text
    assert message.startswith("Generated UUID (version 4): ")
    uuid_str = message.split(": ")[-1]
    generated_uuid = uuid.UUID(uuid_str)
    assert generated_uuid.version == 4

@pytest.mark.asyncio
async def test_generate_uuid_unsupported_version():
    responses = await call_tool("generate_uuid", {"version": 2})
    assert len(responses) == 1
    assert responses[0].text == "Error: Unsupported UUID version"
