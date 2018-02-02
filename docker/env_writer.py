"""
Creates .env files for docker-compose from prefixed host env vars

Usage: python env_writer.py <path_to_json_config>

Example config:
    {
      "host_env_var_prefix": "DIRECTORY_UI",
      "file_path": ".env",
      "env_vars": {
        "required": [
          "SECRET_KEY",
        ],
        "optional": []
      }
    }
"""
import json
import os
import sys


class DockerComposeEnvWriter:

    @classmethod
    def create(cls, config):
        cls.validate(config)

        all_env_vars = (
            config['env_vars']['required'] + config['env_vars']['optional']
        )

        with open(config['file_path'], 'w') as dest:
            for var in all_env_vars:
                # Get value of the prefixed host env var
                value = os.getenv('{}_{}'.format(
                    config['host_env_var_prefix'],
                    var
                ))
                if value:
                    dest.write("{}={}\n".format(var, value))

    @staticmethod
    def validate(config):
        unset_required_host_vars = [
            var for var in config['env_vars']['required']
            if not os.getenv('{}_{}'.format(
                config['host_env_var_prefix'], var
            ))
        ]

        if unset_required_host_vars:
            sys.exit(
                "Required host environment variables are not set: \n{}".format(
                    "\n".join(unset_required_host_vars)
                )
            )


if __name__ == '__main__':
    # TODO: change to docopt
    for path_to_config in sys.argv[1:]:
        with open(path_to_config, 'r') as src:
            config = json.load(src)

        DockerComposeEnvWriter.create(config)
