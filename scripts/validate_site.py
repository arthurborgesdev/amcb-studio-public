#!/usr/bin/env python3
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1] / "docs"


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag not in {"a", "link"}:
            return
        attributes = dict(attrs)
        key = "href"
        if attributes.get(key):
            self.links.append(str(attributes[key]))


def local_target(source: Path, href: str) -> Path | None:
    parsed = urlparse(href)
    if parsed.scheme or parsed.netloc or href.startswith(('#', 'mailto:')):
        return None
    target = (source.parent / parsed.path).resolve()
    if parsed.path.endswith('/'):
        target /= "index.html"
    return target


def main() -> int:
    errors: list[str] = []
    pages = sorted(ROOT.rglob("*.html"))
    if not pages:
        errors.append("Nenhuma página HTML encontrada.")

    for app in ("uploadfit", "pdf-target", "batch-fit", "sample-fit"):
        for filename in ("index.html", "privacy.html"):
            path = ROOT / "apps" / app / filename
            if not path.is_file():
                errors.append(f"Página obrigatória ausente: {path}")

    for page in pages:
        parser = LinkParser()
        parser.feed(page.read_text(encoding="utf-8"))
        for href in parser.links:
            target = local_target(page, href)
            if target is not None and not target.is_file():
                errors.append(f"Link quebrado em {page}: {href}")

    if errors:
        for error in errors:
            print(f"ERRO: {error}")
        return 1
    print(f"Site válido: {len(pages)} páginas HTML e links locais íntegros.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
