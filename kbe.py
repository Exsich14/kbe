def load(path: str) -> dict:
    data = {}

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            if "=" not in line:
                raise ValueError(f"Invalid line in KBE: {line}")

            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip()

            if (value.startswith('"') and value.endswith('"')) or \
               (value.startswith("'") and value.endswith("'")):
                value = value[1:-1]

            elif value in ("True", "False"):
                value = value == "True"

            elif value.isdigit():
                value = int(value)

            else:
                try:
                    value = float(value)
                except:
                    pass

            data[key] = value

    return data

def get(path: str, key: str):
    config = load(path)
    return config.get(key, None)

def set(path: str, key: str, value):
    config = load(path)

    config[key] = value

    lines = []
    for k, v in config.items():
        if isinstance(v, str):
            v = f'"{v}"'
        elif isinstance(v, bool):
            v = "True" if v else "False"
        lines.append(f"{k}={v}")

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
