import os

from mcp.server.transport_security import TransportSecuritySettings
from weather import mcp


if __name__ == "__main__":
    # Render가 배포된 서비스의 도메인을 자동으로 제공합니다.
    public_host = os.environ["RENDER_EXTERNAL_HOSTNAME"]

    security = TransportSecuritySettings(
        allowed_hosts=[
            public_host,
            f"{public_host}:*",
            "localhost:*",
            "127.0.0.1:*",
        ],
        allowed_origins=[
            f"https://{public_host}",
        ],
    )

    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", "10000")),
        stateless_http=True,
        transport_security=security,
    )
