import os.path
import yaml

from geektime.service.petclinic.utils.log import log


class Data:
    @classmethod
    def load_yaml(cls, path):
        yaml_path = os.path.join(
            os.path.realpath(
                os.path.dirname(
                    os.path.dirname(__file__))), path)

        with open(yaml_path) as f:
            env = yaml.safe_load(f)
            log.debug(env)
            return env