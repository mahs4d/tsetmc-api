import json
import pickle
import traceback
import zipfile
from os import path, makedirs, walk
from shutil import rmtree

from .asset import Asset
from .utils import daterange


def _zipdir(tmp_dir, destination_zipfile):
    with zipfile.ZipFile(destination_zipfile, 'w', zipfile.ZIP_LZMA) as ziph:
        for root, dirs, files in walk(tmp_dir):
            for file in files:
                ziph.write(path.join(root, file), arcname=file)


class DataPack:
    def __init__(self, asset, from_date, to_date, snapshots_1m, snapshots_5m, snapshots_10m, snapshots_30m,
                 snapshots_1h):
        self.asset = asset
        self.from_date = from_date
        self.to_date = to_date
        self.snapshots_1m = snapshots_1m
        self.snapshots_5m = snapshots_5m
        self.snapshots_10m = snapshots_10m
        self.snapshots_30m = snapshots_30m
        self.snapshots_1h = snapshots_1h

    def save_to(self, output_directory):
        tmp_dir = path.expanduser('~/.tsetmc-api/tmp')

        rmtree(tmp_dir, ignore_errors=True)
        makedirs(tmp_dir)

        with open(path.join(tmp_dir, f'snapshots_1m.pickle'), 'wb') as fp:
            pickle.dump(self.snapshots_1m, fp)

        with open(path.join(tmp_dir, f'snapshots_5m.pickle'), 'wb') as fp:
            pickle.dump(self.snapshots_5m, fp)

        with open(path.join(tmp_dir, f'snapshots_10m.pickle'), 'wb') as fp:
            pickle.dump(self.snapshots_10m, fp)

        with open(path.join(tmp_dir, f'snapshots_30m.pickle'), 'wb') as fp:
            pickle.dump(self.snapshots_30m, fp)

        with open(path.join(tmp_dir, f'snapshots_1h.pickle'), 'wb') as fp:
            pickle.dump(self.snapshots_1h, fp)

        with open(path.join(tmp_dir, f'info.json'), 'w') as fp:
            info = {
                'version': 1,
                'asset_id': self.asset.asset_id,
                'short_name': self.asset.short_name,
                'full_name': self.asset.full_name,
                'from_date': f'{self.from_date.year}-{self.from_date.month}-{self.from_date.day}',
                'to_date': f'{self.to_date.year}-{self.to_date.month}-{self.to_date.day}',
            }
            json.dump(info, fp)

        output_filename = f"{info['asset_id']}_{info['from_date']}_{info['to_date']}_v{info['version']}.zip"
        _zipdir(tmp_dir, path.join(output_directory, output_filename))
        rmtree(tmp_dir, ignore_errors=True)

    @staticmethod
    def generate_datapack(asset, from_date, to_date):
        snapshots_1m = []
        snapshots_5m = []
        snapshots_10m = []
        snapshots_30m = []
        snapshots_1h = []
        for single_date in daterange(from_date, to_date):
            while True:
                try:
                    print(f'{single_date.year}-{single_date.month}-{single_date.day}')

                    asset_day = asset.get_day_details(single_date.year, single_date.month, single_date.day)

                    s1m = asset_day.get_snapshots_by_resolution('1m', 60)
                    s5m = asset_day.get_snapshots_by_resolution('5m', 300)
                    s10m = asset_day.get_snapshots_by_resolution('10m', 600)
                    s30m = asset_day.get_snapshots_by_resolution('30m', 1800)
                    s1h = asset_day.get_snapshots_by_resolution('1h', 3600)

                    snapshots_1m.extend(s1m)
                    snapshots_5m.extend(s5m)
                    snapshots_10m.extend(s10m)
                    snapshots_30m.extend(s30m)
                    snapshots_1h.extend(s1h)

                    break
                except ValueError:
                    break
                except:
                    traceback.print_exc()

        return DataPack(asset, from_date, to_date, snapshots_1m, snapshots_5m, snapshots_10m, snapshots_30m,
                        snapshots_1h)

    @staticmethod
    def load_datapack(pack_address):
        with zipfile.ZipFile(pack_address, 'r') as zp:
            info = json.loads(zp.read('info.json'))
            snapshots_1m = pickle.loads(zp.read('snapshots_1m.pickle'))
            snapshots_5m = pickle.loads(zp.read('snapshots_5m.pickle'))
            snapshots_10m = pickle.loads(zp.read('snapshots_10m.pickle'))
            snapshots_30m = pickle.loads(zp.read('snapshots_30m.pickle'))
            snapshots_1h = pickle.loads(zp.read('snapshots_1h.pickle'))

            return DataPack(Asset(info['asset_id'], info['short_name'], info['full_name']), info['from_date'],
                            info['to_date'], snapshots_1m, snapshots_5m, snapshots_10m, snapshots_30m, snapshots_1h)
