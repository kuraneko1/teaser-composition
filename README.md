[English](README.en.md)

# Teaser Composition

ティザー画像やキービジュアルを、主役の大きさ・余白・視線・文字組みから設計し、コードで制作するスキル集です。参照画像の構図を骨格として読み、題材に合わせた新しいビジュアルへ展開します。DSH（DeepSeek Harness）のスキルとしてそのまま動き、Codex 形式のメタデータも同梱しています。

## 特徴

- 余白、幾何学、製図、ピクセル、光、流れ、コラージュ、標本、立体、天体、風景、作例の12種類の構図から選べる
- タイトルの実際の文字で複数の書体を比較し、字間・改行・縮小時の見え方まで調整する
- 画像生成や提供画像は必要な素材だけに使い、文字と配置はコードで制御する
- 各構図に描画スターター（Python + Pillow / CairoSVG）と設定例を同梱

## インストール

~~~bash
git clone https://github.com/kuraneko1/teaser-composition.git
cd teaser-composition
./install.sh
~~~

`install.sh` が行うこと:

1. `skills/teaser-*`（13個）を `~/.dsh/skills/` へ symlink
2. `.venv` を作り `requirements.txt`（Pillow / numpy / CairoSVG）を導入
3. `~/.local/bin/teaser-render` を設置

DSH はスキルディレクトリを監視しているので再起動は不要です。作業中のセッションでも、次のターンには `/teaser-composition` が一覧に載ります。

オプション: `--copy`（symlink ではなくコピー。リポジトリを更新したら再実行）、`--no-env`（Python 環境を作らない）、`--no-skills`（スキルの設置だけ省略）。設置先は `DSH_SKILLS_DIR` と `BIN_DIR` で変更できます。

### 必要なもの

- Python 3.10 以降（`python3-venv`）
- システムの Cairo（`libcairo2`）— CairoSVG のラスタライズに使う
- 日本語フォント（Noto Sans CJK など）。`--font` で任意のフォントを指定できる

## 使い方

DSH のチャットでスキルを呼びます。

~~~text
/teaser-composition 新しいAIモデルのティザーを3案。文字と配置はコードで仕上げて。
~~~

12の型は直接呼べます（`/teaser-atmosphere`、`/teaser-orbit` など）。参照画像・用途・サイズ・表示したい文言・書体やブランド指定があれば一緒に渡してください。

コードだけで試す:

~~~bash
teaser-render --list
teaser-render atmosphere --title "NOVA" --output out/nova.png
teaser-render orbit --preset source-102 --width 1200 --height 1200 --output out/orbit.png
~~~

`teaser-render <型> [render.py の引数…]` は、その型の `scripts/render.py` を共通 venv で実行する薄いラッパーです。PNG・SVG・解決済み JSON が同時に出ます。`--config`、`--preset`、`--title`、`--subtitle`、`--variant`、`--width`、`--height`、`--seed`、`--font`、`--glyph`、`--asset`、`--list-presets` が使えます。

## 12の構図

| 構図 | スキル | 核 |
|---|---|---|
| 余白と気配 | `/teaser-atmosphere` | 文字が主役。背景は低周波の気配 |
| 大胆な幾何学 | `/teaser-geometry` | 巨大な円・斜線と中央の文字軸 |
| 製図と構造 | `/teaser-drafting` | 設計途中の線と作図空間 |
| モジュール・ピクセル | `/teaser-pixel` | 端で切れた大モチーフと小さいカード |
| 奥行きへ吸い込む光 | `/teaser-radial` | 収束する光と小さな主役 |
| 面・粒子の流れ | `/teaser-flow` | 連続する面が一瞬だけ像になる |
| 編集的コラージュ | `/teaser-editorial` | 異素材の接ぎ目と不均衡 |
| 標本が作る文字 | `/teaser-specimen` | 遠目に1文字、近くで数十の標本 |
| 象徴的な立体 | `/teaser-object` | 一つの立体に触覚と期待を凝縮 |
| 天体のスケール | `/teaser-orbit` | 端で切る巨大さと小さな文字 |
| 風景と文字レイヤー | `/teaser-scenic` | 場面の中の人と独立した文字 |
| 作例と実画面 | `/teaser-proof` | 成果の密度で根拠を示す |

分類データと参照元の対応は [`references/catalog.json`](skills/teaser-composition/references/catalog.json)、書体の指針は [`references/typography.md`](skills/teaser-composition/references/typography.md) にあります。

## 構成

- [`skills/teaser-composition/SKILL.md`](skills/teaser-composition/SKILL.md)：構図の選択、素材の扱い、タイポグラフィの指針
- `skills/teaser-*`：12種類の構図別スキル。各スキルが `SKILL.md`、`scripts/`、`presets.json`、`examples/`、`references/` を持つ
- `install.sh`：DSH への設置、Python 環境、`teaser-render`
- `scripts/smoke.sh`：12型すべてを描画して確認する

## Codex で使う場合

frontmatter と `agents/openai.yaml` は Codex 互換のままです。

~~~bash
mkdir -p ~/.codex/skills
cp -R skills/teaser-* ~/.codex/skills/
~~~

## 注意

参考画像についての構図分析を含みますが、第三者の参考画像自体は同梱していません。参照元のロゴやビジュアルを複製するのではなく、構図の考え方を別の題材に応用します。フォントや生成素材の利用・再配布条件は、それぞれの提供元で確認してください。
