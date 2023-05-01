import pynecone as pc

# config = pc.Config(
#     app_name="app",
#     db_url="sqlite:///pynecone.db",
#     env=pc.Env.DEV,
# )

config = pc.Config(
    app_name="app",
    port=3000,
    backend_port=5566,
    api_url="https://ro-monster-arena-backend.takurohuang.com",
    bun_path="$HOME/.bun/bin/bun",
    db_url="sqlite:///pynecone.db",
)
