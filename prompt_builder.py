import argparse

def build(subject, style=None, extra=None):
    parts = [subject.strip()]
    if style:
        parts.append(f"{style} style")
    if extra:
        parts.append(extra.strip())
    return ", ".join(p for p in parts if p)

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Format a generation prompt")
    ap.add_argument("subject")
    ap.add_argument("--style")
    ap.add_argument("--extra")
    a = ap.parse_args()
    print(build(a.subject, a.style, a.extra))
