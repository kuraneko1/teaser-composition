# モジュール・ピクセルと端の重心 — 構成の読み

これらは画像の見え方からの解釈。作者の発言や公式の制作意図ではない。

## 統合した理由

Mistralの猫・花・盾・砂時計・音声の各シリーズは、格子上の巨大モチーフと小さな象徴という共通設計。素材単体SVGも完成画と別役割のまま同じ系統に統合する。

## 構成

ピクセルのキャラクターを飾るだけでなく、大きな色面と小さなアイコンの落差で世界観を作る。端で切れた巨大モチーフと、中央付近の小さいカードの関係が重要。

巨大モチーフは左または右の40–55%を占め、画面端から切る。対側45%程度を暗く低密度に保つ。小カードは x=43–65%, y=30–70% を目安。格子のピッチを全要素で共有する。

## 応用

企業の既存キャラをコピーせず、オリジナルの工具・植物・動物へ置換。端・色・カード有無・左右の重心を変える。

## 元画像への対応

IDはZIP全体の固定ID。完全重複も消さず別名として保持。寸法・ハッシュ・透過情報は `source-map.json`。

### 041 — leanstral

`europe-china-main/mistral/leanstral/teaser/release-Cover-Model-Leanstral_2cGQ3n.webp`

役割: complete / サブタイプ: cover

左上から裁ち落とす巨大な記号と右の空白の差。サムネイルでは小さなカードを中間スケールとして加える。

### 042 — leanstral

`europe-china-main/mistral/leanstral/teaser/release-Thumbnail-Model-Leanstral_1EHlSs.webp`

役割: complete / サブタイプ: thumbnail

左上から裁ち落とす巨大な記号と右の空白の差。サムネイルでは小さなカードを中間スケールとして加える。

### 043 — leanstral

`europe-china-main/mistral/leanstral/teaser/release-og-Thumbnail-Model-Leanstral.jpg`

役割: complete / サブタイプ: thumbnail

左上から裁ち落とす巨大な記号と右の空白の差。サムネイルでは小さなカードを中間スケールとして加える。

### 044 — mistral-large-4

`europe-china-main/mistral/mistral-large-4/teaser/release-hero-ml4.jpg`

役割: background / サブタイプ: cover

暗い格子とごく弱い立体の面だけがある背景素材。コントラストを強くしないこと自体が、上に載る情報の席を作る。

### 045 — mistral-large-4

`europe-china-main/mistral/mistral-large-4/teaser/release-hf-blog-thumbnail.png`

役割: complete / サブタイプ: partner

黒地に少数のピクセル記号と中央の短い文章。ブランドの関係を上下の階層で伝える告知カード。

### 046 — mistral-large-4

`europe-china-main/mistral/mistral-large-4/teaser/release-og-cover-mistral-sovereign.webp`

役割: complete / サブタイプ: partner

上半分の白地が言葉を読ませ、下半分の暖色の段が視線を横へ運ぶ。小さなキャラが巨大な面の物差しになる。

### 047 — mistral-large-4

`europe-china-main/mistral/mistral-large-4/teaser/release-oss-hero-cat-signal.svg`

役割: material / サブタイプ: asset

猫・机・投影の独立したSVGパーツ。完成バナーでなく、巨大な余白を持つ場面へ組み込む部品として扱う。

### 048 — mistral-large-4

`europe-china-main/mistral/mistral-large-4/teaser/release-oss-hero-desktop.svg`

役割: material / サブタイプ: asset

猫・机・投影の独立したSVGパーツ。完成バナーでなく、巨大な余白を持つ場面へ組み込む部品として扱う。

### 049 — mistral-large-4

`europe-china-main/mistral/mistral-large-4/teaser/release_x-post.jpg`

役割: complete / サブタイプ: duo

明るい暖色の左と暗い寒色の右を二分し、似た猫のシルエットを対照させる。色だけでなく環境の温度差を作る。

### 050 — mistral-medium-3-5

`europe-china-main/mistral/mistral-medium-3-5/teaser/release-Cover-Model-Medium_2iiBU6.webp`

役割: complete / サブタイプ: cover

左下から広がる青い巨大モチーフを切り、右上に静域。中央の小カードは、巨大背景と細部の間にスケールの段を作る。

### 051 — mistral-medium-3-5

`europe-china-main/mistral/mistral-medium-3-5/teaser/release-Thumbnail-Model-Medium_1LAgDu.webp`

役割: complete / サブタイプ: thumbnail

左下から広がる青い巨大モチーフを切り、右上に静域。中央の小カードは、巨大背景と細部の間にスケールの段を作る。

### 052 — mistral-medium-3-5

`europe-china-main/mistral/mistral-medium-3-5/teaser/release-og-Thumbnail-Model-Medium.jpg`

役割: complete / サブタイプ: thumbnail

左下から広がる青い巨大モチーフを切り、右上に静域。中央の小カードは、巨大背景と細部の間にスケールの段を作る。

### 053 — mistral-small-4

`europe-china-main/mistral/mistral-small-4/teaser/release-Cover-Model-Small_ryVwl.webp`

役割: complete / サブタイプ: cover

右側の大きな花と茎を端で切る。暗い背景版と明るいサムネイル版は、同じモチーフで静域の役割を入れ替える。

### 054 — mistral-small-4

`europe-china-main/mistral/mistral-small-4/teaser/release-Thumbnail-Model-Small_ZyGfKX.webp`

役割: complete / サブタイプ: thumbnail

右側の大きな花と茎を端で切る。暗い背景版と明るいサムネイル版は、同じモチーフで静域の役割を入れ替える。

### 055 — mistral-small-4

`europe-china-main/mistral/mistral-small-4/teaser/release-og-Thumbnail-Model-Small.jpg`

役割: complete / サブタイプ: thumbnail

右側の大きな花と茎を端で切る。暗い背景版と明るいサムネイル版は、同じモチーフで静域の役割を入れ替える。

### 056 — ocr-4

`europe-china-main/mistral/ocr-4/teaser/release-hero-ocr4-image.jpg`

役割: material / サブタイプ: asset

本としおりを大きなセルで表す独立アイコン。小さくても本と読める輪郭を優先し、装飾を増やさない。

### 057 — ocr-4

`europe-china-main/mistral/ocr-4/teaser/release-ocr.svg`

役割: material / サブタイプ: asset

本としおりを大きなセルで表す独立アイコン。小さくても本と読める輪郭を優先し、装飾を増やさない。

### 058 — ocr-4

`europe-china-main/mistral/ocr-4/teaser/release-og-OCR-OG.png`

役割: complete / サブタイプ: cover-title

左の言葉と右のカード群が対置され、中央の本が両者を接続する。文書処理という機能をレイアウトで示す。

### 059 — shieldstral

`europe-china-main/mistral/shieldstral/teaser/release-Cover-Model_Cover-Shieldstral-2x_2pnxcN.webp`

役割: complete / サブタイプ: cover

暖色の巨大な左の面と寒色の右の面が接する。盾の小さいカードを境界へ置き、保護という意味を面の関係に重ねる。

### 060 — shieldstral

`europe-china-main/mistral/shieldstral/teaser/release-Thumbnail-Model_Shieldstral-2x_ZUxlF0.webp`

役割: complete / サブタイプ: thumbnail

暖色の巨大な左の面と寒色の右の面が接する。盾の小さいカードを境界へ置き、保護という意味を面の関係に重ねる。

### 061 — shieldstral

`europe-china-main/mistral/shieldstral/teaser/release-og-Thumbnail-Model-Shieldstral.jpg`

役割: complete / サブタイプ: thumbnail

暖色の巨大な左の面と寒色の右の面が接する。盾の小さいカードを境界へ置き、保護という意味を面の関係に重ねる。

### 062 — timestral

`europe-china-main/mistral/timestral/teaser/release-Thumbnail-Blog-timestral_Z5Y2JF.webp`

役割: complete / サブタイプ: thumbnail

右の大きな砂時計に対して左を暗く空ける。カード版・文字版・背景版で、同じ重心を使い分ける。

### 063 — timestral

`europe-china-main/mistral/timestral/teaser/release-og-og-timestral.webp`

役割: complete / サブタイプ: cover-title

右の大きな砂時計に対して左を暗く空ける。カード版・文字版・背景版で、同じ重心を使い分ける。

### 064 — timestral

`europe-china-main/mistral/timestral/teaser/release-timestral-cover_2ikDAq.webp`

役割: complete / サブタイプ: cover

右の大きな砂時計に対して左を暗く空ける。カード版・文字版・背景版で、同じ重心を使い分ける。

### 065 — voxtral-3

`europe-china-main/mistral/voxtral-3/teaser/release-agent.svg`

役割: material / サブタイプ: asset

平坦な色面で作る人物の単体素材。身体や顔の最小セル構成が識別性を支える。

### 066 — voxtral-3

`europe-china-main/mistral/voxtral-3/teaser/release-og-hero-blog-voxtral.png`

役割: complete / サブタイプ: cover

右端で切れた巨大な音声のモチーフと、ほぼ黒い左の静域。タイトルなしでも重心が成立する背景型。

### 067 — voxtral-transcribe-2

`europe-china-main/mistral/voxtral-transcribe-2/teaser/release-og-Thumbnail-Model-Voxtral.jpg`

役割: complete / サブタイプ: thumbnail

大きい青のモチーフと小さいマイクのカードの対比。カードは真正面で、背景の切れた形だけに勢いを持たせる。

### 068 — voxtral-tts

`europe-china-main/mistral/voxtral-tts/teaser/release-Thumbnail-Model-Voxtral-1_Z2s01JB.webp`

役割: complete / サブタイプ: thumbnail

大きい青のモチーフと小さいマイクのカードの対比。カードは真正面で、背景の切れた形だけに勢いを持たせる。

### 069 — voxtral-tts

`europe-china-main/mistral/voxtral-tts/teaser/release-hero-blog-voxtral_Z2kTJq2.webp`

役割: complete / サブタイプ: cover

右端で切れた巨大な音声のモチーフと、ほぼ黒い左の静域。タイトルなしでも重心が成立する背景型。

### 070 — voxtral-tts

`europe-china-main/mistral/voxtral-tts/teaser/release-og-Thumbnail-Model-Voxtral-1.jpg`

役割: complete / サブタイプ: thumbnail

大きい青のモチーフと小さいマイクのカードの対比。カードは真正面で、背景の切れた形だけに勢いを持たせる。

