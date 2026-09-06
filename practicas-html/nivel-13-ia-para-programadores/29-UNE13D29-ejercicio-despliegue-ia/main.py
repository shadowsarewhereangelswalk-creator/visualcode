import os
config={"host":"0.0.0.0","port":int(os.getenv("PORT","8000")),"environment":os.getenv("APP_ENV","production"),"debug":False}
for clave,valor in config.items(): print(clave,valor)
