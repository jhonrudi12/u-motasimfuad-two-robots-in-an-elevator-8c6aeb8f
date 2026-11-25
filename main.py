# Entry for "Two Robots in an Elevator".
# Writes one funny line of awkward robot small talk to /output/entry.txt.
# Deterministic, no network, no input: the same line every run.
import os

ENTRY = (
    "Do you ever count the floors just to avoid eye contact, "
    "or is that a bug only I have?"
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
