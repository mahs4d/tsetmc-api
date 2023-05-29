from tsetmc_api.group import Group


def method_sync():
	# اطلاعات گروه‌ها
	all_groups = Group.get_all_groups()
	print(f'all groups({len(all_groups)}):\n', '\n'.join(f'\t {item}' for item in all_groups[-5:]))


async def method_async():
	# اطلاعات گروه‌ها
	all_groups = await Group.aio_get_all_groups()
	print(f'all groups({len(all_groups)}):\n', '\n'.join(f'\t {item}' for item in all_groups[-5:]))


if __name__ == '__main__':
	print('RunMode: Sync')
	method_sync()
	
	print('RunMode: Async')
	
	from asyncio import run
	
	run(method_async())
