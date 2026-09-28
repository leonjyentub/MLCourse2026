"""Build missing companion notebooks for numbered Marp decks.

The 00--11 notebooks migrate and consolidate the original course notebooks.
The 12--25 notebooks are short CPU-only teaching experiments adapted from the
fixed handson-mlp snapshot and, where relevant, MachineLearning2025 examples.
"""
from __future__ import annotations

from pathlib import Path
import re

import nbformat
from nbformat.v4 import new_code_cell, new_markdown_cell, new_notebook


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = ROOT / "notebooks"
HANDSON_COMMIT = "47eba45aacc85feae51ba7db68dd1ca66cb25e0a"
TEACHER_COMMIT = "3da2cb56b9efd17d7cd34602589f392554b40603"

KERNEL_METADATA = {
    "kernelspec": {
        "display_name": "MLCourse2026 (uv)",
        "language": "python",
        "name": "mlcourse2026",
    },
    "language_info": {"name": "python", "version": "3.12.10"},
}

COMMON_SETUP = """import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mlcourse.common import SEED, setup, savefig, report
setup()
rng = np.random.default_rng(SEED)"""


def _read(name: str):
    return nbformat.read(NOTEBOOKS / name, as_version=4)


def _module_cells(source_name: str, label: str):
    nb = _read(source_name)
    cells = [new_markdown_cell(f"## {label}\n\n原始分冊：`{source_name}`。內容與已執行輸出完整併入本課同名 Notebook。")]
    cells.extend(nb.cells[1:])
    return cells


def migrate_00_11():
    """Consolidate 17 legacy notebooks into 12 slide-aligned notebooks."""
    legacy_marker = NOTEBOOKS / "01_從資料到線性模型.ipynb"
    if not legacy_marker.exists():
        return

    targets: dict[str, object] = {}

    nb00 = _read("00_環境與重現性.ipynb")
    nb00.cells[0] = new_markdown_cell(
        "# 00｜課程導覽\n\n環境、資料與重現性檢查。對應 `slides/00_課程導覽.md`。"
    )
    nb00.metadata.update(KERNEL_METADATA)
    nb00.metadata["mlcourse"] = {"deck": "00_課程導覽.md", "legacy": ["00_環境與重現性.ipynb"]}
    targets["00_課程導覽.ipynb"] = nb00

    merged = {
        "01_機器學習概觀.ipynb": (
            "01｜機器學習概觀",
            [
                ("01_從資料到線性模型.ipynb", "生活滿意度與線性模型"),
                ("02_驗證正則化與早停.ipynb", "泛化、正則化與早停"),
                ("08_研究延伸與常見陷阱.ipynb", "評估設計與常見陷阱"),
            ],
        ),
        "02_端到端機器學習專案.ipynb": (
            "02｜端到端機器學習專案",
            [
                ("03_房價資料探索與切分.ipynb", "資料探索與切分"),
                ("04_房價Pipeline與模型選擇.ipynb", "Pipeline、模型選擇與最後測試"),
            ],
        ),
        "03_分類與模型評估.ipynb": (
            "03｜分類與模型評估",
            [
                ("05_Iris邏輯斯迴歸與多類別.ipynb", "Iris 邏輯斯迴歸與多類別"),
                ("06_混淆矩陣閾值與ROC.ipynb", "混淆矩陣、閾值與 ROC"),
                ("07_MNIST分類與錯誤分析.ipynb", "MNIST 分類與錯誤分析"),
            ],
        ),
    }
    for target_name, (title, sources) in merged.items():
        cells = [
            new_markdown_cell(
                f"# {title}\n\n對應 `slides/{target_name.removesuffix('.ipynb')}.md`。"
                "原分冊依教學順序合併，各節仍可獨立選講。"
            )
        ]
        for source_name, label in sources:
            cells.extend(_module_cells(source_name, label))
        nb = new_notebook(cells=cells, metadata=KERNEL_METADATA.copy())
        nb.metadata["mlcourse"] = {
            "deck": target_name.removesuffix(".ipynb") + ".md",
            "legacy": [name for name, _ in sources],
        }
        targets[target_name] = nb

    renames = {
        "09_線性模型與最佳化.ipynb": "04_線性模型與最佳化.ipynb",
        "10_正則化與機率分類.ipynb": "05_正則化與機率分類.ipynb",
        "11_決策樹與SVM.ipynb": "06_決策樹與SVM補充.ipynb",
        "12_集成學習與隨機森林.ipynb": "07_集成學習與隨機森林.ipynb",
        "13_降維與資料表示.ipynb": "08_降維與資料表示.ipynb",
        "14_分群與表示應用.ipynb": "09_分群與表示應用.ipynb",
        "15_密度分群與機率模型.ipynb": "10_密度分群與機率模型.ipynb",
        "16_人工神經網路入門.ipynb": "11_人工神經網路入門.ipynb",
    }
    for source_name, target_name in renames.items():
        nb = _read(source_name)
        title = target_name.removesuffix(".ipynb").replace("_", "｜", 1)
        nb.cells[0] = new_markdown_cell(
            f"# {title}\n\n對應 `slides/{target_name.removesuffix('.ipynb')}.md`。"
            f"本檔由 `{source_name}` 改名，程式與已執行輸出保留。"
        )
        nb.metadata.update(KERNEL_METADATA)
        nb.metadata["mlcourse"] = {
            "deck": target_name.removesuffix(".ipynb") + ".md",
            "legacy": [source_name],
        }
        targets[target_name] = nb

    old_paths = list(NOTEBOOKS.glob("*.ipynb"))
    for path in old_paths:
        path.unlink()
    for name, nb in targets.items():
        nbformat.write(nb, NOTEBOOKS / name)


def source_markdown(handson: str, cells: str, teacher: str | None = None) -> str:
    teacher_line = ""
    if teacher:
        teacher_line = (
            f"\n- `MachineLearning2025/{teacher}`，固定 commit `{TEACHER_COMMIT}`。"
        )
    return f"""## 來源與改編界線

- Aurélien Géron，`handson-mlp/{handson}`，固定 commit `{HANDSON_COMMIT}`，參考 {cells}。
{teacher_line}
- 本 Notebook 為課堂短實驗：保留核心張量、演算法或評估流程，改用 NumPy／scikit-learn 與小型資料，讓 CPU 能快速重跑。
- 圖表與數值是本檔實際執行結果，不代表原書完整模型成效。原始程式授權與歸屬見 `../NOTICE.md`。"""


SPECS = {
    "12_深層神經網路訓練_梯度與遷移": {
        "summary": "用梯度範數與深度尺度理解消失、爆炸與裁剪。",
        "source": source_markdown(
            "11_training_deep_neural_networks.ipynb",
            "Glorot／He 初始化、Gradient Clipping、Transfer Learning",
            "06_ANN_from_Scratch_MNIST.py",
        ),
        "code": """depth = np.array([1, 2, 5, 10, 20])
sigmoid_upper = 0.25 ** depth
scale_table = pd.DataFrame({'depth': depth, 'sigmoid_derivative_upper_bound': sigmoid_upper})

gradient = np.array([3.0, 4.0, 12.0])
before = np.linalg.norm(gradient)
clip_norm = 5.0
clipped = gradient * min(1.0, clip_norm / before)
after = np.linalg.norm(clipped)
print(f'gradient norm: {before:.1f} -> {after:.1f}')
scale_table""",
        "plot": """plt.semilogy(depth, sigmoid_upper, 'o-', label=r'$(1/4)^L$')
plt.axhline(1e-6, color='tab:red', ls='--', label='1e-6')
plt.xlabel('number of saturated sigmoid layers')
plt.ylabel('upper bound of derivative product')
plt.title('Repeated small derivatives shrink the backward signal')
plt.legend()
savefig('12_gradient_transfer_demo')
report('deep_gradient_transfer', {'gradient_norm_before': before, 'gradient_norm_after': after,
                                  'depths': depth.tolist(), 'sigmoid_upper': sigmoid_upper.tolist()})""",
    },
    "13_深層神經網路訓練_最佳化與正則化": {
        "summary": "在同一個狹長損失面比較一般梯度下降與 Momentum。",
        "source": source_markdown(
            "11_training_deep_neural_networks.ipynb",
            "Momentum、Adam、Learning Rate Scheduling、Regularization",
            "01_batchgradientDescent.ipynb；02_Regularization_Regression.ipynb；02_Polynomial_Regression_Early_stopping.ipynb",
        ),
        "code": """A = np.diag([1.0, 30.0])
def optimize(momentum=0.0, eta=0.035, steps=80):
    theta = np.array([4.0, 1.5]); velocity = np.zeros(2); losses = []
    for _ in range(steps):
        losses.append(0.5 * theta @ A @ theta)
        grad = A @ theta
        velocity = momentum * velocity + grad
        theta -= eta * velocity
    return np.array(losses), theta

plain_loss, plain_theta = optimize(momentum=0.0)
mom_loss, mom_theta = optimize(momentum=0.8)
pd.DataFrame({'method': ['GD', 'Momentum'], 'final_loss': [plain_loss[-1], mom_loss[-1]],
              'theta_0': [plain_theta[0], mom_theta[0]], 'theta_1': [plain_theta[1], mom_theta[1]]})""",
        "plot": """plt.semilogy(plain_loss, label='gradient descent')
plt.semilogy(mom_loss, label='momentum=0.8')
plt.xlabel('update'); plt.ylabel('quadratic loss'); plt.title('Momentum crosses the shallow direction faster')
plt.legend()
savefig('13_optimizer_regularization_demo')
report('optimizer_regularization', {'gd_final_loss': plain_loss[-1], 'momentum_final_loss': mom_loss[-1]})""",
    },
    "14_卷積神經網路_影像特徵與架構": {
        "summary": "手算與程式同時檢查 2D 互相關、ReLU 與最大池化。",
        "source": source_markdown(
            "12_deep_computer_vision_with_cnns.ipynb",
            "Cells 20–61（卷積與池化）",
            "06_ANN_from_Scratch_MNIST.py",
        ),
        "code": """X = np.array([[1, 2, 0], [0, 1, 3], [2, 1, 0]], dtype=float)
K = np.array([[1, 0], [0, -1]], dtype=float)
Y = np.empty((2, 2))
for i in range(2):
    for j in range(2):
        Y[i, j] = np.sum(X[i:i+2, j:j+2] * K)  # 深度學習框架採互相關慣例
relu = np.maximum(Y, 0)
pooled = relu.max()
print('cross-correlation output:\\n', Y)
print('after ReLU:', relu.tolist(), ' max pool:', pooled)""",
        "plot": """fig, axes = plt.subplots(1, 3, figsize=(10, 3))
for ax, arr, title in zip(axes, [X, K, Y], ['input', 'kernel', 'output']):
    im = ax.imshow(arr, cmap='coolwarm'); ax.set_title(title)
    for (i, j), value in np.ndenumerate(arr): ax.text(j, i, f'{value:g}', ha='center', va='center')
    ax.set_xticks([]); ax.set_yticks([])
savefig('14_convolution_demo')
report('convolution_demo', {'output': Y.tolist(), 'relu': relu.tolist(), 'max_pool': pooled})""",
    },
    "15_電腦視覺_遷移學習與偵測分割": {
        "summary": "用 IoU 與 NMS 小例子連接偵測框、信心分數與後處理。",
        "source": source_markdown(
            "12_deep_computer_vision_with_cnns.ipynb",
            "Cells 78–104（遷移學習）、125–131（物件偵測）",
        ),
        "code": """boxes = np.array([[0.10,0.10,0.55,0.55], [0.16,0.14,0.58,0.57], [0.62,0.58,0.92,0.90]])
scores = np.array([0.92, 0.81, 0.74])
def iou(a, b):
    lo = np.maximum(a[:2], b[:2]); hi = np.minimum(a[2:], b[2:])
    inter = np.prod(np.maximum(hi - lo, 0))
    area_a = np.prod(a[2:] - a[:2]); area_b = np.prod(b[2:] - b[:2])
    return inter / (area_a + area_b - inter)
keep = []
for idx in np.argsort(scores)[::-1]:
    if all(iou(boxes[idx], boxes[j]) < 0.5 for j in keep): keep.append(int(idx))
table = pd.DataFrame(boxes, columns=['x1','y1','x2','y2']).assign(score=scores, kept=[i in keep for i in range(3)])
print('IoU(box 0, box 1)=', round(iou(boxes[0], boxes[1]), 3))
table""",
        "plot": """from matplotlib.patches import Rectangle
fig, axes = plt.subplots(1, 2, figsize=(9, 4))
for ax, ids, title in [(axes[0], range(3), 'before NMS'), (axes[1], keep, 'after NMS')]:
    for i in ids:
        x1,y1,x2,y2 = boxes[i]
        ax.add_patch(Rectangle((x1,y1), x2-x1, y2-y1, fill=False, lw=3, label=f'{scores[i]:.2f}'))
    ax.set(xlim=(0,1), ylim=(1,0), title=title); ax.legend()
savefig('15_detection_demo')
report('vision_detection', {'keep': keep, 'iou_0_1': iou(boxes[0], boxes[1])})""",
    },
    "16_序列模型_RNN與時間序列預測": {
        "summary": "把連續時間序列切成視窗，嚴格使用過去預測下一步。",
        "source": source_markdown(
            "13_processing_sequences_using_rnns_and_cnns.ipynb",
            "Cells 19–35、47–62（時間序列、視窗與 Simple RNN）",
        ),
        "code": """from sklearn.linear_model import LinearRegression
t = np.arange(240)
series = np.sin(t / 12) + 0.35 * np.sin(t / 3.5) + rng.normal(0, 0.08, len(t))
window = 12
X = np.stack([series[i:i+window] for i in range(len(series)-window)])
y = series[window:]
split = 170
model = LinearRegression().fit(X[:split], y[:split])
pred = model.predict(X[split:])
persistence = X[split:, -1]
rmse = lambda a,b: float(np.sqrt(np.mean((a-b)**2)))
pd.Series({'window_model_RMSE': rmse(y[split:], pred), 'persistence_RMSE': rmse(y[split:], persistence)})""",
        "plot": """idx = np.arange(split+window, len(series))
plt.plot(idx, y[split:], label='actual')
plt.plot(idx, pred, label='window model')
plt.plot(idx, persistence, alpha=.6, label='persistence')
plt.xlabel('time'); plt.ylabel('value'); plt.title('Forecast uses only the previous 12 values')
plt.legend()
savefig('16_sequence_demo')
report('sequence_forecast', {'window_RMSE': rmse(y[split:], pred), 'persistence_RMSE': rmse(y[split:], persistence)})""",
    },
    "17_自然語言處理_詞嵌入與注意力": {
        "summary": "由詞嵌入計算 scaled dot-product attention，直接讀權重矩陣。",
        "source": source_markdown(
            "14_nlp_with_rnns_and_attention.ipynb",
            "Cell 39（embeddings）、Cells 210–214（attention）",
        ),
        "code": """tokens = ['我', '喜歡', '機器', '學習']
E = np.array([[1.,0.,0.], [.8,.2,0.], [0.,.8,.4], [0.,.6,.8]])
Q = K = V = E
scores = Q @ K.T / np.sqrt(E.shape[1])
weights = np.exp(scores - scores.max(axis=1, keepdims=True))
weights /= weights.sum(axis=1, keepdims=True)
context = weights @ V
pd.DataFrame(weights, index=tokens, columns=tokens).round(3)""",
        "plot": """plt.imshow(weights, cmap='Blues', vmin=0, vmax=weights.max())
plt.xticks(range(4), tokens); plt.yticks(range(4), tokens)
plt.xlabel('key token'); plt.ylabel('query token'); plt.title('Scaled dot-product attention weights')
for (i,j), value in np.ndenumerate(weights): plt.text(j, i, f'{value:.2f}', ha='center', va='center')
savefig('17_attention_demo')
report('nlp_attention', {'tokens': tokens, 'weights': weights.tolist(), 'context': context.tolist()})""",
    },
    "18_Transformer_注意力架構與預訓練": {
        "summary": "位置編碼加上 causal mask，驗證第 t 個 token 不會看到未來。",
        "source": source_markdown(
            "15_transformers_for_nlp_and_chatbots.ipynb",
            "Cells 31、35、46（位置編碼、遮罩、多頭注意力）",
        ),
        "code": """n, d = 6, 4
pos = np.arange(n)[:, None]
freq = np.exp(np.arange(0, d, 2) * (-np.log(10000.0) / d))
pe = np.zeros((n, d)); pe[:, 0::2] = np.sin(pos * freq); pe[:, 1::2] = np.cos(pos * freq)
scores = pe @ pe.T / np.sqrt(d)
causal_mask = np.triu(np.ones((n, n), dtype=bool), k=1)
masked = np.where(causal_mask, -1e9, scores)
weights = np.exp(masked - masked.max(axis=1, keepdims=True)); weights /= weights.sum(1, keepdims=True)
print('future attention mass:', weights[causal_mask].sum())
pd.DataFrame(weights).round(3)""",
        "plot": """plt.imshow(weights, cmap='magma', vmin=0, vmax=1)
plt.colorbar(label='attention weight'); plt.xlabel('key position'); plt.ylabel('query position')
plt.title('Causal self-attention is lower triangular')
savefig('18_transformer_mask_demo')
report('transformer_mask', {'future_mass': weights[causal_mask].sum(), 'weights': weights.tolist()})""",
    },
    "19_大型語言模型_生成與聊天系統": {
        "summary": "在固定 logits 上比較 greedy 與 top-k 抽樣，觀察溫度的影響。",
        "source": source_markdown(
            "15_transformers_for_nlp_and_chatbots.ipynb",
            "Decoder-only Transformers、generation 與 chatbot 區段",
        ),
        "code": """vocab = np.array(['資料', '模型', '學習', '風險', '答案'])
logits = np.array([1.2, 2.4, 1.8, 0.4, 1.0])
def probs(temp):
    z = logits / temp; p = np.exp(z-z.max()); return p/p.sum()
def sample_top_k(temp=1.0, k=3, n=8):
    p = probs(temp); ids = np.argsort(p)[-k:]; q = p[ids]/p[ids].sum()
    return rng.choice(vocab[ids], size=n, p=q)
rows = pd.DataFrame({'token': vocab, 'p_T0.7': probs(.7), 'p_T1.3': probs(1.3)})
print('greedy:', vocab[np.argmax(logits)])
print('top-k sample:', ' '.join(sample_top_k()))
rows.round(3)""",
        "plot": """x = np.arange(len(vocab)); w = .36
plt.bar(x-w/2, probs(.7), w, label='temperature 0.7')
plt.bar(x+w/2, probs(1.3), w, label='temperature 1.3')
plt.xticks(x, vocab); plt.ylabel('probability'); plt.title('Temperature changes distribution sharpness')
plt.legend()
savefig('19_sampling_demo')
report('llm_sampling', {'vocab': vocab.tolist(), 'p_07': probs(.7).tolist(), 'p_13': probs(1.3).tolist()})""",
    },
    "20_視覺與多模態Transformer": {
        "summary": "把影像切成 patches，再以正規化向量比較圖文相似度。",
        "source": source_markdown(
            "16_vision_and_multimodal_transformers.ipynb",
            "ViT From Scratch、CLIP 區段",
        ),
        "code": """image = np.arange(16).reshape(4,4)
patches = np.stack([image[i:i+2,j:j+2].ravel() for i in (0,2) for j in (0,2)])
image_emb = np.array([[.9,.1], [.2,.8]])
text_emb = np.array([[1.,0.], [0.,1.], [.7,.7]])
labels = ['貓', '街景', '戶外動物']
norm = lambda x: x / np.linalg.norm(x, axis=1, keepdims=True)
sim = norm(image_emb) @ norm(text_emb).T
print('patch matrix:\\n', patches)
pd.DataFrame(sim, index=['image_A','image_B'], columns=labels).round(3)""",
        "plot": """plt.imshow(sim, cmap='viridis', vmin=0, vmax=1)
plt.xticks(range(3), labels); plt.yticks(range(2), ['image_A','image_B'])
plt.colorbar(label='cosine similarity'); plt.title('Normalized image-text similarity')
for (i,j), value in np.ndenumerate(sim): plt.text(j, i, f'{value:.2f}', ha='center', va='center', color='white')
savefig('20_multimodal_demo')
report('multimodal', {'patches': patches.tolist(), 'similarity': sim.tolist()})""",
    },
    "21_Transformer加速_推論與參數高效微調": {
        "summary": "量化 KV cache 的計算差異，並計算 LoRA 的可訓練參數量。",
        "source": source_markdown(
            "17_speeding_up_transformers.ipynb",
            "Key/Value Caching、MQA／GQA、Faster Training 區段",
        ),
        "code": """lengths = np.array([16, 32, 64, 128, 256])
without_cache = lengths * (lengths + 1) / 2
with_cache = lengths
d_in = d_out = 4096; rank = 8
full = d_in * d_out
lora = rank * (d_in + d_out)
table = pd.DataFrame({'sequence_length': lengths,
                      'projected_token_states_without_cache': without_cache.astype(int),
                      'with_KV_cache': with_cache,
                      'ratio': without_cache / with_cache})
print(f'LoRA trainable parameters: {lora:,} vs full matrix {full:,} ({lora/full:.3%})')
table""",
        "plot": """plt.loglog(lengths, without_cache, 'o-', label='recompute prefix')
plt.loglog(lengths, with_cache, 's-', label='KV cache')
plt.xlabel('generated sequence length'); plt.ylabel('projected token states')
plt.title('KV cache avoids repeated key/value projections'); plt.legend()
savefig('21_transformer_efficiency_demo')
report('transformer_efficiency', {'lora_params': lora, 'full_params': full, 'table': table.to_dict('records')})""",
    },
    "22_生成模型_自編碼器GAN與擴散": {
        "summary": "用線性欠完備自編碼器的等價案例 PCA 觀察壓縮與重建誤差。",
        "source": source_markdown(
            "18_autoencoders_gans_and_diffusion_models.ipynb",
            "Performing PCA with an Undercomplete Linear Autoencoder、Diffusion Models",
            "04_PCA_from_scratch.py；04_SVD_from_scratch.py",
        ),
        "code": """from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
digits = load_digits()
X = digits.data / 16.0
pca = PCA(n_components=12, random_state=SEED).fit(X)
Z = pca.transform(X); recon = pca.inverse_transform(Z)
errors = np.mean((X-recon)**2, axis=1)
idx = [0, 1, int(np.argmax(errors))]
pd.DataFrame({'sample': idx, 'label': digits.target[idx], 'reconstruction_MSE': errors[idx]}).round(4)""",
        "plot": """fig, axes = plt.subplots(2, 3, figsize=(7, 5))
for col, i in enumerate(idx):
    axes[0,col].imshow(X[i].reshape(8,8), cmap='gray'); axes[0,col].set_title(f'original {digits.target[i]}')
    axes[1,col].imshow(recon[i].reshape(8,8), cmap='gray'); axes[1,col].set_title(f'reconstruction\\nMSE={errors[i]:.3f}')
    axes[0,col].axis('off'); axes[1,col].axis('off')
savefig('22_generative_demo')
report('generative_models', {'components': 12, 'mean_MSE': errors.mean(), 'samples': idx})""",
    },
    "23_強化學習_策略價值與深度RL": {
        "summary": "以兩臂 bandit 示範探索、回饋與增量式價值估計。",
        "source": source_markdown(
            "19_reinforcement_learning.ipynb",
            "Neural Network Policies、Policy Gradients、Q-Learning 區段",
        ),
        "code": """true_means = np.array([0.2, 0.8])
Q = np.zeros(2); counts = np.zeros(2, dtype=int); rewards = []
epsilon = 0.12
for step in range(300):
    action = rng.integers(2) if rng.random() < epsilon else int(np.argmax(Q))
    reward = rng.normal(true_means[action], 0.25)
    counts[action] += 1
    Q[action] += (reward - Q[action]) / counts[action]
    rewards.append(reward)
pd.DataFrame({'arm': [0,1], 'pulls': counts, 'estimated_value': Q, 'true_mean': true_means}).round(3)""",
        "plot": """rewards = np.array(rewards)
moving = np.convolve(rewards, np.ones(25)/25, mode='valid')
plt.plot(np.arange(24, len(rewards)), moving)
plt.axhline(true_means.max(), color='tab:red', ls='--', label='best arm mean')
plt.xlabel('interaction'); plt.ylabel('25-step mean reward'); plt.title('Exploration gradually identifies the better action')
plt.legend()
savefig('23_rl_demo')
report('reinforcement_learning', {'counts': counts.tolist(), 'Q': Q.tolist(), 'mean_reward': rewards.mean()})""",
    },
    "24_附錄A_自動微分與計算圖": {
        "summary": "以中央差分檢查解析梯度，並觀察步長過大或過小的誤差。",
        "source": source_markdown(
            "Appendix_A_autodiff.ipynb",
            "Cells 6、17–23（數值微分與 toy computation graph）",
            "06_ANN_from_Scratch_MNIST.py",
        ),
        "code": """def f(x, y): return x*x*y + y + 2
x, y, check_eps = 3.0, 4.0, 1e-5
analytic = np.array([2*x*y, x*x+1])
numeric_f = np.array([(f(x+check_eps,y)-f(x-check_eps,y))/(2*check_eps),
                      (f(x,y+check_eps)-f(x,y-check_eps))/(2*check_eps)])

# f 對 x 是二次式，中央差分會特別精準；另用非多項式 g 觀察步長誤差。
def g(v): return np.sin(v) * np.exp(v/10)
g_prime = np.exp(x/10) * (np.cos(x) + 0.1*np.sin(x))
eps_values = np.logspace(-1, -14, 14)
numeric_g = np.array([(g(x+e)-g(x-e))/(2*e) for e in eps_values])
errors = np.abs(numeric_g-g_prime)
best = int(np.argmin(errors))
print('f analytic gradient:', analytic, ' finite difference:', numeric_f)
print('g best epsilon:', eps_values[best], 'error:', errors[best])""",
        "plot": """plt.loglog(eps_values, errors, 'o-')
plt.axvline(eps_values[best], color='tab:red', ls='--', label=f'best eps={eps_values[best]:.0e}')
plt.gca().invert_xaxis(); plt.xlabel('epsilon'); plt.ylabel('gradient error')
plt.title('Finite differences fail when epsilon is too large or too small'); plt.legend()
savefig('24_autodiff_demo')
report('autodiff', {'f_analytic': analytic.tolist(), 'f_numeric': numeric_f.tolist(),
                    'g_best_epsilon': eps_values[best], 'g_best_error': errors[best]})""",
    },
    "25_附錄B_混合精度與量化": {
        "summary": "執行對稱 int8 量化，直接比較原權重、整數碼與反量化誤差。",
        "source": source_markdown(
            "Appendix_B_mixed_precision_and_quantization.ipynb",
            "Reduced Precision Models、Symmetric Linear Quantization、Dynamic Quantization",
        ),
        "code": """weights = np.array([[-1.20, -0.35, 0.0, 0.42, 1.05], [0.18, -0.77, 0.63, 0.91, -0.12]])
scale = np.max(np.abs(weights)) / 127
q = np.clip(np.round(weights / scale), -127, 127).astype(np.int8)
dequant = q.astype(float) * scale
err = dequant - weights
table = pd.DataFrame({'weight': weights.ravel(), 'int8': q.ravel(),
                      'dequantized': dequant.ravel(), 'error': err.ravel()})
print('scale:', scale, ' max abs error:', np.max(np.abs(err)))
table.round(5)""",
        "plot": """x = np.arange(weights.size)
plt.plot(x, weights.ravel(), 'o-', label='float')
plt.plot(x, dequant.ravel(), 'x--', label='dequantized int8')
plt.xlabel('weight index'); plt.ylabel('value'); plt.title('Symmetric int8 quantization')
plt.legend()
savefig('25_quantization_demo')
report('quantization', {'scale': scale, 'max_abs_error': np.max(np.abs(err)), 'codes': q.tolist()})""",
    },
}


def build_12_25():
    for stem, spec in SPECS.items():
        if (NOTEBOOKS / f"{stem}.ipynb").exists():
            continue
        number, title = stem.split("_", 1)
        cells = [
            new_markdown_cell(
                f"# {number}｜{title}\n\n{spec['summary']}\n\n"
                f"對應 `slides/{stem}.md`；從第一格依序執行即可重現投影片中的表格與圖。"
            ),
            new_markdown_cell(spec["source"]),
            new_code_cell(COMMON_SETUP),
            new_markdown_cell("## 課堂小實驗"),
            new_code_cell(spec["code"]),
            new_markdown_cell("## 執行結果圖"),
            new_code_cell(spec["plot"]),
            new_markdown_cell(
                "## 解讀與延伸\n\n先描述圖或表直接支持的結果，再說明這個縮編實驗不能代表完整模型的哪些面向。"
            ),
        ]
        nb = new_notebook(cells=cells, metadata=KERNEL_METADATA.copy())
        nb.metadata["mlcourse"] = {
            "deck": f"{stem}.md",
            "handson_commit": HANDSON_COMMIT,
            "teacher_commit": TEACHER_COMMIT,
            "profile": "cpu-short-demo",
        }
        nbformat.write(nb, NOTEBOOKS / f"{stem}.ipynb")


def main():
    NOTEBOOKS.mkdir(parents=True, exist_ok=True)
    migrate_00_11()
    build_12_25()
    from prepare_colab_notebooks import main as prepare_colab
    prepare_colab()
    names = sorted(path.stem for path in NOTEBOOKS.glob("*.ipynb"))
    assert len(names) == 26, names
    assert names == [f"{i:02d}_" + names[i].split("_", 1)[1] for i in range(26)]
    print(f"Built {len(names)} slide-aligned notebooks")


if __name__ == "__main__":
    main()
