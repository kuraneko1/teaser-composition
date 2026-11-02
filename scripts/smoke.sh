#!/usr/bin/env bash
# 全12型が描画できるか確認する。出力は一時ディレクトリ。
set -euo pipefail
REPO="$(cd "$(dirname "$0")/.." && pwd -P)"
OUT="$(mktemp -d)"
fail=0
for d in "$REPO"/skills/teaser-*; do
  [ -f "$d/scripts/render.py" ] || continue
  type="$(basename "$d" | sed 's/^teaser-//')"
  cfg="$d/examples/default.json"
  [ -f "$cfg" ] || cfg=""
  if "$REPO/.venv/bin/python" "$d/scripts/render.py" --config "$cfg" --title "スモークテスト" --output "$OUT/$type.png" >/dev/null 2>"$OUT/$type.err"; then
    echo "ok   $type"
  else
    echo "FAIL $type"; sed -n '1,6p' "$OUT/$type.err"
    fail=1
  fi
done
echo "output: $OUT"
exit "$fail"
