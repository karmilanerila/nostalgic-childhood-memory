"""Write one nostalgic childhood memory sentence to /output/entry.txt.

The sentence is a single concrete memory: on a rainy afternoon, a
grandmother lifts the lid of the rice cooker, rain drums on the tin roof,
steam fogs her glasses, and the ceiling fan clicks overhead. One sentence,
well under 280 characters, plain UTF-8 text, no trailing decoration.
"""

import os


SENTENCE = (
    "Every rainy afternoon my grandmother lifted the lid of the rice "
    "cooker while rain drummed on the tin roof, steam fogged her glasses, "
    "the ceiling fan clicked overhead, and the whole small kitchen smelled "
    "like coming home."
)


def main() -> None:
    text = SENTENCE.strip()
    if not text or len(text) > 280:
        raise SystemExit("entry sentence must be 1-280 non-blank characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(text.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
