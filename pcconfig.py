import pynecone as pc

config = pc.Config(
    app_name="ragnarok_expedition_pet",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
