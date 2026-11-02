#!/usr/bin/env bash
# teaser-composition を DSH のスキルとして使えるようにする。
#
#   ./install.sh              既定: ~/.dsh/skills へ symlink、.venv 作成、teaser-render 設置
#   ./install.sh --copy       コピーで入れる（リポジトリ更新後は再実行）
#   ./install.sh --no-env     Python 環境と teaser-render の作成を省略
#   ./install.sh --no-skills  スキルの設置を省略
#
# 設置先: DSH_SKILLS_DIR（既定 ~/.dsh/skills）, BIN_DIR（既定 ~/.local/bin）
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)"
SKILLS_SRC="$REPO/skills"
DSH_SKILLS_DIR="${DSH_SKILLS_DIR:-$HOME/.dsh/skills}"
BIN_DIR="${BIN_DIR:-$HOME/.local/bin}"
VENV="$REPO/.venv"
REQ="$REPO/requirements.txt"

MODE="link"
DO_SKILLS=1
DO_ENV=1
for arg in "$@"; do
  case "$arg" in
    --copy) MODE="copy" ;;
    --no-env) DO_ENV=0 ;;
    --no-skills) DO_SKILLS=0 ;;
    -h|--help) sed -n '2,9p' "$0"; exit 0 ;;
    *) echo "unknown option: $arg" >&2; exit 2 ;;
  esac
done

if [ "$DO_SKILLS" = 1 ]; then
  mkdir -p "$DSH_SKILLS_DIR"
  for src in "$SKILLS_SRC"/teaser-*; do
    [ -f "$src/SKILL.md" ] || continue
    name="$(basename "$src")"
    declared="$(grep -m1 '^name:' "$src/SKILL.md" | sed -e 's/^name:[[:space:]]*//' -e 's/[[:space:]]*$//' -e 's/^"//' -e 's/"$//')"
    if [ "$declared" != "$name" ]; then
      echo "skip $name: frontmatter の name ($declared) がディレクトリ名と違う" >&2
      continue
    fi
    dst="$DSH_SKILLS_DIR/$name"
    if [ "$MODE" = "copy" ]; then
      if [ -e "$dst" ] && [ ! -L "$dst" ]; then
        mv "$dst" "$dst.bak-$(date +%Y%m%d%H%M%S)"
      fi
      rm -rf "$dst"
      cp -R "$src" "$dst"
    else
      if [ -e "$dst" ] && [ ! -L "$dst" ]; then
        echo "skip $name: $dst は実ディレクトリ。退避してから再実行してください" >&2
        continue
      fi
      ln -sfn "$src" "$dst"
    fi
    echo "installed $name -> $dst"
  done
fi

if [ "$DO_ENV" = 1 ]; then
  if [ ! -x "$VENV/bin/python" ]; then
    echo "creating venv: $VENV"
    python3 -m venv "$VENV" || { echo "venv の作成に失敗しました（python3-venv を入れてください）" >&2; exit 1; }
  fi
  "$VENV/bin/pip" install -q --disable-pip-version-check -r "$REQ"
  mkdir -p "$BIN_DIR"
  cat > "$BIN_DIR/teaser-render" <<'WRAPPER'
#!/usr/bin/env bash
# teaser-render <type> [render.py の引数...]
# teaser-composition の描画スターターをリポジトリの .venv で実行する。
set -euo pipefail
REPO="__REPO__"
PY="$REPO/.venv/bin/python"
list_types() { for d in "$REPO"/skills/teaser-*; do [ -f "$d/scripts/render.py" ] || continue; basename "$d" | sed 's/^teaser-//'; done; }
case "${1:-}" in
  ""|-h|--help)
    echo "usage: teaser-render <type> [--config FILE] [--preset ID] [--title T] [--output OUT.png] ..." >&2
    echo "types: $(list_types | tr '\n' ' ')" >&2
    exit 2 ;;
  -l|--list) list_types; exit 0 ;;
  --path) shift; echo "$REPO/skills/teaser-${1:-}"; exit 0 ;;
esac
type="$1"; shift
skill="$REPO/skills/teaser-$type"
if [ ! -f "$skill/scripts/render.py" ]; then
  echo "unknown type: $type" >&2
  echo "types: $(list_types | tr '\n' ' ')" >&2
  exit 2
fi
if [ ! -x "$PY" ]; then
  echo "venv がありません: $REPO で ./install.sh を実行してください" >&2
  exit 1
fi
exec "$PY" "$skill/scripts/render.py" "$@"
WRAPPER
  sed -i "s|__REPO__|$REPO|g" "$BIN_DIR/teaser-render"
  chmod +x "$BIN_DIR/teaser-render"
  echo "installed $BIN_DIR/teaser-render"
fi

echo
echo "完了。DSH はスキルディレクトリを監視しているので、次のターンで一覧に載ります。"
