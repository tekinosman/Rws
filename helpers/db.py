import aioredis

async def posts():
	client = await aioredis.create_redis_pool(("127.0.0.1", 6379))
	pipe = client.multi_exec()
	pipe.hgetall("p:1", encoding = "utf-8")
	pipe.hgetall("p:2", encoding = "utf-8")
	pipe.hgetall("p:3", encoding = "utf-8")
	data = await pipe.execute()
	client.close()
	await client.wait_closed()
	return data
