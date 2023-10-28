from glob import glob
from importlib import import_module

from loguru import logger


class GetRouters:
    TARGET_FOLDERS = [
        "apps",
    ]
    EXCLUDE_APPS = [
        "auth",
    ]

    @classmethod
    def _get_routers_data(cls, module_name):
        module_name = module_name.replace("/", ".")
        target_module = import_module(module_name)
        module_items = [
            {"name": item_name, "value": getattr(target_module, item_name)}
            for item_name in target_module.__all__
        ]
        return module_items

    @classmethod
    def call(cls, version):
        # scan all 'routers' folders in TARGET_FOLDER recursively
        routers_data = []
        for folder in cls.TARGET_FOLDERS:
            files_with_routers = glob(f"{folder}/**/{version}", recursive=True)
            for module_path in files_with_routers:
                if module_path.split("/")[1] not in cls.EXCLUDE_APPS:
                    try:
                        routers_data += cls._get_routers_data(module_path)
                    except Exception as e:
                        # logger.error(e)
                        raise e
        return routers_data
