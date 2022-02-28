import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('streamlit 超入門')

st.write('DataFrame')

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})

st.dataframe(df.style.highlight_max(axis=0), width=200, height=200)  #動的なデータ表示

st.table(df.style.highlight_max(axis=0))   #静的なデータ表示

#マークダウンの書き方``(マジックコマンド)でpythonのコードを書ける
"""

```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""

#グラフは~chartを使用。マッピング
df_2 = pd.DataFrame(
    np.random.rand(100,2)/[50 ,50] + [35.69, 139.7],
    columns=['lat', 'lon']
)

st.map(df_2)

st.write('Display Image')

img = Image.open('image.png')

st.image(img, caption='人', use_column_width=True)