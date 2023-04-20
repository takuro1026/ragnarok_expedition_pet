import pynecone as pc

# config = pc.Config(
#     app_name="app",
#     db_url="sqlite:///pynecone.db",
#     env=pc.Env.DEV,
# )

config = pc.Config(
    app_name="app",
    port=80,
    api_url="http://localhost:8000",
    bun_path="$HOME/.bun/bin/bun",
    db_url="sqlite:///pynecone.db",
)
