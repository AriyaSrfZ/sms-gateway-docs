#!/usr/bin/env python3
import glob
import sys
from html.parser import HTMLParser

class HtmlValidator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.errors = []

    def handle_starttag(self, tag, attrs):
        if tag not in ('br', 'hr', 'img', 'input', 'link', 'meta'):
            self.stack.append((tag, self.getpos()))

    def handle_endtag(self, tag):
        if tag not in ('br', 'hr', 'img', 'input', 'link', 'meta'):
            if self.stack and self.stack[-1][0] == tag:
                self.stack.pop()
            else:
                self.errors.append((tag, self.getpos()))

def main():
    failed = False
    for fpath in sorted(glob.glob("docs/*.html")):
        v = HtmlValidator()
        with open(fpath, "r", encoding="utf-8") as f:
            v.feed(f.read())
        if v.stack or v.errors:
            print(f"FAIL {fpath}: unclosed={v.stack}, mismatches={v.errors}", file=sys.stderr)
            failed = True
        else:
            print(f"OK   {fpath}")
    sys.exit(1 if failed else 0)

if __name__ == "__main__":
    main()
