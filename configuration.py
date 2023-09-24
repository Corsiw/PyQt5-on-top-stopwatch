import json


class Configuration:
    @staticmethod
    def getConfig() -> dict:
        try:
            with open("config.json", "r", encoding='utf-8') as f:
                config = json.load(f)
                if Configuration.checkConfig(config):
                    return config
                else:
                    return Configuration.genConfig()
        except Exception:
            return Configuration.genConfig()

    @staticmethod
    def genConfig() -> dict:
        config = {"textColor": "255, 255, 255",
                  "windowColor": "0, 0, 0",
                  "baseOpacity": 0.7,
                  "noFocusOpacity": 0.45}
        with open("config.json", "w", encoding='utf-8') as f:
            json.dump(config, f, ensure_ascii=False)
        return config

    @staticmethod
    def checkConfig(config: dict) -> bool:
        if "textColor" not in config.keys():
            return False
        textColor = config["textColor"]
        r, g, b = map(int, textColor.split(", "))
        if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
            return False

        if "windowColor" not in config.keys():
            return False
        r, g, b = map(int, config["textColor"].split(", "))
        if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
            return False

        if "baseOpacity" not in config.keys():
            return False
        if not (0 < config["baseOpacity"] <= 1):
            return False

        if "noFocusOpacity" not in config.keys():
            return False
        if not (0 < config["noFocusOpacity"] <= 1):
            return False

        return True


if __name__ == '__main__':
    print(Configuration.getConfig())
