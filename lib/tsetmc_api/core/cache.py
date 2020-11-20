import os
import pickle
from collections import defaultdict
from os import path

_cache_dir = os.getenv('TSETMC_API_CACHE_DIRECTORY', path.expanduser('~/.tsetmc-api/cache'))


class PersistentCache:
    @staticmethod
    def store(major, minor, data):
        final_cache_dir = path.join(_cache_dir, major)
        final_path = path.join(final_cache_dir, f'{minor}.pickle')
        os.makedirs(final_cache_dir, exist_ok=True)

        with open(final_path, 'wb') as fp:
            pickle.dump(data, fp)

    @staticmethod
    def fetch(major, minor):
        final_path = path.join(_cache_dir, major, f'{minor}.pickle')

        try:
            with open(final_path, 'rb') as fp:
                return pickle.load(fp)
        except FileNotFoundError:
            return None

    @staticmethod
    def exists(major, minor):
        final_path = path.join(_cache_dir, major, f'{minor}.pickle')
        return path.exists(final_path)

    @staticmethod
    def remove(major, minor):
        if PersistentCache.exists(major, minor):
            final_path = path.join(_cache_dir, major, f'{minor}.pickle')
            os.unlink(final_path)


class MemoryCache:
    _cache = defaultdict(dict)

    @staticmethod
    def store(major, minor, data):
        MemoryCache._cache[major][minor] = data

    @staticmethod
    def fetch(major, minor):
        return MemoryCache._cache[major].get(minor, None)

    @staticmethod
    def exists(major, minor):
        return minor in MemoryCache._cache[major]

    @staticmethod
    def remove(major, minor):
        if MemoryCache.exists(major, minor):
            del MemoryCache._cache[major][minor]

    @staticmethod
    def clear(self):
        MemoryCache._cache.clear()
