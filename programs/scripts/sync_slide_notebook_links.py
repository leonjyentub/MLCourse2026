"""Add one companion-notebook link and one code/result slide to each Marp deck."""
from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
SLIDES = ROOT / "slides"

LEGACY_REFS = {
    "01_從資料到線性模型.ipynb": "01_機器學習概觀.ipynb",
    "02_驗證正則化與早停.ipynb": "01_機器學習概觀.ipynb",
    "08_研究延伸與常見陷阱.ipynb": "01_機器學習概觀.ipynb",
    "03_房價資料探索與切分.ipynb": "02_端到端機器學習專案.ipynb",
    "04_房價Pipeline與模型選擇.ipynb": "02_端到端機器學習專案.ipynb",
    "05_Iris邏輯斯迴歸與多類別.ipynb": "03_分類與模型評估.ipynb",
    "06_混淆矩陣閾值與ROC.ipynb": "03_分類與模型評估.ipynb",
    "07_MNIST分類與錯誤分析.ipynb": "03_分類與模型評估.ipynb",
}

RESULTS = {
    "01": ("01_lifesat_linear_knn.png", "model.fit(X, y)\nmodel.predict([[37_655]])", "同一份生活滿意度資料可比較線性模型與近鄰模型，先看資料與假設再讀預測。"),
    "02": ("03_housing_geography.png", "train, test = housing_split()\ntrain.plot.scatter('longitude', 'latitude')", "圖只使用訓練資料；地理位置與房價的關係需連同人口密度一起解讀。"),
    "03": ("07_multiclass_confusion.png", "y_oof = cross_val_predict(clf, X, y, cv=3)\nConfusionMatrixDisplay.from_predictions(y, y_oof)", "折外預測產生的混淆矩陣可用於錯誤分析，最後測試集仍保留到決策完成後。"),
    "04": ("09_gradient_learning_rate.png", "theta -= eta * gradient\n# 比較 eta=0.02、0.30、1.05", "學習率過小收斂慢，適中可收斂，過大會讓損失發散。"),
    "05": ("10_regularization_paths.png", "for alpha in alphas:\n    Ridge(alpha=alpha).fit(X, y)", "正則化強度改變係數大小；比較前要固定資料切分與特徵縮放流程。"),
    "06": ("11_tree_regularization.png", "DecisionTreeClassifier(max_depth=depth,\n                       random_state=42).fit(X, y)", "限制樹深會平滑決策邊界；是否改善泛化仍要看驗證結果。"),
    "07": ("12_gradient_boosting_stages.png", "residual = y - model.predict(X)\nnext_tree.fit(X, residual)", "平方損失下，每一棵新樹擬合目前殘差，集成預測逐步修正。"),
    "08": ("13_pca_reconstruction.png", "Z = pca.fit_transform(X_train)\nX_hat = pca.inverse_transform(Z)", "降維保留主要變異，同時造成重建誤差；維度選擇要連回下游任務。"),
    "09": ("14_kmeans_selection.png", "km = KMeans(n_clusters=k, n_init=10)\nscore = silhouette_score(X, km.fit_predict(X))", "inertia 會隨 k 下降，輪廓分數提供另一個群內緊密與群間分離的角度。"),
    "10": ("15_gmm_ellipses.png", "gmm = GaussianMixture(n_components=3)\ngmm.fit(X)", "GMM 以機率描述橢圓形群集；共變異限制會改變模型自由度與邊界。"),
    "11": ("16_tiny_mlp_training.png", "net.step(X_batch, y_batch, lr=0.5)\nvalidation_acc = mean(net.predict(X_val) == y_val)", "同時畫訓練與驗證曲線，才能區分尚未學會與已開始過度擬合。"),
    "12": ("12_gradient_transfer_demo.png", "clipped = g * min(1, max_norm / norm(g))", "13 的梯度範數裁剪為 5；圖顯示多層小導數連乘會快速縮小反向訊號。"),
    "13": ("13_optimizer_regularization_demo.png", "velocity = beta * velocity + gradient\ntheta -= eta * velocity", "在狹長損失面上，Momentum 累積一致方向的更新，減少淺方向的緩慢移動。"),
    "14": ("14_convolution_demo.png", "Y[i, j] = sum(X[i:i+2, j:j+2] * K)", "程式輸出與投影片手算相同：[[0, -1], [-1, 1]]。"),
    "15": ("15_detection_demo.png", "for i in argsort(scores)[::-1]:\n    if all(iou(boxes[i], boxes[j]) < .5 for j in keep): keep.append(i)", "NMS 保留高分框並移除與它高度重疊的候選；閾值本身是任務設定。"),
    "16": ("16_sequence_demo.png", "X[t] = series[t-12:t]\ny[t] = series[t]", "視窗模型只讀過去 12 點；圖同時保留 persistence 基準，避免只看單一模型。"),
    "17": ("17_attention_demo.png", "scores = Q @ K.T / sqrt(d)\nweights = softmax(scores)", "每列代表一個 query 對各 key 的權重，總和為 1；高權重不是因果證明。"),
    "18": ("18_transformer_mask_demo.png", "scores[future_mask] = -inf\nweights = softmax(scores)", "遮罩後未來位置的注意力總量為 0，權重矩陣呈下三角。"),
    "19": ("19_sampling_demo.png", "p = softmax(logits / temperature)\ntoken = sample_top_k(p, k=3)", "較低溫度讓分布更集中；greedy 與抽樣回答的是不同生成策略。"),
    "20": ("20_multimodal_demo.png", "similarity = normalize(image_emb) @ normalize(text_emb).T", "圖文嵌入先正規化，再以餘弦相似度比較；分數只在同一模型空間內有意義。"),
    "21": ("21_transformer_efficiency_demo.png", "lora_params = r * (d_in + d_out)\nfull_params = d_in * d_out", "r=8、d=4096 時，LoRA 訓練 65,536 個參數，約為完整矩陣的 0.391%。"),
    "22": ("22_generative_demo.png", "Z = encoder(X)\nX_hat = decoder(Z)", "線性欠完備自編碼器的教學對照使用 PCA；重建誤差揭示壓縮會捨棄資訊。"),
    "23": ("23_rl_demo.png", "Q[a] += (reward - Q[a]) / count[a]", "epsilon-greedy 保留探索；移動平均獎勵逐步接近較佳動作的期望值。"),
    "24": ("24_autodiff_demo.png", "dfdx = (f(x+eps)-f(x-eps)) / (2*eps)", "有限差分的步長太大有近似誤差，太小則受浮點相消影響。"),
    "25": ("25_quantization_demo.png", "q = round(weight / scale).astype(int8)\nweight_hat = q * scale", "對稱 int8 量化大幅縮小表示範圍，但反量化後仍會留下離散化誤差。"),
}


def add_outcomes_link(part: str, notebook_name: str) -> str:
    if "notebook-companion-link" in part:
        return part
    block = (
        f"\n\n<!-- notebook-companion-link -->\n"
        f"> 💻 **配套 Notebook**：[`{notebook_name}`](../programs/notebooks/{notebook_name})。"
        "程式片段、實際圖表與表格可由此檔重現。\n"
    )
    note = part.find("<!--")
    if note >= 0:
        return part[:note].rstrip() + block + "\n" + part[note:]
    return part.rstrip() + block + "\n"


def result_slide(stem: str, notebook_name: str) -> str:
    number = stem[:2]
    figure, code, observation = RESULTS[number]
    return f"""
<!-- notebook-result-slide -->
<!-- _class: small -->
## 程式實驗與實際輸出

<div class="columns wide-left">
<div>

```python
{code}
```

**觀察**：{observation}

[開啟完整 Notebook](../programs/notebooks/{notebook_name})

</div>
<div>

![h:330 {stem} 的實際執行結果](../programs/outputs/figures/{figure})

</div>
</div>

<!-- 講者提示：程式與圖均來自 programs/notebooks/{notebook_name} 的已執行輸出；來源與改編界線見 Notebook。 -->
""".strip()


def main():
    decks = sorted(path for path in SLIDES.glob("[0-9][0-9]_*.md"))
    assert len(decks) == 26, [path.name for path in decks]
    for path in decks:
        stem = path.stem
        notebook_name = stem + ".ipynb"
        text = path.read_text()
        text = text.replace(
            f"<!-- 程式與圖均來自 programs/notebooks/{notebook_name} 的已執行輸出；來源與改編界線見 Notebook。 -->",
            f"<!-- 講者提示：程式與圖均來自 programs/notebooks/{notebook_name} 的已執行輸出；來源與改編界線見 Notebook。 -->",
        )
        for old, new in LEGACY_REFS.items():
            text = text.replace(old, new)
        parts = re.split(r"^---\s*$", text, flags=re.MULTILINE)
        if len(parts) < 4:
            raise ValueError(f"Unexpected Marp structure: {path}")
        parts[3] = add_outcomes_link(parts[3], notebook_name)
        if stem != "00_課程導覽" and "notebook-result-slide" not in text:
            parts.insert(4, "\n" + result_slide(stem, notebook_name) + "\n")
        path.write_text("---".join(parts))
    print(f"Updated {len(decks)} decks")


if __name__ == "__main__":
    main()
