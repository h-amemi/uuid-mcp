#!/usr/bin/env python3
import asyncio
import uuid
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent


server = Server("uuid-mcp")


@server.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="generate_uuid",
            description="Generate a new UUID (Universally Unique Identifier)",
            inputSchema={
                "type": "object",
                "properties": {
                    "version": {
                        "type": "integer",
                        "description": "UUID version (1 or 4)",
                        "enum": [1, 4],
                        "default": 4,
                    }
                },
                "additionalProperties": False,
            },
        )
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    if name == "generate_uuid":
        version_value = arguments.get("version", 4)
        try:
            version = int(version_value)
        except (TypeError, ValueError):
            return [
                TextContent(
                    type="text", text="Error: 'version' must be an integer (1 or 4)"
                )
            ]

        if version == 1:
            generated_uuid = str(uuid.uuid1())
        elif version == 4:
            generated_uuid = str(uuid.uuid4())
        else:
            return [TextContent(type="text", text="Error: Unsupported UUID version")]

        return [
            TextContent(
                type="text",
                text=f"Generated UUID (version {version}): {generated_uuid}",
            )
        ]

    return [TextContent(type="text", text=f"Unknown tool: {name}")]


async def main():
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream, write_stream, server.create_initialization_options()
        )


if __name__ == "__main__":
    asyncio.run(main())
